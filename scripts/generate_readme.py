import os
import sys
import glob
import json
import logging
from typing import Dict, Callable
import anthropic
import openai

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_env_var(name: str, default: str = '') -> str:
    """Safely get an environment variable."""
    return os.environ.get(name, default)

def load_file_types() -> Dict[str, str]:
    """Load file types from configuration file."""
    config_path = '.github/config/file_types.json'
    try:
        with open(config_path, 'r') as f:
            file_types = json.load(f)
        logging.info(f"Loaded file types: {json.dumps(file_types, indent=2)}")
        return file_types
    except (json.JSONDecodeError, FileNotFoundError) as e:
        logging.error(f"Error loading file types from {config_path}: {e}")
        return {}

def get_file_contents(file_path: str) -> str:
    """Read and return file contents."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except IOError as e:
        logging.error(f"Error reading file {file_path}: {e}")
        return ""

def scan_repository(file_types: Dict[str, str]) -> str:
    """Scan repository and return content of all matched files."""
    repo_content = []
    for file_type, glob_pattern in file_types.items():
        logging.info(f"Scanning for {file_type} files with pattern: {glob_pattern}")
        files = glob.glob(glob_pattern, recursive=True)
        logging.info(f"Found {len(files)} {file_type} files")
        if files:
            repo_content.append(f"\n{file_type}:")
            for file in files:
                content = get_file_contents(file)
                if content:
                    repo_content.append(f"\n--- {file} ---\n{content}")
    return "\n".join(repo_content)

def chunk_content(content: str, chunk_size: int = 4000) -> list[str]:
    """Split content into chunks of specified size."""
    return [content[i:i+chunk_size] for i in range(0, len(content), chunk_size)]

def generate_readme_with_anthropic(prompt: str) -> str:
    """Generate README using Anthropic API."""
    client = anthropic.Anthropic(api_key=get_env_var('ANTHROPIC_API_KEY'))
    chunks = chunk_content(prompt)
    full_response = ""
    for chunk in chunks:
        try:
            message = client.messages.create(
                model=get_env_var('AI_MODEL'),
                max_tokens=4000,
                messages=[{"role": "user", "content": chunk}]
            )
            full_response += message.content[0].text
        except anthropic.APIError as e:
            logging.error(f"Anthropic API error: {e}")
            raise
    return full_response

def generate_readme_with_openai(prompt: str) -> str:
    """Generate README using OpenAI API."""
    client = openai.OpenAI(api_key=get_env_var('OPENAI_API_KEY'))
    chunks = chunk_content(prompt)
    full_response = ""
    for chunk in chunks:
        try:
            response = client.chat.completions.create(
                model=get_env_var('AI_MODEL'),
                messages=[{"role": "user", "content": chunk}],
                max_tokens=4000
            )
            full_response += response.choices[0].message.content
        except openai.OpenAIError as e:
            logging.error(f"OpenAI API error: {e}")
            raise
    return full_response

def get_ai_provider() -> Callable[[str], str]:
    """Get the appropriate AI provider function with fallback."""
    primary_provider = get_env_var('AI_PROVIDER', '').lower()
    fallback_provider = 'openai' if primary_provider == 'anthropic' else 'anthropic'
    
    providers = {
        'anthropic': (generate_readme_with_anthropic, 'ANTHROPIC_API_KEY'),
        'openai': (generate_readme_with_openai, 'OPENAI_API_KEY')
    }

    for provider in [primary_provider, fallback_provider]:
        generate_func, api_key = providers.get(provider, (None, None))
        if generate_func and get_env_var(api_key):
            logging.info(f"Using {provider.capitalize()} as the AI provider")
            return generate_func
    
    raise ValueError("No valid AI provider available")

def update_readme_section(existing_content: str, new_content: str, section: str) -> str:
    """Update a specific section in README without duplication."""
    section_marker = f"## {section}"
    next_section_pattern = "\n## "
    
    # Extract the new section content
    section_start = new_content.find(section_marker)
    if section_start == -1:
        return existing_content
        
    section_end = new_content.find(next_section_pattern, section_start + len(section_marker))
    if section_end == -1:
        section_end = len(new_content)
        
    section_content = new_content[section_start:section_end].strip()
    
    # Replace or append section in existing content
    start_index = existing_content.find(section_marker)
    if start_index == -1:
        return f"{existing_content}\n\n{section_content}"
        
    end_index = existing_content.find(next_section_pattern, start_index + len(section_marker))
    if end_index == -1:
        end_index = len(existing_content)
        
    return f"{existing_content[:start_index]}{section_content}{existing_content[end_index:]}"

def generate_readme():
    """Main function to generate README."""
    try:
        file_types = load_file_types()
        if not file_types:
            logging.warning("No file types specified")
            return

        repo_content = scan_repository(file_types)
        if not repo_content:
            logging.info("No matching files found")
            return

        prompt = f"""Generate a README.md with exactly these sections:

## Project Description
[Project overview and main features]

## Installation
[Installation steps]

## Usage
[Usage instructions]

## Contributing
[Contributing guidelines]

Base the content on this repository structure:
{repo_content}"""

        generate_readme_func = get_ai_provider()
        new_readme_content = generate_readme_func(prompt)

        try:
            with open('README.md', 'r') as f:
                existing_readme = f.read()
        except FileNotFoundError:
            existing_readme = ""

        # Update each section once
        sections = ["Project Description", "Installation", "Usage", "Contributing"]
        for section in sections:
            existing_readme = update_readme_section(existing_readme, new_readme_content, section)

        with open('README.md', 'w') as f:
            f.write(existing_readme.strip() + '\n')

        logging.info("README.md updated successfully")
        print("readme_generated=true")
        
    except Exception as e:
        logging.error(f"Error generating README: {e}")
        print("readme_generated=false")
        sys.exit(1)

if __name__ == "__main__":
    generate_readme()