# README FILE
## Content generated using Groq AI 


**README Generation Tool**

This tool generates a README description for a given code snippet using the Groq AI API. The tool reads in a source code file, uses the Groq API to generate a README description, and writes the output to a user-specified file or prints it to the CLI.

**Usage**

1. Install the required dependencies (dotenv, groq)
2. Run the script with the following arguments:
    - `source_file`: The path to the source code file you'd like to generate a README description for.
    - `generated_file`: The file path (optional) where you'd like to write the generated README description. If not specified, the file will be printed to the CLI. Default is "README.md".
    - `api_key`: Your Groq API key (optional, can be set as an environment variable).

**Environment Variables**

* `GROQ_API_KEY`: Your Groq API key. If not set, you'll be prompted to set an API key when running the script.

**Features**

* Supports multiple input files
* Option to generate a separate README file for each input file
* Option to output the generated README file to a specified file or to the console
* Supports API key authentication for Groq AI
* Option to outpout token usage

**Getting Started**

1. Run DocBot by running `python docbot <options> <files>`
2. Options:
	* `--version` or `-v`: Show the version of DocBot
	* `--output` or `-o`: Specify the output file (default: stdout)
	* `--api-key`: Specify the API key for Groq AI
	* `--multi-file` or `-mf`: Generate a separate README file for each input file
	* `--token` or `-t`: Display token usage after generating README
3. Files: Specify the input files for which you want to generate README files

**Example Usage**

Example 1: Generate a single README file for a single input file
```bash
docbot --output my_readme.md my_file.txt
```
Example 2: Generate separate README files for multiple input files
```bash
docbot --multi-file my_file1.txt my_file2.txt my_file3.txt
```
Example 3: Generate a single README file for multiple input files and output to the console
```bash
docbot my_file1.txt my_file2.txt my_file3.txt
```
**Video of Tool in Action**


https://github.com/user-attachments/assets/e1930888-27c4-4feb-ad80-62691ec9c2cd



**Note**

* Make sure to install the required dependencies (dotenv, groq) before running the script.
* The generated README description is intended to be a starting point and may require editing to ensure accuracy and completeness.
* The Groq API usage and pricing policies apply to this script. Please review their terms and conditions before using this tool in production.

**License**

This script is licensed under the [MIT License](https://opensource.org/licenses/MIT).
