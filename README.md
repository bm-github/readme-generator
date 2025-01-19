

Based on the repository content, I'll generate a README.md file that accurately reflects the purpose and functionality of the provided files.

# README.md

## Project Description
This project provides a sophisticated README generator that automatically creates and updates README.md files based on repository content. It uses AI services (Anthropic and OpenAI) to generate comprehensive documentation by analyzing the files in your repository.

Based on the repository content, I'll generate a README.md file that accurately reflects the purpose and functionality of the provided files.

# README.md

## Project Description
This project provides a sophisticated README generator that automatically creates and updates README.md files based on repository content. It uses AI services (Anthropic and OpenAI) to generate comprehensive documentation by analyzing the files in your repository.

## Installation

### Prerequisites
- Python 3.x
- Required Python packages:
  - anthropic
  - openai
  - typing
  - logging

### Setup
1. Clone the repository
2. Install dependencies:
```bash
pip install anthropic openai
```
3. Set up environment variables:
   - `ANTHROPIC_API_KEY`: Your Anthropic API key
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `AI_MODEL`: The AI model to use for generation

Based on the repository content, I'll generate a README.md file that accurately reflects the purpose and functionality of the provided files.

# README.md

## Project Description
This project provides a sophisticated README generator that automatically creates and updates README.md files based on repository content. It uses AI services (Anthropic and OpenAI) to generate comprehensive documentation by analyzing the files in your repository.

## Installation

### Prerequisites
- Python 3.x
- Required Python packages:
  - anthropic
  - openai
  - typing
  - logging

### Setup
1. Clone the repository
2. Install dependencies:
```bash
pip install anthropic openai
```
3. Set up environment variables:
   - `ANTHROPIC_API_KEY`: Your Anthropic API key
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `AI_MODEL`: The AI model to use for generation

## Usage

### Generate README
The main script `scripts/generate_readme.py` provides the following functionality:

1. **File Type Configuration**
   - Define file types to scan in `.github/config/file_types.json`
   - The script will automatically scan for files matching the specified patterns

2. **Content Analysis**
   - Scans repository for specified file types
   - Reads and processes file contents
   - Chunks large content for API processing

3. **README Generation**
   - Supports both Anthropic and OpenAI APIs
   - Generates structured documentation
   - Handles large repositories through content chunking

Example usage:
```bash
python scripts/generate_readme.py
```

Based on the repository content, I'll generate a README.md file that accurately reflects the purpose and functionality of the provided files.

# README.md

## Project Description
This project provides a sophisticated README generator that automatically creates and updates README.md files based on repository content. It uses AI services (Anthropic and OpenAI) to generate comprehensive documentation by analyzing the files in your repository.

## Installation

### Prerequisites
- Python 3.x
- Required Python packages:
  - anthropic
  - openai
  - typing
  - logging

### Setup
1. Clone the repository
2. Install dependencies:
```bash
pip install anthropic openai
```
3. Set up environment variables:
   - `ANTHROPIC_API_KEY`: Your Anthropic API key
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `AI_MODEL`: The AI model to use for generation

## Usage

### Generate README
The main script `scripts/generate_readme.py` provides the following functionality:

1. **File Type Configuration**
   - Define file types to scan in `.github/config/file_types.json`
   - The script will automatically scan for files matching the specified patterns

2. **Content Analysis**
   - Scans repository for specified file types
   - Reads and processes file contents
   - Chunks large content for API processing

3. **README Generation**
   - Supports both Anthropic and OpenAI APIs
   - Generates structured documentation
   - Handles large repositories through content chunking

Example usage:
```bash
python scripts/generate_readme.py
```

## Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add appropriate error handling and logging
5. Submit a pull request

### Code Style
- Use type hints for function parameters and return values
- Follow PEP 8 guidelines
- Include appropriate error handling and logging
- Document functions using docstrings

### Error Handling
The project includes comprehensive error handling for:
- File operations
- API interactions
- Environment variable management
- Configuration loading

---

For any questions or issues, please open an issue in the repository.I'll help you complete the GitHub Actions workflow file. Based on the Python code shown, here's the complete `workflows/main.yml`:

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
          echo "README_GENERATED=$(echo "$output" | grep "readme_generated=" | cut -d'=' -f2)" >> $GITHUB_ENV

      - name: Commit and push if README changed
        if: env.README_GENERATED == 'true'
        run: |
          git config --local user.email "github-actions[bot]@users.noreply.github.com"
          git config --local user.name "github-actions[bot]"
          git add README.md
          git diff --quiet && git diff --staged --quiet || (git commit -m "Update README.md [skip ci]" && git push)
```

This workflow:

1. Runs on push to the 'readme-update' branch or manual trigger
2. Sets up Python 3.10
3. Installs required dependencies (anthropic and openai packages)
4. Sets environment variables from GitHub secrets
5. Runs the README generation script
6. Checks if the README was successfully generated
7. If successful, commits and pushes changes to the repository

Required GitHub Secrets:
- `ANTHROPIC_API_KEY`: API key for Anthropic
- `OPENAI_API_KEY`: API key for OpenAI
- `AI_PROVIDER`: Preferred AI provider ('anthropic' or 'openai')
- `AI_MODEL`: AI model to use

The workflow includes error handling and will only commit changes if the README was successfully generated. The commit message includes [skip ci] to prevent infinite loops of workflow runs.Here's a generated README.md content:

```markdown
# Repository File Analysis

This repository contains various file types organized for different development purposes. Below is an analysis of the file types and their purposes.

## File Types Overview

- **Python Files** (*.py) - Python source code files
- **Terraform Files** (*.tf) - Infrastructure as Code configuration files
- **Terraform Variables** (*.tfvars) - Terraform variable definition files
- **JavaScript Files** (*.js) - JavaScript source code files
- **TypeScript Files** (*.ts) - TypeScript source code files
- **HTML Files** (*.html) - Web page markup files
- **CSS Files** (*.css) - Stylesheet files
- **Markdown Files** (*.md) - Documentation and text files
- **YAML Files** (*.yml) - Configuration and data files
- **JSON Files** (*.json) - Data interchange files
- **Shell Scripts** (*.sh) - Shell/Bash scripts
- **Dockerfile** (Dockerfile*) - Container definition files
- **C++ Files** (*.cpp) - C++ source code files
- **Java Files** (*.java) - Java source code files
- **Go Files** (*.go) - Go source code files
- **Ruby Files** (*.rb) - Ruby source code files
- **SQL Files** (*.sql) - Database query and schema files

## Purpose

This repository serves as a multi-language development environment supporting:
- Web Development (HTML, CSS, JavaScript, TypeScript)
- Backend Development (Python, Java, Go, Ruby)
- Infrastructure Management (Terraform)
- Container Management (Dockerfile)
- Database Management (SQL)
- System Scripting (Shell Scripts)
- Documentation (Markdown)
- Configuration Management (YAML, JSON)

## Contributing

When contributing to this repository, please ensure your files are placed in appropriate directories according to their type and purpose. Follow the established coding standards for each language and file type.

## File Organization

Files should be organized in a logical directory structure that separates concerns and maintains clean architecture principles. Consider creating separate directories for:

- `src/` - Source code files
- `docs/` - Documentation
- `config/` - Configuration files
- `scripts/` - Utility scripts
- `infrastructure/` - Infrastructure as Code files
- `tests/` - Test files

## Maintenance

This README is automatically generated and updated through GitHub Actions. The file type definitions are maintained in `config/file_types.json`.

---
*Last Updated: [Current Date]*
```

This README provides a clear overview of the file types supported in the repository, their purposes, and basic organization guidelines. It's designed to be informative for new contributors while maintaining a clean, professional format. The content is based on the file types defined in the `file_types.json` configuration file.### Code Style
- Use type hints for function parameters and return values
- Follow PEP 8 guidelines
- Include appropriate error handling and logging
- Document functions using docstrings

### Error Handling
The project includes comprehensive error handling for:
- File operations
- API interactions
- Environment variable management
- Configuration loading

---

For any questions or issues, please open an issue in the repository.I'll help you complete the GitHub Actions workflow file. Based on the Python code shown, here's the complete `workflows/main.yml`:

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
          echo "README_GENERATED=$(echo "$output" | grep "readme_generated=" | cut -d'=' -f2)" >> $GITHUB_ENV

      - name: Commit and push if README changed
        if: env.README_GENERATED == 'true'
        run: |
          git config --local user.email "github-actions[bot]@users.noreply.github.com"
          git config --local user.name "github-actions[bot]"
          git add README.md
          git diff --quiet && git diff --staged --quiet || (git commit -m "Update README.md [skip ci]" && git push)
```

This workflow:

1. Runs on push to the 'readme-update' branch or manual trigger
2. Sets up Python 3.10
3. Installs required dependencies (anthropic and openai packages)
4. Sets environment variables from GitHub secrets
5. Runs the README generation script
6. Checks if the README was successfully generated
7. If successful, commits and pushes changes to the repository

Required GitHub Secrets:
- `ANTHROPIC_API_KEY`: API key for Anthropic
- `OPENAI_API_KEY`: API key for OpenAI
- `AI_PROVIDER`: Preferred AI provider ('anthropic' or 'openai')
- `AI_MODEL`: AI model to use

The workflow includes error handling and will only commit changes if the README was successfully generated. The commit message includes [skip ci] to prevent infinite loops of workflow runs.Here's a generated README.md content:

```markdown
# Repository File Analysis

This repository contains various file types organized for different development purposes. Below is an analysis of the file types and their purposes.

## File Types Overview

- **Python Files** (*.py) - Python source code files
- **Terraform Files** (*.tf) - Infrastructure as Code configuration files
- **Terraform Variables** (*.tfvars) - Terraform variable definition files
- **JavaScript Files** (*.js) - JavaScript source code files
- **TypeScript Files** (*.ts) - TypeScript source code files
- **HTML Files** (*.html) - Web page markup files
- **CSS Files** (*.css) - Stylesheet files
- **Markdown Files** (*.md) - Documentation and text files
- **YAML Files** (*.yml) - Configuration and data files
- **JSON Files** (*.json) - Data interchange files
- **Shell Scripts** (*.sh) - Shell/Bash scripts
- **Dockerfile** (Dockerfile*) - Container definition files
- **C++ Files** (*.cpp) - C++ source code files
- **Java Files** (*.java) - Java source code files
- **Go Files** (*.go) - Go source code files
- **Ruby Files** (*.rb) - Ruby source code files
- **SQL Files** (*.sql) - Database query and schema files

## Purpose

This repository serves as a multi-language development environment supporting:
- Web Development (HTML, CSS, JavaScript, TypeScript)
- Backend Development (Python, Java, Go, Ruby)
- Infrastructure Management (Terraform)
- Container Management (Dockerfile)
- Database Management (SQL)
- System Scripting (Shell Scripts)
- Documentation (Markdown)
- Configuration Management (YAML, JSON)

## Contributing

When contributing to this repository, please ensure your files are placed in appropriate directories according to their type and purpose. Follow the established coding standards for each language and file type.

## File Organization

Files should be organized in a logical directory structure that separates concerns and maintains clean architecture principles. Consider creating separate directories for:

- `src/` - Source code files
- `docs/` - Documentation
- `config/` - Configuration files
- `scripts/` - Utility scripts
- `infrastructure/` - Infrastructure as Code files
- `tests/` - Test files

## Maintenance

This README is automatically generated and updated through GitHub Actions. The file type definitions are maintained in `config/file_types.json`.

---
*Last Updated: [Current Date]*
```

This README provides a clear overview of the file types supported in the repository, their purposes, and basic organization guidelines. It's designed to be informative for new contributors while maintaining a clean, professional format. The content is based on the file types defined in the `file_types.json` configuration file.### Generate README
The main script `scripts/generate_readme.py` provides the following functionality:

1. **File Type Configuration**
   - Define file types to scan in `.github/config/file_types.json`
   - The script will automatically scan for files matching the specified patterns

2. **Content Analysis**
   - Scans repository for specified file types
   - Reads and processes file contents
   - Chunks large content for API processing

3. **README Generation**
   - Supports both Anthropic and OpenAI APIs
   - Generates structured documentation
   - Handles large repositories through content chunking

Example usage:
```bash
python scripts/generate_readme.py
```

## Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add appropriate error handling and logging
5. Submit a pull request

### Code Style
- Use type hints for function parameters and return values
- Follow PEP 8 guidelines
- Include appropriate error handling and logging
- Document functions using docstrings

### Error Handling
The project includes comprehensive error handling for:
- File operations
- API interactions
- Environment variable management
- Configuration loading

---

For any questions or issues, please open an issue in the repository.I'll help you complete the GitHub Actions workflow file. Based on the Python code shown, here's the complete `workflows/main.yml`:

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
          echo "README_GENERATED=$(echo "$output" | grep "readme_generated=" | cut -d'=' -f2)" >> $GITHUB_ENV

      - name: Commit and push if README changed
        if: env.README_GENERATED == 'true'
        run: |
          git config --local user.email "github-actions[bot]@users.noreply.github.com"
          git config --local user.name "github-actions[bot]"
          git add README.md
          git diff --quiet && git diff --staged --quiet || (git commit -m "Update README.md [skip ci]" && git push)
```

This workflow:

1. Runs on push to the 'readme-update' branch or manual trigger
2. Sets up Python 3.10
3. Installs required dependencies (anthropic and openai packages)
4. Sets environment variables from GitHub secrets
5. Runs the README generation script
6. Checks if the README was successfully generated
7. If successful, commits and pushes changes to the repository

Required GitHub Secrets:
- `ANTHROPIC_API_KEY`: API key for Anthropic
- `OPENAI_API_KEY`: API key for OpenAI
- `AI_PROVIDER`: Preferred AI provider ('anthropic' or 'openai')
- `AI_MODEL`: AI model to use

The workflow includes error handling and will only commit changes if the README was successfully generated. The commit message includes [skip ci] to prevent infinite loops of workflow runs.Here's a generated README.md content:

```markdown
# Repository File Analysis

This repository contains various file types organized for different development purposes. Below is an analysis of the file types and their purposes.

## File Types Overview

- **Python Files** (*.py) - Python source code files
- **Terraform Files** (*.tf) - Infrastructure as Code configuration files
- **Terraform Variables** (*.tfvars) - Terraform variable definition files
- **JavaScript Files** (*.js) - JavaScript source code files
- **TypeScript Files** (*.ts) - TypeScript source code files
- **HTML Files** (*.html) - Web page markup files
- **CSS Files** (*.css) - Stylesheet files
- **Markdown Files** (*.md) - Documentation and text files
- **YAML Files** (*.yml) - Configuration and data files
- **JSON Files** (*.json) - Data interchange files
- **Shell Scripts** (*.sh) - Shell/Bash scripts
- **Dockerfile** (Dockerfile*) - Container definition files
- **C++ Files** (*.cpp) - C++ source code files
- **Java Files** (*.java) - Java source code files
- **Go Files** (*.go) - Go source code files
- **Ruby Files** (*.rb) - Ruby source code files
- **SQL Files** (*.sql) - Database query and schema files

## Purpose

This repository serves as a multi-language development environment supporting:
- Web Development (HTML, CSS, JavaScript, TypeScript)
- Backend Development (Python, Java, Go, Ruby)
- Infrastructure Management (Terraform)
- Container Management (Dockerfile)
- Database Management (SQL)
- System Scripting (Shell Scripts)
- Documentation (Markdown)
- Configuration Management (YAML, JSON)

## Contributing

When contributing to this repository, please ensure your files are placed in appropriate directories according to their type and purpose. Follow the established coding standards for each language and file type.

## File Organization

Files should be organized in a logical directory structure that separates concerns and maintains clean architecture principles. Consider creating separate directories for:

- `src/` - Source code files
- `docs/` - Documentation
- `config/` - Configuration files
- `scripts/` - Utility scripts
- `infrastructure/` - Infrastructure as Code files
- `tests/` - Test files

## Maintenance

This README is automatically generated and updated through GitHub Actions. The file type definitions are maintained in `config/file_types.json`.

---
*Last Updated: [Current Date]*
```

This README provides a clear overview of the file types supported in the repository, their purposes, and basic organization guidelines. It's designed to be informative for new contributors while maintaining a clean, professional format. The content is based on the file types defined in the `file_types.json` configuration file.### Prerequisites
- Python 3.x
- Required Python packages:
  - anthropic
  - openai
  - typing
  - logging

### Setup
1. Clone the repository
2. Install dependencies:
```bash
pip install anthropic openai
```
3. Set up environment variables:
   - `ANTHROPIC_API_KEY`: Your Anthropic API key
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `AI_MODEL`: The AI model to use for generation

## Usage

### Generate README
The main script `scripts/generate_readme.py` provides the following functionality:

1. **File Type Configuration**
   - Define file types to scan in `.github/config/file_types.json`
   - The script will automatically scan for files matching the specified patterns

2. **Content Analysis**
   - Scans repository for specified file types
   - Reads and processes file contents
   - Chunks large content for API processing

3. **README Generation**
   - Supports both Anthropic and OpenAI APIs
   - Generates structured documentation
   - Handles large repositories through content chunking

Example usage:
```bash
python scripts/generate_readme.py
```

## Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add appropriate error handling and logging
5. Submit a pull request

### Code Style
- Use type hints for function parameters and return values
- Follow PEP 8 guidelines
- Include appropriate error handling and logging
- Document functions using docstrings

### Error Handling
The project includes comprehensive error handling for:
- File operations
- API interactions
- Environment variable management
- Configuration loading

---

For any questions or issues, please open an issue in the repository.I'll help you complete the GitHub Actions workflow file. Based on the Python code shown, here's the complete `workflows/main.yml`:

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
          echo "README_GENERATED=$(echo "$output" | grep "readme_generated=" | cut -d'=' -f2)" >> $GITHUB_ENV

      - name: Commit and push if README changed
        if: env.README_GENERATED == 'true'
        run: |
          git config --local user.email "github-actions[bot]@users.noreply.github.com"
          git config --local user.name "github-actions[bot]"
          git add README.md
          git diff --quiet && git diff --staged --quiet || (git commit -m "Update README.md [skip ci]" && git push)
```

This workflow:

1. Runs on push to the 'readme-update' branch or manual trigger
2. Sets up Python 3.10
3. Installs required dependencies (anthropic and openai packages)
4. Sets environment variables from GitHub secrets
5. Runs the README generation script
6. Checks if the README was successfully generated
7. If successful, commits and pushes changes to the repository

Required GitHub Secrets:
- `ANTHROPIC_API_KEY`: API key for Anthropic
- `OPENAI_API_KEY`: API key for OpenAI
- `AI_PROVIDER`: Preferred AI provider ('anthropic' or 'openai')
- `AI_MODEL`: AI model to use

The workflow includes error handling and will only commit changes if the README was successfully generated. The commit message includes [skip ci] to prevent infinite loops of workflow runs.Here's a generated README.md content:

```markdown
# Repository File Analysis

This repository contains various file types organized for different development purposes. Below is an analysis of the file types and their purposes.

## File Types Overview

- **Python Files** (*.py) - Python source code files
- **Terraform Files** (*.tf) - Infrastructure as Code configuration files
- **Terraform Variables** (*.tfvars) - Terraform variable definition files
- **JavaScript Files** (*.js) - JavaScript source code files
- **TypeScript Files** (*.ts) - TypeScript source code files
- **HTML Files** (*.html) - Web page markup files
- **CSS Files** (*.css) - Stylesheet files
- **Markdown Files** (*.md) - Documentation and text files
- **YAML Files** (*.yml) - Configuration and data files
- **JSON Files** (*.json) - Data interchange files
- **Shell Scripts** (*.sh) - Shell/Bash scripts
- **Dockerfile** (Dockerfile*) - Container definition files
- **C++ Files** (*.cpp) - C++ source code files
- **Java Files** (*.java) - Java source code files
- **Go Files** (*.go) - Go source code files
- **Ruby Files** (*.rb) - Ruby source code files
- **SQL Files** (*.sql) - Database query and schema files

## Purpose

This repository serves as a multi-language development environment supporting:
- Web Development (HTML, CSS, JavaScript, TypeScript)
- Backend Development (Python, Java, Go, Ruby)
- Infrastructure Management (Terraform)
- Container Management (Dockerfile)
- Database Management (SQL)
- System Scripting (Shell Scripts)
- Documentation (Markdown)
- Configuration Management (YAML, JSON)

## Contributing

When contributing to this repository, please ensure your files are placed in appropriate directories according to their type and purpose. Follow the established coding standards for each language and file type.

## File Organization

Files should be organized in a logical directory structure that separates concerns and maintains clean architecture principles. Consider creating separate directories for:

- `src/` - Source code files
- `docs/` - Documentation
- `config/` - Configuration files
- `scripts/` - Utility scripts
- `infrastructure/` - Infrastructure as Code files
- `tests/` - Test files

## Maintenance

This README is automatically generated and updated through GitHub Actions. The file type definitions are maintained in `config/file_types.json`.

---
*Last Updated: [Current Date]*
```

This README provides a clear overview of the file types supported in the repository, their purposes, and basic organization guidelines. It's designed to be informative for new contributors while maintaining a clean, professional format. The content is based on the file types defined in the `file_types.json` configuration file.