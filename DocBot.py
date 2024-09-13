# main.py

import sys
import argparse
from api import generate_readme

# Version information
TOOL_NAME = "DocBot"
TOOL_VERSION = "0.1"

# Functions to handle CLI arguments
def main():
    parser = argparse.ArgumentParser(description="A CLI tool called DocBot to generate README files using Groq AI.")
    
    # Required flags
    parser.add_argument('--version', '-v', action='store_true', help="Show the tool's version")
    parser.add_argument('--output', '-o', type=str, default="cli_print", help="Specify output file (default: stdout)")
    # Accepting multiple files
    parser.add_argument('files', metavar='file', type=str, nargs='*', help='Source file(s) to generate README for')
    
    args = parser.parse_args()

    # Check for version flag before anything else
    if args.version:
        print(f"{TOOL_NAME}, version {TOOL_VERSION}")
        sys.exit(0)

    # Check if any files were provided
    if not args.files:
        parser.print_usage()
        print("error: the following arguments are required: file", file=sys.stderr)
        sys.exit(1)

    # Process each input file
    for file in args.files:
        print(f"Processing file: {file}", file=sys.stderr)
        generate_readme(file, args.output)


if __name__ == "__main__":
    main()
