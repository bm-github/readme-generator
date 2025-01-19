

Here's the generated README.md based on the repository content:

# AI-Powered README Generator

## Project Description
This project provides an automated solution for generating and updating README.md files using AI capabilities from either Anthropic or OpenAI. The script analyzes repository content and creates comprehensive documentation that accurately reflects the project's structure and purpose.

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

This workflow:

1. Runs on pushes to the 'readme-update' branch or manual triggers
2. Sets up Python 3.10
3. Installs required dependencies (anthropic and openai packages)
4. Runs the README generation script with necessary environment variables
5. Checks if the README was generated successfully
6. Creates a pull request if the README was generated successfully
7. Includes error handling for failed README generation

To use this workflow:

1. Store your API keys and preferences as repository secrets:
   - `ANTHROPIC_API_KEY`
   - `OPENAI_API_KEY`
   - `AI_PROVIDER` (either 'anthropic' or 'openai')
   - `AI_MODEL` (e.g., 'gpt-4' or 'claude-2')

2. The workflow will create a pull request with the updated README when:
   - You push to the 'readme-update' branch
   - You manually trigger the workflow
   - The README generation is successful

3. If the README generation fails, the workflow will fail with an error message.

The pull request will include a helpful description of the changes made to the README file and will automatically clean up the temporary branch after merging.Here's a generated README.md content based on the provided context:

```markdown
# Repository File Analysis Tool

This repository contains an automated system for analyzing and documenting code files across multiple programming languages and file types.

## Supported File Types

The tool supports analysis of the following file types:

- Python (*.py)
- Terraform (*.tf, *.tfvars) 
- JavaScript (*.js)
- TypeScript (*.ts)
- HTML (*.html)
- CSS (*.css)
- Markdown (*.md)
- YAML (*.yml)
- JSON (*.json)
- Shell Scripts (*.sh)
- Dockerfiles
- C++ (*.cpp)
- Java (*.java)
- Go (*.go)
- Ruby (*.rb)
- SQL (*.sql)

## Automation Features

This repository includes GitHub Actions workflows that:

1. Automatically scan and analyze repository contents
2. Generate updated documentation
3. Create automated commits with changes
4. Push updates to a dedicated branch (readme-update)

## Configuration

The system uses environment variables for AI provider configuration:
- `ANTHROPIC_API_KEY`: For Anthropic Claude integration
- `OPENAI_API_KEY`: For OpenAI integration
- `AI_PROVIDER`: Configurable AI provider selection
- `AI_MODEL`: Specific AI model to use

## File Type Patterns

File type patterns are configured in `config/file_types.json` which defines the glob patterns used to identify different file types during analysis.

## Usage

The README is automatically generated and updated through GitHub Actions. Manual updates to the documentation can be triggered by:

1. Pushing changes to the repository
2. Running the GitHub Action workflow manually

## Contributing

To contribute to this project:

1. Fork the repository
2. Create your feature branch
3. Update the relevant configuration files if adding new file types
4. Submit a pull request

## License

This project is open source and available under the MIT License.

---
*This README is automatically generated and updated through GitHub Actions*
```

This README.md provides a comprehensive overview of the repository's functionality, supported file types, and automation features while maintaining a clean and professional format. It can be automatically updated as new file types are added or configurations change.## Features

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

This workflow:

1. Runs on pushes to the 'readme-update' branch or manual triggers
2. Sets up Python 3.10
3. Installs required dependencies (anthropic and openai packages)
4. Runs the README generation script with necessary environment variables
5. Checks if the README was generated successfully
6. Creates a pull request if the README was generated successfully
7. Includes error handling for failed README generation

To use this workflow:

1. Store your API keys and preferences as repository secrets:
   - `ANTHROPIC_API_KEY`
   - `OPENAI_API_KEY`
   - `AI_PROVIDER` (either 'anthropic' or 'openai')
   - `AI_MODEL` (e.g., 'gpt-4' or 'claude-2')

2. The workflow will create a pull request with the updated README when:
   - You push to the 'readme-update' branch
   - You manually trigger the workflow
   - The README generation is successful

3. If the README generation fails, the workflow will fail with an error message.

The pull request will include a helpful description of the changes made to the README file and will automatically clean up the temporary branch after merging.Here's a generated README.md content based on the provided context:

```markdown
# Repository File Analysis Tool

This repository contains an automated system for analyzing and documenting code files across multiple programming languages and file types.

## Supported File Types

The tool supports analysis of the following file types:

- Python (*.py)
- Terraform (*.tf, *.tfvars) 
- JavaScript (*.js)
- TypeScript (*.ts)
- HTML (*.html)
- CSS (*.css)
- Markdown (*.md)
- YAML (*.yml)
- JSON (*.json)
- Shell Scripts (*.sh)
- Dockerfiles
- C++ (*.cpp)
- Java (*.java)
- Go (*.go)
- Ruby (*.rb)
- SQL (*.sql)

## Automation Features

This repository includes GitHub Actions workflows that:

1. Automatically scan and analyze repository contents
2. Generate updated documentation
3. Create automated commits with changes
4. Push updates to a dedicated branch (readme-update)

## Configuration

The system uses environment variables for AI provider configuration:
- `ANTHROPIC_API_KEY`: For Anthropic Claude integration
- `OPENAI_API_KEY`: For OpenAI integration
- `AI_PROVIDER`: Configurable AI provider selection
- `AI_MODEL`: Specific AI model to use

## File Type Patterns

File type patterns are configured in `config/file_types.json` which defines the glob patterns used to identify different file types during analysis.

## Usage

The README is automatically generated and updated through GitHub Actions. Manual updates to the documentation can be triggered by:

1. Pushing changes to the repository
2. Running the GitHub Action workflow manually

## Contributing

To contribute to this project:

1. Fork the repository
2. Create your feature branch
3. Update the relevant configuration files if adding new file types
4. Submit a pull request

## License

This project is open source and available under the MIT License.

---
*This README is automatically generated and updated through GitHub Actions*
```

This README.md provides a comprehensive overview of the repository's functionality, supported file types, and automation features while maintaining a clean and professional format. It can be automatically updated as new file types are added or configurations change.## Contributing

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

This workflow:

1. Runs on pushes to the 'readme-update' branch or manual triggers
2. Sets up Python 3.10
3. Installs required dependencies (anthropic and openai packages)
4. Runs the README generation script with necessary environment variables
5. Checks if the README was generated successfully
6. Creates a pull request if the README was generated successfully
7. Includes error handling for failed README generation

To use this workflow:

1. Store your API keys and preferences as repository secrets:
   - `ANTHROPIC_API_KEY`
   - `OPENAI_API_KEY`
   - `AI_PROVIDER` (either 'anthropic' or 'openai')
   - `AI_MODEL` (e.g., 'gpt-4' or 'claude-2')

2. The workflow will create a pull request with the updated README when:
   - You push to the 'readme-update' branch
   - You manually trigger the workflow
   - The README generation is successful

3. If the README generation fails, the workflow will fail with an error message.

The pull request will include a helpful description of the changes made to the README file and will automatically clean up the temporary branch after merging.Here's a generated README.md content based on the provided context:

```markdown
# Repository File Analysis Tool

This repository contains an automated system for analyzing and documenting code files across multiple programming languages and file types.

## Supported File Types

The tool supports analysis of the following file types:

- Python (*.py)
- Terraform (*.tf, *.tfvars) 
- JavaScript (*.js)
- TypeScript (*.ts)
- HTML (*.html)
- CSS (*.css)
- Markdown (*.md)
- YAML (*.yml)
- JSON (*.json)
- Shell Scripts (*.sh)
- Dockerfiles
- C++ (*.cpp)
- Java (*.java)
- Go (*.go)
- Ruby (*.rb)
- SQL (*.sql)

## Automation Features

This repository includes GitHub Actions workflows that:

1. Automatically scan and analyze repository contents
2. Generate updated documentation
3. Create automated commits with changes
4. Push updates to a dedicated branch (readme-update)

## Configuration

The system uses environment variables for AI provider configuration:
- `ANTHROPIC_API_KEY`: For Anthropic Claude integration
- `OPENAI_API_KEY`: For OpenAI integration
- `AI_PROVIDER`: Configurable AI provider selection
- `AI_MODEL`: Specific AI model to use

## File Type Patterns

File type patterns are configured in `config/file_types.json` which defines the glob patterns used to identify different file types during analysis.

## Usage

The README is automatically generated and updated through GitHub Actions. Manual updates to the documentation can be triggered by:

1. Pushing changes to the repository
2. Running the GitHub Action workflow manually

## Contributing

To contribute to this project:

1. Fork the repository
2. Create your feature branch
3. Update the relevant configuration files if adding new file types
4. Submit a pull request

## License

This project is open source and available under the MIT License.

---
*This README is automatically generated and updated through GitHub Actions*
```

This README.md provides a comprehensive overview of the repository's functionality, supported file types, and automation features while maintaining a clean and professional format. It can be automatically updated as new file types are added or configurations change.## Usage

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

This workflow:

1. Runs on pushes to the 'readme-update' branch or manual triggers
2. Sets up Python 3.10
3. Installs required dependencies (anthropic and openai packages)
4. Runs the README generation script with necessary environment variables
5. Checks if the README was generated successfully
6. Creates a pull request if the README was generated successfully
7. Includes error handling for failed README generation

To use this workflow:

1. Store your API keys and preferences as repository secrets:
   - `ANTHROPIC_API_KEY`
   - `OPENAI_API_KEY`
   - `AI_PROVIDER` (either 'anthropic' or 'openai')
   - `AI_MODEL` (e.g., 'gpt-4' or 'claude-2')

2. The workflow will create a pull request with the updated README when:
   - You push to the 'readme-update' branch
   - You manually trigger the workflow
   - The README generation is successful

3. If the README generation fails, the workflow will fail with an error message.

The pull request will include a helpful description of the changes made to the README file and will automatically clean up the temporary branch after merging.Here's a generated README.md content based on the provided context:

```markdown
# Repository File Analysis Tool

This repository contains an automated system for analyzing and documenting code files across multiple programming languages and file types.

## Supported File Types

The tool supports analysis of the following file types:

- Python (*.py)
- Terraform (*.tf, *.tfvars) 
- JavaScript (*.js)
- TypeScript (*.ts)
- HTML (*.html)
- CSS (*.css)
- Markdown (*.md)
- YAML (*.yml)
- JSON (*.json)
- Shell Scripts (*.sh)
- Dockerfiles
- C++ (*.cpp)
- Java (*.java)
- Go (*.go)
- Ruby (*.rb)
- SQL (*.sql)

## Automation Features

This repository includes GitHub Actions workflows that:

1. Automatically scan and analyze repository contents
2. Generate updated documentation
3. Create automated commits with changes
4. Push updates to a dedicated branch (readme-update)

## Configuration

The system uses environment variables for AI provider configuration:
- `ANTHROPIC_API_KEY`: For Anthropic Claude integration
- `OPENAI_API_KEY`: For OpenAI integration
- `AI_PROVIDER`: Configurable AI provider selection
- `AI_MODEL`: Specific AI model to use

## File Type Patterns

File type patterns are configured in `config/file_types.json` which defines the glob patterns used to identify different file types during analysis.

## Usage

The README is automatically generated and updated through GitHub Actions. Manual updates to the documentation can be triggered by:

1. Pushing changes to the repository
2. Running the GitHub Action workflow manually

## Contributing

To contribute to this project:

1. Fork the repository
2. Create your feature branch
3. Update the relevant configuration files if adding new file types
4. Submit a pull request

## License

This project is open source and available under the MIT License.

---
*This README is automatically generated and updated through GitHub Actions*
```

This README.md provides a comprehensive overview of the repository's functionality, supported file types, and automation features while maintaining a clean and professional format. It can be automatically updated as new file types are added or configurations change.