# README FILE

## Content generated using Groq AI 

Here is a README description for the code:

**DocBot: A CLI tool to generate README files using Groq AI**

**Overview**
--------

DocBot is a command-line interface (CLI) tool that uses Groq AI to generate README files for your code projects. Simply provide the source code file(s) as input, and DocBot will create a README.md file with a human-readable description of the code.

**Features**
-------

* Generate README files using Groq AI's chat completion feature
* Supports multiple source files as input
* Option to specify output file name or write to stdout
* Displays tool version on demand
* Supports basic error handling

**Usage**
-------

run `DocBot.py [-h] [--version] [--output OUTPUT] [file ...]`
   -h, --help     show this help message and exit
   --version     show the tool's version and exit
   --output OUTPUT, -o OUTPUT
                     Specify output file (default: stdout)
   file           Source file(s) to generate README for

**Example**
--------

To generate a README file for a file named `example.py`, use the following command:
```
DocBot.py --output README.md example.py
```
This will create a file named `README.md` in the current directory with a human-readable description of the code in `example.py`.

**Note**
-----

Make sure to install the Groq library and set your Groq API key as an environment variable named `GROQ_API_KEY` for this tool to work.

I hope this helps!
