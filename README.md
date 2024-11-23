
# DocBot-AI

DocBot-AI is a powerful command-line tool that automates the creation of comprehensive README files for your projects. Utilizing advanced AI models through the Groq API, DocBot-AI analyzes source code files to generate detailed documentation. This tool is ideal for developers who want to simplify their documentation process.

## Features

- **Automated README Generation**: Generate detailed README files based on your source code.
- **Model Selection**: Choose from various Groq models, including `llama3-8b-8192`, `mixtral-8x7b-32768`, and `llava-v1.5-7b-4096-preview`.
- **Token Usage Statistics**: View token usage data after README generation (optional).
- **Custom Output**: Direct the output to a specific file or display it in the terminal.
- **TOML Configuration Support**: Set default parameters using a configuration file.

---

## Installation

### Prerequisites

1. Python 3.10 or higher.
2. [Groq API Python Client](https://pypi.org/project/groq/).
3. `pip` installed on your system.
4. **Note:** Ensure that the Groq API key is set as an environment variable (GROQ_API_KEY) before using the tool. This can be done by adding the key to your .env file or directly exporting it in your terminal.

### Installation Steps

1. **Install DocBot-AI**:
   ```bash
   pip install docbot-ai
   ```

2. **Verify Installation**:
   Ensure the tool is installed correctly by running:
   ```bash
   docbot-ai -v
   ```

   You should see the version of DocBot-AI displayed.

---

## Usage

### Running the Tool

Run the `docbot-ai` command from your terminal, providing source files and any necessary options:

```bash
docbot-ai <files> [OPTIONS]
```

### Common Options

- `files`: List of source files to process for README generation.
- `--output <output_file>`: Specify the output file for the generated README.
- `--models <model1> <model2>`: List of Groq models to use for generation.
- `--api_key <API_KEY>`: API key for Groq (optional if specified in a `.env` file).
- `--token (-t)`: Display token usage after generating the README.
- `--config <config_file>`: Path to a TOML config file (default: `.docbot-config.toml`).
- `--version (-v)`: Display the current version of DocBot-AI.

### Example Usage

1. Generate a README for `app.py` and save it to `README.md`:
   ```bash
   docbot-ai app.py --output README.md
   ```

2. Specify multiple AI models for README generation:
   ```bash
   docbot-ai app.py --models llama3-8b-8192 mixtral-8x7b-32768
   ```

3. Use a custom TOML configuration file:
   ```bash
   docbot-ai app.py --config my-config.toml
   ```

---


## Video of Tool in Action


https://github.com/user-attachments/assets/e1930888-27c4-4feb-ad80-62691ec9c2cd


## Development Setup

### Clone the Repository

For local development, clone the repository and set up the environment:

```bash
git clone https://github.com/ajogseneca/DocBot.git
cd DocBot
```

### Install Dependencies

Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

### Run the CLI Locally

Use the following command to test the tool locally:

```bash
python -m docbot_app.src.DocBot <files> [OPTIONS]
```

---

## Code Overview

- **`src/api.py`**: Handles Groq API interactions, including README content generation and error handling.
- **`src/arg_parser.py`**: Parses command-line arguments and manages TOML configurations.
- **`src/file_handler.py`**: Processes input files and directs README content to the specified output.
- **`src/DocBot.py`**: The main script that orchestrates the CLI operations, integrates components, and generates READMEs.

---

## Important Notes

- Install all dependencies (`dotenv`, `groq`, etc.) before running the tool.
- Ensure you have access to the Groq API and a valid API key to use this tool.
- The generated README content serves as a starting point and may require manual refinement.
- Review Groq API pricing and usage policies before using this tool for production-level projects.

---

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
