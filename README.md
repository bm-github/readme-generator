## Project Description
This is a Python-based tool that automatically generates README documentation by analyzing repository content using AI services (Anthropic and OpenAI). The project features:

- Flexible AI provider selection between Anthropic and OpenAI
- Automated repository scanning and content analysis
- Configurable file type filtering
- Robust error handling and logging
- Support for processing large codebases through content chunking

## Installation
1. Clone the repository
```bash
git clone [repository-url]
```

2. Install required dependencies
```bash
pip install anthropic openai
```

3. Set up environment variables
```bash
export ANTHROPIC_API_KEY="your-anthropic-key"
export OPENAI_API_KEY="your-openai-key"
export AI_PROVIDER="anthropic|openai"
export AI_MODEL="your-preferred-model"
```

## Usage
1. Configure file types to scan in `.github/config/file_types.json`:
```json
{
  "Python": "**/*.py",
  "Configuration": "**/*.json"
}
```

2. Run the script:
```bash
python scripts/generate_readme.py
```

The script will:
- Scan your repository for specified file types
- Process the content using the configured AI provider
- Generate a comprehensive README.md file

## Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Implement your changes
4. Add appropriate logging statements
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

Please ensure your contributions maintain the existing error handling and logging patterns, and include appropriate documentation.Here's the completion of the YAML file based on the context:

```yaml
# --- workflows/main.yml (continued) ---
          AI_MODEL: ${{ vars.AI_MODEL }}
          FALLBACK_PROVIDER: ${{ vars.FALLBACK_PROVIDER }}

      - name: Check README Generation
        id: check_readme
        run: |
          if [ -f README.md ]; then
            echo "README.md was generated successfully"
            echo "readme_exists=true" >> $GITHUB_OUTPUT
          else
            echo "README.md was not generated"
            echo "readme_exists=false" >> $GITHUB_OUTPUT
            exit 1
          fi

      - name: Create Pull Request
        if: steps.check_readme.outputs.readme_exists == 'true'
        uses: peter-evans/create-pull-request@v5
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
          commit-message: "docs: Update README.md with AI-generated content"
          title: "docs: Update README.md"
          body: |
            This PR updates the README.md with AI-generated content based on the repository structure.
            
            Please review the changes and merge if appropriate.
          branch: update-readme
          delete-branch: true
          base: main
```

This workflow:
1. Sets up Python and installs required dependencies
2. Runs the README generation script with necessary environment variables
3. Checks if README was generated successfully
4. Creates a pull request with the updated README if generation was successful

The environment variables include:
- API keys for both Anthropic and OpenAI
- Primary AI provider preference
- AI model selection
- Fallback provider configuration

The pull request is created using the peter-evans/create-pull-request action with:
- Automated commit message and PR title
- Descriptive PR body
- Creates/updates on a dedicated branch
- Targets the main branch
- Deletes the branch after mergingBased on the provided workflow snippet and JSON configuration file, it seems you're working with GitHub Actions to update a README file. Let me help improve and explain the code:

```yaml
      - name: Update README using AI
        env:
          AI_MODEL: ${{ vars.AI_MODEL }}
        run: |
          # Configure git
          git config user.name github-actions[bot]
          git config user.email github-actions[bot]@users.noreply.github.com
          
          # Create/update README.md
          echo "# Repository Analysis" > README.md
          echo "" >> README.md
          echo "Analysis performed using ${AI_MODEL}" >> README.md
          echo "" >> README.md
          
          # Process each file type from config
          while IFS=':' read -r type pattern; do
            # Remove quotes and commas
            pattern=$(echo "$pattern" | tr -d '," ')
            type=$(echo "$type" | tr -d '" ')
            
            # Count files of each type
            count=$(find . -type f -name "$pattern" | wc -l)
            
            if [ $count -gt 0 ]; then
              echo "## $type" >> README.md
              echo "Found $count file(s)" >> README.md
              echo "" >> README.md
            fi
          done < <(jq -r 'to_entries | .[] | "\(.key):\(.value)"' config/file_types.json)
          
          # Commit and push changes
          git add README.md
          git commit -m "Update README.md with repository analysis" || echo "No changes to commit"
          git push origin HEAD:readme-update
```

This improved version:

1. Uses the AI_MODEL variable from GitHub variables properly
2. Creates a structured README with:
   - A main heading
   - AI model information
   - Sections for each file type found
3. Processes the file_types.json configuration to:
   - Count files matching each pattern
   - Only adds sections for file types that are actually present
4. Handles the git operations safely

To use this:

1. Set up a GitHub variable named `AI_MODEL` with your AI model name
2. Ensure the config/file_types.json is present in your repository
3. Add this step to your GitHub Actions workflow

The script will:
- Create a new README.md
- Add sections for each file type found in your repository
- Commit and push changes to a readme-update branch

Example output might look like:
```markdown
# Repository Analysis

Analysis performed using GPT-4
