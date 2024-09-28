import sys
import argparse
from api import generate_readme, AVAILABLE_MODELS
import os

# Version information
TOOL_NAME = "DocBot"
TOOL_VERSION = "0.1"

# Functions to handle CLI arguments
def main():
    parser = argparse.ArgumentParser(description="A CLI tool called DocBot to generate README files using Groq AI.")
    
    # Required flags
    parser.add_argument('--version', '-v', action='store_true', help="Show the tool's version")
    parser.add_argument('--output', '-o', type=str, help="Specify output file (default: print to terminal)")
    parser.add_argument('--api-key', type=str, help="Specify the API key for Groq API")
    
    # Accepting multiple models
    parser.add_argument('--models', '-m', nargs='+', type=str,  metavar='model', choices=AVAILABLE_MODELS, help=f"Specify models (default: all available models: {AVAILABLE_MODELS})")
    
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

    # Use specified models or default to all available models
    models_to_use = args.models if args.models else AVAILABLE_MODELS

    # Process each input file
    try:
        if args.output:
            with open(args.output, 'w') as output_file:
                for file in args.files:
                    print(f"Processing file: {file}", file=sys.stderr)
                    generate_readme(file, output_file=args.output, models=models_to_use, api_key=args.api_key, token=args.token)
        else:
            # If no output is provided, print to terminal
            for file in args.files:
                print(f"Processing file: {file}", file=sys.stderr)
                generate_readme(file, models=models_to_use, api_key=args.api_key, token=args.token)
    except Exception as e:
        print(f"An error occurred: {str(e)}", file=sys.stderr)
        sys.exit(1)  # Exiting on any processing error

if __name__ == "__main__":
    main()
