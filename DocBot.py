import sys
import argparse
from api import generate_readme
import os

# Version information
TOOL_NAME = "DocBot"
TOOL_VERSION = "0.1"

# Functions to handle CLI arguments
def main():
    parser = argparse.ArgumentParser(description="A CLI tool called DocBot to generate README files using Groq AI.")
    
    # Required flags
    parser.add_argument('--version', '-v', action='store_true', help="Show the tool's version")
    parser.add_argument('--output', '-o', type=str, default="cli_print", help="Specify output file (default: stdout)")
    parser.add_argument('--api-key', type=str, help="Specify the API key for Groq API")
    parser.add_argument('--multi-file', '-mf', action='store_true', help="Generate a separate README for each input file")
    
    # Accepting multiple files
    parser.add_argument('files', metavar='file', type=str, nargs='*', help='Source file(s) to generate README for')
    
    # Viewing token usage
    parser.add_argument('--token', '-t', action='store_true', help="Display token usage after generating README")

    
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
    if args.multi_file:
        # If multi-file flag is set, generate separate README for each file, using splitext
        for file in args.files:
            print(f"Processing file: {file}", file=sys.stderr)
            output_file = f"{os.path.splitext(file)[0]}_README.md"
            generate_readme(file, output_file, api_key=args.api_key, token=args.token)
    else:
        # If multi-file flag is not set, generate a single README file or append to output file
        if args.output == "cli_print":
            for file in args.files:
                print(f"Processing file: {file}", file=sys.stderr)
                generate_readme(file, "cli_print", api_key=args.api_key, token=args.token)
        else:
            # Append content to the specified output file for multiple files
            with open(args.output, 'w') as output_file:
                for file in args.files:
                    print(f"Processing file: {file}", file=sys.stderr)
                    # Write or append to the output file
                    output_file.write(f"# README for {file}\n\n")
                    generate_readme(file, args.output, api_key=args.api_key, token=args.token)

if __name__ == "__main__":
    main()
