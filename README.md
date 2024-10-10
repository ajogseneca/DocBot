


# DocBot

DocBot is a command-line tool designed to automate the generation of README files for projects using AI-powered language models. Leveraging Groq API's advanced language models, DocBot reads source code files and generates comprehensive README documentation based on the content, making it especially useful for developers who want to streamline documentation.

## Features

- **README Generation**: Automatically generate detailed README files based on source code content.
- **Multi-Model Support**: Choose from a range of Groq models, including `llama3-8b-8192`, `mixtral-8x7b-32768`, and `llava-v1.5-7b-4096-preview`.
- **Token Usage Display**: Optionally display token usage statistics after README generation.
- **Configurable Output**: Direct output to a file or print to the terminal.
- **Config File Support**: Use a TOML configuration file to set default parameters.

## Installation

### Requirements
- Python 3.6+
- [Groq API Python Client](https://pypi.org/project/groq/) 

### Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ajogseneca/DocBot.git
   cd DocBot

## Usage
Run DocBot from the command line, providing source files and optional arguments.
```
files: List of source files to process for README generation.
--output <output_file>: Specify the output file for the generated README.
--models <model1> <model2> ...: List of Groq models to use for generation.
--api_key <API_KEY>: API key for Groq (optional if specified in .env).
--token (-t): Display token usage after generating README.
--config <config_file>: Path to a TOML config file (defaults to .docbot-config.toml).
--version (-v): Display the current version of DocBot.
```

## Code Overview
### api.py
Handles initialization and interaction with the Groq API for generating README content. Supports multiple models and error handling for file and API operations.

### arg_parser.py
Defines and parses command-line arguments for DocBot, including options for files, output, models, and config files. Includes support for loading configuration from TOML 

### file_handler.py
Processes files specified by the user and manages output, directing README content either to a file or the terminal.

### DocBot.py
Main script that integrates components, processes user inputs, and initiates README generation using Groq API models.


**Video of Tool in Action**


https://github.com/user-attachments/assets/e1930888-27c4-4feb-ad80-62691ec9c2cd



**Note**

* Make sure to install the required dependencies (dotenv, groq) before running the script.
* The generated README description is intended to be a starting point and may require editing to ensure accuracy and completeness.
* The Groq API usage and pricing policies apply to this script. Please review their terms and conditions before using this tool in production.

**License**

This script is licensed under the [MIT License](https://opensource.org/licenses/MIT).
