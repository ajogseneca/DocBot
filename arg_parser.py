import argparse
import tomli  # toml parser

def parse_arguments():
    parser = argparse.ArgumentParser(description="CLI tool for generating README files using Groq models.")
    
    # Define arguments
    parser.add_argument("files", nargs="*", help="List of source files to process")
    parser.add_argument("--output", help="Output file to save the generated README")
    parser.add_argument("--models", nargs="+", help="List of models to use for generation")
    parser.add_argument("--api_key", help="API key for Groq client")
    parser.add_argument("--token", help="Token for Groq client")
    parser.add_argument("--config", help="Path to a config file (TOML format)")
    parser.add_argument('--version', '-v', action='store_true', help="Show the tool's version")
    
    # Parse arguments
    args = parser.parse_args()

    # Load config from TOML file if provided
    toml_dict = {}
    if args.config:
        with open(args.config, 'rb') as toml_file:
            toml_dict = tomli.load(toml_file)

    return args, toml_dict
