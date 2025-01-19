# AI-Powered README Generator

Based on the repository content, I'll generate a README.md file that accurately reflects the project:

# Automated README Generator

## Project Description
This project provides a sophisticated automation tool for generating and updating README.md files for software repositories. It uses AI services (both Anthropic and OpenAI) to analyze repository content and create comprehensive documentation automatically.

The generator supports multiple file types and can process repository content in chunks, making it suitable for repositories of any size. It includes robust error handling and logging capabilities to ensure reliable operation.

Based on the repository content, I'll generate a README.md file that accurately reflects the project:

# Automated README Generator

## Project Description
This project provides a sophisticated automation tool for generating and updating README.md files for software repositories. It uses AI services (both Anthropic and OpenAI) to analyze repository content and create comprehensive documentation automatically.

The generator supports multiple file types and can process repository content in chunks, making it suitable for repositories of any size. It includes robust error handling and logging capabilities to ensure reliable operation.

## Installation

1. Clone the repository
2. Install required dependencies:
```bash
pip install anthropic openai
```

3. Set up environment variables:
- `ANTHROPIC_API_KEY`: Your Anthropic API key
- `OPENAI_API_KEY`: Your OpenAI API key
- `AI_MODEL`: The AI model to use for generation

Based on the repository content, I'll generate a README.md file that accurately reflects the project:

# Automated README Generator

## Project Description
This project provides a sophisticated automation tool for generating and updating README.md files for software repositories. It uses AI services (both Anthropic and OpenAI) to analyze repository content and create comprehensive documentation automatically.

The generator supports multiple file types and can process repository content in chunks, making it suitable for repositories of any size. It includes robust error handling and logging capabilities to ensure reliable operation.

## Installation

1. Clone the repository
2. Install required dependencies:
```bash
pip install anthropic openai
```

3. Set up environment variables:
- `ANTHROPIC_API_KEY`: Your Anthropic API key
- `OPENAI_API_KEY`: Your OpenAI API key
- `AI_MODEL`: The AI model to use for generation

## Usage

The main script (`scripts/generate_readme.py`) provides several key functions:

1. **File Type Configuration**
   - Define file types to scan in `.github/config/file_types.json`
   - The script will automatically detect and process files matching the configured patterns

2. **Content Processing**
   - Scans repository for specified file types
   - Reads and processes file contents
   - Chunks large content for optimal API processing

3. **README Generation**
   - Supports both Anthropic and OpenAI APIs
   - Generates structured documentation based on repository content
   - Includes error handling and logging for reliable operation

Example usage:
```python
python scripts/generate_readme.py
```

Based on the repository content, I'll generate a README.md file that accurately reflects the project:

# Automated README Generator

## Project Description
This project provides a sophisticated automation tool for generating and updating README.md files for software repositories. It uses AI services (both Anthropic and OpenAI) to analyze repository content and create comprehensive documentation automatically.

The generator supports multiple file types and can process repository content in chunks, making it suitable for repositories of any size. It includes robust error handling and logging capabilities to ensure reliable operation.

## Installation

1. Clone the repository
2. Install required dependencies:
```bash
pip install anthropic openai
```

3. Set up environment variables:
- `ANTHROPIC_API_KEY`: Your Anthropic API key
- `OPENAI_API_KEY`: Your OpenAI API key
- `AI_MODEL`: The AI model to use for generation

## Usage

The main script (`scripts/generate_readme.py`) provides several key functions:

1. **File Type Configuration**
   - Define file types to scan in `.github/config/file_types.json`
   - The script will automatically detect and process files matching the configured patterns

2. **Content Processing**
   - Scans repository for specified file types
   - Reads and processes file contents
   - Chunks large content for optimal API processing

3. **README Generation**
   - Supports both Anthropic and OpenAI APIs
   - Generates structured documentation based on repository content
   - Includes error handling and logging for reliable operation

Example usage:
```python
python scripts/generate_readme.py
```

## Contributing

To contribute to this project:

1. Fork the repository
2. Create a feature branch
3. Make your changes, ensuring to:
   - Follow the existing code style
   - Add appropriate error handling
   - Include logging statements
   - Update documentation as needed
4. Submit a pull request

Please make sure to:
- Test your changes thoroughly
- Update any relevant documentation
- Add appropriate logging statements for new functionality
- Follow existing error handling patterns

## Technical Details

The project includes the following key components:

- `generate_readme.py`: Main script containing:
  - Environment variable management
  - File type configuration loading
  - Repository content scanning
  - Content chunking
  - AI API integration (Anthropic and OpenAI)
  - Comprehensive logging
  - Error handling

The script uses type hints and follows Python best practices for code organization and error handling.I'll analyze this Python script and the partial README.md content to provide a comprehensive explanation of how the code works.

This code is part of an AI-Powered README Generator with two main functions:

1. `get_ai_provider()`:
- Returns a callable function that will handle README generation
- Implements a fallback mechanism between Anthropic and OpenAI
- Key features:
  - Checks environment variables for the primary AI provider preference
  - Creates a fallback to an alternative provider if the primary one isn't available
  - Validates API keys for both providers
  - Returns the appropriate generation function or raises an error if no valid provider is found

2. `update_readme_section()`:
- Updates specific sections within an existing README file
- Parameters:
  - `existing_content`: Current README content
  - `new_content`: New content to be inserted
  - `section`: Section name to be updated
- Logic:
  - Locates sections using "## " markers
  - Preserves content outside the target section
  - Handles cases where sections don't exist by appending new content

3. `generate_readme()`:
- Main orchestration function that:
  - Loads file type configurations
  - Scans repository content
  - Generates prompts for AI
  - Manages README updates
  - Handles error cases and logging

Key Features of the Implementation:
- Fallback mechanism between AI providers
- Section-specific updates rather than full file replacement
- Environment variable configuration
- Comprehensive error handling and logging
- Clear separation of concerns between functions

The code shows good practices in terms of:
- Type hints
- Error handling
- Configuration management
- Modular design
- Logging implementation

The system is designed to be flexible and maintainable, with clear separation between the AI provider selection, content generation, and file management components.I'll help create a clear and organized README.md based on the repository content. Here's a streamlined version:

# AI-Powered README Generator

## Project Description
This project provides an automated solution for generating and updating README.md files using AI capabilities from either Anthropic or OpenAI. The script analyzes repository content and creates comprehensive documentation that accurately reflects the project's structure and purpose.

## Installation

1. Clone the repository
2. Install required dependencies:
```bash
pip install anthropic openai
```

3. Set up environment variables:
- `ANTHROPIC_API_KEY` - Your Anthropic API key
- `OPENAI_API_KEY` - Your OpenAI API key
- `AI_MODEL` - The AI model to use

## Usage

The main script `scripts/generate_readme.py` provides the following functionality:

1. **File Type Configuration**
   - Loads file type definitions from `.github/config/file_types.json`
   - Supports custom file type patterns for repository scanning

2. **Repository Scanning**
   - Recursively scans the repository for specified file types
   - Processes and aggregates file contents for analysis

3. **AI Integration**
   - Supports both Anthropic and OpenAI APIs
   - Chunks large content to handle API token limits
   - Generates comprehensive README content based on repository analysis

To run the script:
```bash
python scripts/generate_readme.py
```

## Contributing

To contribute to this project:

1. Fork the repository
2. Create a new branch for your feature
3. Implement your changes
4. Add appropriate error handling and logging
5. Submit a pull request

When contributing, please:
- Follow the existing code style
- Add appropriate logging statements
- Handle errors gracefully
- Update documentation as needed
- Test your changes thoroughly

## Features

- Dynamic repository content scanning
- Configurable file type support
- Flexible AI provider integration (Anthropic/OpenAI)
- Robust error handling and logging
- Content chunking for large repositories

## License

[Add your license information here]I'll help you complete those configuration files and add additional ones needed. Here's a complete set of necessary files:

```yaml
# .github/workflows/main.yml
name: Generate README with AI

on:
  push:
    branches:
      - 'readme-update'
  workflow_dispatch:

jobs:
  generate-readme:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install anthropic openai python-dotenv pyyaml

      - name: Generate README
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          AI_PROVIDER: ${{ vars.AI_PROVIDER }}
          AI_MODEL: ${{ vars.AI_MODEL }}
        run: python .github/scripts/generate_readme.py

      - name: Create Pull Request
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: 'docs: update README.md'
          title: 'Update README.md'
          body: 'Auto-generated README update'
          branch: update-readme
          delete-branch: true
```

```json
// config/file_types.json
{
    "Python Files": "**/*.py",
    "Terraform Files": "**/*.tf",
    "Terraform Variables": "**/*.tfvars",
    "JavaScript Files": "**/*.js",
    "TypeScript Files": "**/*.ts",
    "YAML Files": "**/*.{yml,yaml}",
    "JSON Files": "**/*.json",
    "Markdown Files": "**/*.md",
    "Docker Files": "**/Dockerfile*",
    "Shell Scripts": "**/*.sh"
}
```

```json
// config/ai_prompts.json
{
    "readme_template": "Create a comprehensive README.md for a repository with the following sections:\n\n- Project Overview\n- Installation\n- Usage\n- Configuration\n- Contributing\n- License\n\nRepository contents:\n{content_summary}",
    
    "content_analysis": "Analyze the following repository contents and provide a brief summary:\n{file_list}",
    
    "error_handling": "Please review the following error and suggest appropriate handling:\n{error_message}"
}
```

```json
// config/settings.json
{
    "default_provider": "anthropic",
    "default_model": "claude-2",
    "backup_provider": "openai",
    "backup_model": "gpt-4",
    "max_retries": 3,
    "timeout": 30,
    "excluded_paths": [
        "node_modules",
        "venv",
        ".git",
        "__pycache__",
        "dist",
        "build"
    ],
    "output_file": "README.md",
    "log_level": "INFO"
}
```

And here's the basic structure for error handling classes:

```python
# .github/scripts/exceptions.py
class ReadmeGenerationError(Exception):
    """Base exception for README generation errors"""
    pass

class APIError(ReadmeGenerationError):
    """Raised when API calls fail"""
    pass

class ConfigurationError(ReadmeGenerationError):
    """Raised when configuration is invalid"""
    pass

class FileOperationError(ReadmeGenerationError):
    """Raised when file operations fail"""
    pass

class ContentProcessingError(ReadmeGenerationError):
    """Raised when content processing fails"""
    pass
```

These files provide:

1. A complete GitHub Actions workflow
2. Comprehensive file type definitions
3. AI prompt templates
4. Application settings
5. Custom exception classes

The configuration is modular and can be easily extended. The error handling covers all major operations:
- File operations through custom exceptions
- API interactions with retry logic
- Configuration validation
- Content processing errors

You can add more specific configurations or error handlers as needed for your use case.# Project File Structure Guide

## Overview
This repository contains various file types commonly used in software development. Below is a comprehensive list of the file extensions and their corresponding file types.

## File Types

### Development Files
- **Script Files**: `*.js`
  - JavaScript source files

- **TypeScript Files**: `*.ts`
  - TypeScript source files

- **HTML Files**: `*.html`
  - Web page markup files

- **CSS Files**: `*.css`
  - Cascading Style Sheets for styling

### Documentation
- **Markdown Files**: `*.md`
  - Documentation and README files

### Configuration Files
- **YAML Files**: `*.yml`
  - Configuration and data files

- **JSON Files**: `*.json`
  - JavaScript Object Notation data files

### System Files
- **Shell Scripts**: `*.sh`
  - Bash/Shell script files

- **Dockerfile**: `Dockerfile*`
  - Container configuration files

### Programming Languages
- **C++ Files**: `*.cpp`
  - C++ source code files

- **Java Files**: `*.java`
  - Java source code files

- **Go Files**: `*.go`
  - Go source code files

- **Ruby Files**: `*.rb`
  - Ruby source code files

### Database
- **SQL Files**: `*.sql`
  - SQL database queries and schemas

## Usage
Each file type serves a specific purpose in the development workflow. Make sure to follow the appropriate naming conventions and best practices for each file type.

## Contributing
When contributing to this project, please ensure your files are placed in the appropriate directories and follow the established naming conventions.

## License
[Include your license information here]

---
*Note: This README provides a basic structure for organizing different file types. Adjust it according to your project's specific needs.*## Technical Details

The project includes the following key components:

- `generate_readme.py`: Main script containing:
  - Environment variable management
  - File type configuration loading
  - Repository content scanning
  - Content chunking
  - AI API integration (Anthropic and OpenAI)
  - Comprehensive logging
  - Error handling

The script uses type hints and follows Python best practices for code organization and error handling.I'll analyze this Python script and the partial README.md content to provide a comprehensive explanation of how the code works.

This code is part of an AI-Powered README Generator with two main functions:

1. `get_ai_provider()`:
- Returns a callable function that will handle README generation
- Implements a fallback mechanism between Anthropic and OpenAI
- Key features:
  - Checks environment variables for the primary AI provider preference
  - Creates a fallback to an alternative provider if the primary one isn't available
  - Validates API keys for both providers
  - Returns the appropriate generation function or raises an error if no valid provider is found

2. `update_readme_section()`:
- Updates specific sections within an existing README file
- Parameters:
  - `existing_content`: Current README content
  - `new_content`: New content to be inserted
  - `section`: Section name to be updated
- Logic:
  - Locates sections using "## " markers
  - Preserves content outside the target section
  - Handles cases where sections don't exist by appending new content

3. `generate_readme()`:
- Main orchestration function that:
  - Loads file type configurations
  - Scans repository content
  - Generates prompts for AI
  - Manages README updates
  - Handles error cases and logging

Key Features of the Implementation:
- Fallback mechanism between AI providers
- Section-specific updates rather than full file replacement
- Environment variable configuration
- Comprehensive error handling and logging
- Clear separation of concerns between functions

The code shows good practices in terms of:
- Type hints
- Error handling
- Configuration management
- Modular design
- Logging implementation

The system is designed to be flexible and maintainable, with clear separation between the AI provider selection, content generation, and file management components.I'll help create a clear and organized README.md based on the repository content. Here's a streamlined version:

# AI-Powered README Generator

## Project Description
This project provides an automated solution for generating and updating README.md files using AI capabilities from either Anthropic or OpenAI. The script analyzes repository content and creates comprehensive documentation that accurately reflects the project's structure and purpose.

## Installation

1. Clone the repository
2. Install required dependencies:
```bash
pip install anthropic openai
```

3. Set up environment variables:
- `ANTHROPIC_API_KEY` - Your Anthropic API key
- `OPENAI_API_KEY` - Your OpenAI API key
- `AI_MODEL` - The AI model to use

## Usage

The main script `scripts/generate_readme.py` provides the following functionality:

1. **File Type Configuration**
   - Loads file type definitions from `.github/config/file_types.json`
   - Supports custom file type patterns for repository scanning

2. **Repository Scanning**
   - Recursively scans the repository for specified file types
   - Processes and aggregates file contents for analysis

3. **AI Integration**
   - Supports both Anthropic and OpenAI APIs
   - Chunks large content to handle API token limits
   - Generates comprehensive README content based on repository analysis

To run the script:
```bash
python scripts/generate_readme.py
```

## Contributing

To contribute to this project:

1. Fork the repository
2. Create a new branch for your feature
3. Implement your changes
4. Add appropriate error handling and logging
5. Submit a pull request

When contributing, please:
- Follow the existing code style
- Add appropriate logging statements
- Handle errors gracefully
- Update documentation as needed
- Test your changes thoroughly

## Features

- Dynamic repository content scanning
- Configurable file type support
- Flexible AI provider integration (Anthropic/OpenAI)
- Robust error handling and logging
- Content chunking for large repositories

## License

[Add your license information here]I'll help you complete those configuration files and add additional ones needed. Here's a complete set of necessary files:

```yaml
# .github/workflows/main.yml
name: Generate README with AI

on:
  push:
    branches:
      - 'readme-update'
  workflow_dispatch:

jobs:
  generate-readme:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install anthropic openai python-dotenv pyyaml

      - name: Generate README
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          AI_PROVIDER: ${{ vars.AI_PROVIDER }}
          AI_MODEL: ${{ vars.AI_MODEL }}
        run: python .github/scripts/generate_readme.py

      - name: Create Pull Request
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: 'docs: update README.md'
          title: 'Update README.md'
          body: 'Auto-generated README update'
          branch: update-readme
          delete-branch: true
```

```json
// config/file_types.json
{
    "Python Files": "**/*.py",
    "Terraform Files": "**/*.tf",
    "Terraform Variables": "**/*.tfvars",
    "JavaScript Files": "**/*.js",
    "TypeScript Files": "**/*.ts",
    "YAML Files": "**/*.{yml,yaml}",
    "JSON Files": "**/*.json",
    "Markdown Files": "**/*.md",
    "Docker Files": "**/Dockerfile*",
    "Shell Scripts": "**/*.sh"
}
```

```json
// config/ai_prompts.json
{
    "readme_template": "Create a comprehensive README.md for a repository with the following sections:\n\n- Project Overview\n- Installation\n- Usage\n- Configuration\n- Contributing\n- License\n\nRepository contents:\n{content_summary}",
    
    "content_analysis": "Analyze the following repository contents and provide a brief summary:\n{file_list}",
    
    "error_handling": "Please review the following error and suggest appropriate handling:\n{error_message}"
}
```

```json
// config/settings.json
{
    "default_provider": "anthropic",
    "default_model": "claude-2",
    "backup_provider": "openai",
    "backup_model": "gpt-4",
    "max_retries": 3,
    "timeout": 30,
    "excluded_paths": [
        "node_modules",
        "venv",
        ".git",
        "__pycache__",
        "dist",
        "build"
    ],
    "output_file": "README.md",
    "log_level": "INFO"
}
```

And here's the basic structure for error handling classes:

```python
# .github/scripts/exceptions.py
class ReadmeGenerationError(Exception):
    """Base exception for README generation errors"""
    pass

class APIError(ReadmeGenerationError):
    """Raised when API calls fail"""
    pass

class ConfigurationError(ReadmeGenerationError):
    """Raised when configuration is invalid"""
    pass

class FileOperationError(ReadmeGenerationError):
    """Raised when file operations fail"""
    pass

class ContentProcessingError(ReadmeGenerationError):
    """Raised when content processing fails"""
    pass
```

These files provide:

1. A complete GitHub Actions workflow
2. Comprehensive file type definitions
3. AI prompt templates
4. Application settings
5. Custom exception classes

The configuration is modular and can be easily extended. The error handling covers all major operations:
- File operations through custom exceptions
- API interactions with retry logic
- Configuration validation
- Content processing errors

You can add more specific configurations or error handlers as needed for your use case.# Project File Structure Guide

## Overview
This repository contains various file types commonly used in software development. Below is a comprehensive list of the file extensions and their corresponding file types.

## File Types

### Development Files
- **Script Files**: `*.js`
  - JavaScript source files

- **TypeScript Files**: `*.ts`
  - TypeScript source files

- **HTML Files**: `*.html`
  - Web page markup files

- **CSS Files**: `*.css`
  - Cascading Style Sheets for styling

### Documentation
- **Markdown Files**: `*.md`
  - Documentation and README files

### Configuration Files
- **YAML Files**: `*.yml`
  - Configuration and data files

- **JSON Files**: `*.json`
  - JavaScript Object Notation data files

### System Files
- **Shell Scripts**: `*.sh`
  - Bash/Shell script files

- **Dockerfile**: `Dockerfile*`
  - Container configuration files

### Programming Languages
- **C++ Files**: `*.cpp`
  - C++ source code files

- **Java Files**: `*.java`
  - Java source code files

- **Go Files**: `*.go`
  - Go source code files

- **Ruby Files**: `*.rb`
  - Ruby source code files

### Database
- **SQL Files**: `*.sql`
  - SQL database queries and schemas

## Usage
Each file type serves a specific purpose in the development workflow. Make sure to follow the appropriate naming conventions and best practices for each file type.

## Contributing
When contributing to this project, please ensure your files are placed in the appropriate directories and follow the established naming conventions.

## License
[Include your license information here]

---
*Note: This README provides a basic structure for organizing different file types. Adjust it according to your project's specific needs.*## Contributing

To contribute to this project:

1. Fork the repository
2. Create a feature branch
3. Make your changes, ensuring to:
   - Follow the existing code style
   - Add appropriate error handling
   - Include logging statements
   - Update documentation as needed
4. Submit a pull request

Please make sure to:
- Test your changes thoroughly
- Update any relevant documentation
- Add appropriate logging statements for new functionality
- Follow existing error handling patterns

## Technical Details

The project includes the following key components:

- `generate_readme.py`: Main script containing:
  - Environment variable management
  - File type configuration loading
  - Repository content scanning
  - Content chunking
  - AI API integration (Anthropic and OpenAI)
  - Comprehensive logging
  - Error handling

The script uses type hints and follows Python best practices for code organization and error handling.I'll analyze this Python script and the partial README.md content to provide a comprehensive explanation of how the code works.

This code is part of an AI-Powered README Generator with two main functions:

1. `get_ai_provider()`:
- Returns a callable function that will handle README generation
- Implements a fallback mechanism between Anthropic and OpenAI
- Key features:
  - Checks environment variables for the primary AI provider preference
  - Creates a fallback to an alternative provider if the primary one isn't available
  - Validates API keys for both providers
  - Returns the appropriate generation function or raises an error if no valid provider is found

2. `update_readme_section()`:
- Updates specific sections within an existing README file
- Parameters:
  - `existing_content`: Current README content
  - `new_content`: New content to be inserted
  - `section`: Section name to be updated
- Logic:
  - Locates sections using "## " markers
  - Preserves content outside the target section
  - Handles cases where sections don't exist by appending new content

3. `generate_readme()`:
- Main orchestration function that:
  - Loads file type configurations
  - Scans repository content
  - Generates prompts for AI
  - Manages README updates
  - Handles error cases and logging

Key Features of the Implementation:
- Fallback mechanism between AI providers
- Section-specific updates rather than full file replacement
- Environment variable configuration
- Comprehensive error handling and logging
- Clear separation of concerns between functions

The code shows good practices in terms of:
- Type hints
- Error handling
- Configuration management
- Modular design
- Logging implementation

The system is designed to be flexible and maintainable, with clear separation between the AI provider selection, content generation, and file management components.I'll help create a clear and organized README.md based on the repository content. Here's a streamlined version:

# AI-Powered README Generator

## Project Description
This project provides an automated solution for generating and updating README.md files using AI capabilities from either Anthropic or OpenAI. The script analyzes repository content and creates comprehensive documentation that accurately reflects the project's structure and purpose.

## Installation

1. Clone the repository
2. Install required dependencies:
```bash
pip install anthropic openai
```

3. Set up environment variables:
- `ANTHROPIC_API_KEY` - Your Anthropic API key
- `OPENAI_API_KEY` - Your OpenAI API key
- `AI_MODEL` - The AI model to use

## Usage

The main script `scripts/generate_readme.py` provides the following functionality:

1. **File Type Configuration**
   - Loads file type definitions from `.github/config/file_types.json`
   - Supports custom file type patterns for repository scanning

2. **Repository Scanning**
   - Recursively scans the repository for specified file types
   - Processes and aggregates file contents for analysis

3. **AI Integration**
   - Supports both Anthropic and OpenAI APIs
   - Chunks large content to handle API token limits
   - Generates comprehensive README content based on repository analysis

To run the script:
```bash
python scripts/generate_readme.py
```

## Contributing

To contribute to this project:

1. Fork the repository
2. Create a new branch for your feature
3. Implement your changes
4. Add appropriate error handling and logging
5. Submit a pull request

When contributing, please:
- Follow the existing code style
- Add appropriate logging statements
- Handle errors gracefully
- Update documentation as needed
- Test your changes thoroughly

## Features

- Dynamic repository content scanning
- Configurable file type support
- Flexible AI provider integration (Anthropic/OpenAI)
- Robust error handling and logging
- Content chunking for large repositories

## License

[Add your license information here]I'll help you complete those configuration files and add additional ones needed. Here's a complete set of necessary files:

```yaml
# .github/workflows/main.yml
name: Generate README with AI

on:
  push:
    branches:
      - 'readme-update'
  workflow_dispatch:

jobs:
  generate-readme:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install anthropic openai python-dotenv pyyaml

      - name: Generate README
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          AI_PROVIDER: ${{ vars.AI_PROVIDER }}
          AI_MODEL: ${{ vars.AI_MODEL }}
        run: python .github/scripts/generate_readme.py

      - name: Create Pull Request
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: 'docs: update README.md'
          title: 'Update README.md'
          body: 'Auto-generated README update'
          branch: update-readme
          delete-branch: true
```

```json
// config/file_types.json
{
    "Python Files": "**/*.py",
    "Terraform Files": "**/*.tf",
    "Terraform Variables": "**/*.tfvars",
    "JavaScript Files": "**/*.js",
    "TypeScript Files": "**/*.ts",
    "YAML Files": "**/*.{yml,yaml}",
    "JSON Files": "**/*.json",
    "Markdown Files": "**/*.md",
    "Docker Files": "**/Dockerfile*",
    "Shell Scripts": "**/*.sh"
}
```

```json
// config/ai_prompts.json
{
    "readme_template": "Create a comprehensive README.md for a repository with the following sections:\n\n- Project Overview\n- Installation\n- Usage\n- Configuration\n- Contributing\n- License\n\nRepository contents:\n{content_summary}",
    
    "content_analysis": "Analyze the following repository contents and provide a brief summary:\n{file_list}",
    
    "error_handling": "Please review the following error and suggest appropriate handling:\n{error_message}"
}
```

```json
// config/settings.json
{
    "default_provider": "anthropic",
    "default_model": "claude-2",
    "backup_provider": "openai",
    "backup_model": "gpt-4",
    "max_retries": 3,
    "timeout": 30,
    "excluded_paths": [
        "node_modules",
        "venv",
        ".git",
        "__pycache__",
        "dist",
        "build"
    ],
    "output_file": "README.md",
    "log_level": "INFO"
}
```

And here's the basic structure for error handling classes:

```python
# .github/scripts/exceptions.py
class ReadmeGenerationError(Exception):
    """Base exception for README generation errors"""
    pass

class APIError(ReadmeGenerationError):
    """Raised when API calls fail"""
    pass

class ConfigurationError(ReadmeGenerationError):
    """Raised when configuration is invalid"""
    pass

class FileOperationError(ReadmeGenerationError):
    """Raised when file operations fail"""
    pass

class ContentProcessingError(ReadmeGenerationError):
    """Raised when content processing fails"""
    pass
```

These files provide:

1. A complete GitHub Actions workflow
2. Comprehensive file type definitions
3. AI prompt templates
4. Application settings
5. Custom exception classes

The configuration is modular and can be easily extended. The error handling covers all major operations:
- File operations through custom exceptions
- API interactions with retry logic
- Configuration validation
- Content processing errors

You can add more specific configurations or error handlers as needed for your use case.# Project File Structure Guide

## Overview
This repository contains various file types commonly used in software development. Below is a comprehensive list of the file extensions and their corresponding file types.

## File Types

### Development Files
- **Script Files**: `*.js`
  - JavaScript source files

- **TypeScript Files**: `*.ts`
  - TypeScript source files

- **HTML Files**: `*.html`
  - Web page markup files

- **CSS Files**: `*.css`
  - Cascading Style Sheets for styling

### Documentation
- **Markdown Files**: `*.md`
  - Documentation and README files

### Configuration Files
- **YAML Files**: `*.yml`
  - Configuration and data files

- **JSON Files**: `*.json`
  - JavaScript Object Notation data files

### System Files
- **Shell Scripts**: `*.sh`
  - Bash/Shell script files

- **Dockerfile**: `Dockerfile*`
  - Container configuration files

### Programming Languages
- **C++ Files**: `*.cpp`
  - C++ source code files

- **Java Files**: `*.java`
  - Java source code files

- **Go Files**: `*.go`
  - Go source code files

- **Ruby Files**: `*.rb`
  - Ruby source code files

### Database
- **SQL Files**: `*.sql`
  - SQL database queries and schemas

## Usage
Each file type serves a specific purpose in the development workflow. Make sure to follow the appropriate naming conventions and best practices for each file type.

## Contributing
When contributing to this project, please ensure your files are placed in the appropriate directories and follow the established naming conventions.

## License
[Include your license information here]

---
*Note: This README provides a basic structure for organizing different file types. Adjust it according to your project's specific needs.*## Usage

The main script (`scripts/generate_readme.py`) provides several key functions:

1. **File Type Configuration**
   - Define file types to scan in `.github/config/file_types.json`
   - The script will automatically detect and process files matching the configured patterns

2. **Content Processing**
   - Scans repository for specified file types
   - Reads and processes file contents
   - Chunks large content for optimal API processing

3. **README Generation**
   - Supports both Anthropic and OpenAI APIs
   - Generates structured documentation based on repository content
   - Includes error handling and logging for reliable operation

Example usage:
```python
python scripts/generate_readme.py
```

## Contributing

To contribute to this project:

1. Fork the repository
2. Create a feature branch
3. Make your changes, ensuring to:
   - Follow the existing code style
   - Add appropriate error handling
   - Include logging statements
   - Update documentation as needed
4. Submit a pull request

Please make sure to:
- Test your changes thoroughly
- Update any relevant documentation
- Add appropriate logging statements for new functionality
- Follow existing error handling patterns

## Technical Details

The project includes the following key components:

- `generate_readme.py`: Main script containing:
  - Environment variable management
  - File type configuration loading
  - Repository content scanning
  - Content chunking
  - AI API integration (Anthropic and OpenAI)
  - Comprehensive logging
  - Error handling

The script uses type hints and follows Python best practices for code organization and error handling.I'll analyze this Python script and the partial README.md content to provide a comprehensive explanation of how the code works.

This code is part of an AI-Powered README Generator with two main functions:

1. `get_ai_provider()`:
- Returns a callable function that will handle README generation
- Implements a fallback mechanism between Anthropic and OpenAI
- Key features:
  - Checks environment variables for the primary AI provider preference
  - Creates a fallback to an alternative provider if the primary one isn't available
  - Validates API keys for both providers
  - Returns the appropriate generation function or raises an error if no valid provider is found

2. `update_readme_section()`:
- Updates specific sections within an existing README file
- Parameters:
  - `existing_content`: Current README content
  - `new_content`: New content to be inserted
  - `section`: Section name to be updated
- Logic:
  - Locates sections using "## " markers
  - Preserves content outside the target section
  - Handles cases where sections don't exist by appending new content

3. `generate_readme()`:
- Main orchestration function that:
  - Loads file type configurations
  - Scans repository content
  - Generates prompts for AI
  - Manages README updates
  - Handles error cases and logging

Key Features of the Implementation:
- Fallback mechanism between AI providers
- Section-specific updates rather than full file replacement
- Environment variable configuration
- Comprehensive error handling and logging
- Clear separation of concerns between functions

The code shows good practices in terms of:
- Type hints
- Error handling
- Configuration management
- Modular design
- Logging implementation

The system is designed to be flexible and maintainable, with clear separation between the AI provider selection, content generation, and file management components.I'll help create a clear and organized README.md based on the repository content. Here's a streamlined version:

# AI-Powered README Generator

## Project Description
This project provides an automated solution for generating and updating README.md files using AI capabilities from either Anthropic or OpenAI. The script analyzes repository content and creates comprehensive documentation that accurately reflects the project's structure and purpose.

## Installation

1. Clone the repository
2. Install required dependencies:
```bash
pip install anthropic openai
```

3. Set up environment variables:
- `ANTHROPIC_API_KEY` - Your Anthropic API key
- `OPENAI_API_KEY` - Your OpenAI API key
- `AI_MODEL` - The AI model to use

## Usage

The main script `scripts/generate_readme.py` provides the following functionality:

1. **File Type Configuration**
   - Loads file type definitions from `.github/config/file_types.json`
   - Supports custom file type patterns for repository scanning

2. **Repository Scanning**
   - Recursively scans the repository for specified file types
   - Processes and aggregates file contents for analysis

3. **AI Integration**
   - Supports both Anthropic and OpenAI APIs
   - Chunks large content to handle API token limits
   - Generates comprehensive README content based on repository analysis

To run the script:
```bash
python scripts/generate_readme.py
```

## Contributing

To contribute to this project:

1. Fork the repository
2. Create a new branch for your feature
3. Implement your changes
4. Add appropriate error handling and logging
5. Submit a pull request

When contributing, please:
- Follow the existing code style
- Add appropriate logging statements
- Handle errors gracefully
- Update documentation as needed
- Test your changes thoroughly

## Features

- Dynamic repository content scanning
- Configurable file type support
- Flexible AI provider integration (Anthropic/OpenAI)
- Robust error handling and logging
- Content chunking for large repositories

## License

[Add your license information here]I'll help you complete those configuration files and add additional ones needed. Here's a complete set of necessary files:

```yaml
# .github/workflows/main.yml
name: Generate README with AI

on:
  push:
    branches:
      - 'readme-update'
  workflow_dispatch:

jobs:
  generate-readme:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install anthropic openai python-dotenv pyyaml

      - name: Generate README
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          AI_PROVIDER: ${{ vars.AI_PROVIDER }}
          AI_MODEL: ${{ vars.AI_MODEL }}
        run: python .github/scripts/generate_readme.py

      - name: Create Pull Request
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: 'docs: update README.md'
          title: 'Update README.md'
          body: 'Auto-generated README update'
          branch: update-readme
          delete-branch: true
```

```json
// config/file_types.json
{
    "Python Files": "**/*.py",
    "Terraform Files": "**/*.tf",
    "Terraform Variables": "**/*.tfvars",
    "JavaScript Files": "**/*.js",
    "TypeScript Files": "**/*.ts",
    "YAML Files": "**/*.{yml,yaml}",
    "JSON Files": "**/*.json",
    "Markdown Files": "**/*.md",
    "Docker Files": "**/Dockerfile*",
    "Shell Scripts": "**/*.sh"
}
```

```json
// config/ai_prompts.json
{
    "readme_template": "Create a comprehensive README.md for a repository with the following sections:\n\n- Project Overview\n- Installation\n- Usage\n- Configuration\n- Contributing\n- License\n\nRepository contents:\n{content_summary}",
    
    "content_analysis": "Analyze the following repository contents and provide a brief summary:\n{file_list}",
    
    "error_handling": "Please review the following error and suggest appropriate handling:\n{error_message}"
}
```

```json
// config/settings.json
{
    "default_provider": "anthropic",
    "default_model": "claude-2",
    "backup_provider": "openai",
    "backup_model": "gpt-4",
    "max_retries": 3,
    "timeout": 30,
    "excluded_paths": [
        "node_modules",
        "venv",
        ".git",
        "__pycache__",
        "dist",
        "build"
    ],
    "output_file": "README.md",
    "log_level": "INFO"
}
```

And here's the basic structure for error handling classes:

```python
# .github/scripts/exceptions.py
class ReadmeGenerationError(Exception):
    """Base exception for README generation errors"""
    pass

class APIError(ReadmeGenerationError):
    """Raised when API calls fail"""
    pass

class ConfigurationError(ReadmeGenerationError):
    """Raised when configuration is invalid"""
    pass

class FileOperationError(ReadmeGenerationError):
    """Raised when file operations fail"""
    pass

class ContentProcessingError(ReadmeGenerationError):
    """Raised when content processing fails"""
    pass
```

These files provide:

1. A complete GitHub Actions workflow
2. Comprehensive file type definitions
3. AI prompt templates
4. Application settings
5. Custom exception classes

The configuration is modular and can be easily extended. The error handling covers all major operations:
- File operations through custom exceptions
- API interactions with retry logic
- Configuration validation
- Content processing errors

You can add more specific configurations or error handlers as needed for your use case.# Project File Structure Guide

## Overview
This repository contains various file types commonly used in software development. Below is a comprehensive list of the file extensions and their corresponding file types.

## File Types

### Development Files
- **Script Files**: `*.js`
  - JavaScript source files

- **TypeScript Files**: `*.ts`
  - TypeScript source files

- **HTML Files**: `*.html`
  - Web page markup files

- **CSS Files**: `*.css`
  - Cascading Style Sheets for styling

### Documentation
- **Markdown Files**: `*.md`
  - Documentation and README files

### Configuration Files
- **YAML Files**: `*.yml`
  - Configuration and data files

- **JSON Files**: `*.json`
  - JavaScript Object Notation data files

### System Files
- **Shell Scripts**: `*.sh`
  - Bash/Shell script files

- **Dockerfile**: `Dockerfile*`
  - Container configuration files

### Programming Languages
- **C++ Files**: `*.cpp`
  - C++ source code files

- **Java Files**: `*.java`
  - Java source code files

- **Go Files**: `*.go`
  - Go source code files

- **Ruby Files**: `*.rb`
  - Ruby source code files

### Database
- **SQL Files**: `*.sql`
  - SQL database queries and schemas

## Usage
Each file type serves a specific purpose in the development workflow. Make sure to follow the appropriate naming conventions and best practices for each file type.

## Contributing
When contributing to this project, please ensure your files are placed in the appropriate directories and follow the established naming conventions.

## License
[Include your license information here]

---
*Note: This README provides a basic structure for organizing different file types. Adjust it according to your project's specific needs.*## Project Description
This project provides an automated solution for generating and updating README.md files using AI capabilities from either Anthropic or OpenAI. The script analyzes repository content and creates comprehensive documentation that accurately reflects the project's structure and purpose.

## Installation

1. Clone the repository
2. Install required dependencies:
```bash
pip install anthropic openai
```

3. Set up environment variables:
- `ANTHROPIC_API_KEY` - Your Anthropic API key
- `OPENAI_API_KEY` - Your OpenAI API key
- `AI_MODEL` - The AI model to use

Here's the generated README.md based on the repository content:

# AI-Powered README Generator

## Project Description
This project provides an automated solution for generating and updating README.md files using AI capabilities from either Anthropic or OpenAI. The script analyzes repository content and creates comprehensive documentation that accurately reflects the project's structure and purpose.

## Installation

1. Clone the repository
2. Install required dependencies:
```bash
pip install anthropic openai
```

3. Set up environment variables:
- `ANTHROPIC_API_KEY` - Your Anthropic API key
- `OPENAI_API_KEY` - Your OpenAI API key
- `AI_MODEL` - The AI model to use

## Usage

The main script `scripts/generate_readme.py` provides the following functionality:

1. **File Type Configuration**
   - Loads file type definitions from `.github/config/file_types.json`
   - Supports custom file type patterns for repository scanning

2. **Repository Scanning**
   - Recursively scans the repository for specified file types
   - Processes and aggregates file contents for analysis

3. **AI Integration**
   - Supports both Anthropic and OpenAI APIs
   - Chunks large content to handle API token limits
   - Generates comprehensive README content based on repository analysis

To run the script:
```bash
python scripts/generate_readme.py
```

Here's the generated README.md based on the repository content:

# AI-Powered README Generator

## Project Description
This project provides an automated solution for generating and updating README.md files using AI capabilities from either Anthropic or OpenAI. The script analyzes repository content and creates comprehensive documentation that accurately reflects the project's structure and purpose.

## Installation

1. Clone the repository
2. Install required dependencies:
```bash
pip install anthropic openai
```

3. Set up environment variables:
- `ANTHROPIC_API_KEY` - Your Anthropic API key
- `OPENAI_API_KEY` - Your OpenAI API key
- `AI_MODEL` - The AI model to use

## Usage

The main script `scripts/generate_readme.py` provides the following functionality:

1. **File Type Configuration**
   - Loads file type definitions from `.github/config/file_types.json`
   - Supports custom file type patterns for repository scanning

2. **Repository Scanning**
   - Recursively scans the repository for specified file types
   - Processes and aggregates file contents for analysis

3. **AI Integration**
   - Supports both Anthropic and OpenAI APIs
   - Chunks large content to handle API token limits
   - Generates comprehensive README content based on repository analysis

To run the script:
```bash
python scripts/generate_readme.py
```

## Contributing

To contribute to this project:

1. Fork the repository
2. Create a new branch for your feature
3. Implement your changes
4. Add appropriate error handling and logging
5. Submit a pull request

When contributing, please:
- Follow the existing code style
- Add appropriate logging statements
- Handle errors gracefully
- Update documentation as needed
- Test your changes thoroughly

## Features

- Dynamic repository content scanning
- Configurable file type support
- Flexible AI provider integration (Anthropic/OpenAI)
- Robust error handling and logging
- Content chunking for large repositories

## Error Handling

The script includes comprehensive error handling for:
- File operations
- API interactions
- Environment variable configuration
- JSON parsing
- Content processing

## Dependencies

- `anthropic`: For Anthropic API integration
- `openai`: For OpenAI API integration
- Standard Python libraries: `os`, `sys`, `glob`, `json`, `logging`, `typing`I'll help you complete the GitHub Actions workflow YAML file for generating README with AI. Here's the continuation of the `main.yml` file:

```yaml
name: Generate README with AI

on:
  push:
    branches:
      - 'readme-update'
  workflow_dispatch:

jobs:
  generate-readme:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install anthropic openai python-dotenv

      - name: Generate README
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          AI_PROVIDER: ${{ secrets.AI_PROVIDER }}
          AI_MODEL: ${{ secrets.AI_MODEL }}
        run: python generate_readme.py

      - name: Check if README was generated
        id: check_readme
        run: |
          output=$(python generate_readme.py)
          echo "README_GENERATED=$(echo "$output" | grep "readme_generated=" | cut -d'=' -f2)" >> $GITHUB_OUTPUT

      - name: Create Pull Request
        if: steps.check_readme.outputs.README_GENERATED == 'true'
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: 'docs: update README.md with AI-generated content'
          title: 'Update README.md'
          body: |
            This PR updates the README.md file with AI-generated content.
            
            Changes made:
            - Updated Project Description
            - Updated Installation section
            - Updated Usage section
            - Updated Contributing section
          branch: update-readme
          base: main
          delete-branch: true

      - name: Handle README Generation Failure
        if: steps.check_readme.outputs.README_GENERATED != 'true'
        run: |
          echo "README generation failed"
          exit 1
```

This README.md provides a comprehensive overview of the repository's functionality, supported file types, and automation features while maintaining a clean and professional format. It can be automatically updated as new file types are added or configurations change.