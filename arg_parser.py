import argparse
import tomli  # toml parser
import sys  # for stderr and exit

def parse_arguments():
    parser = argparse.ArgumentParser(description="CLI tool for generating README files using Groq models.")
    
    # Define arguments
    parser.add_argument("files", nargs="*", help="List of source files to process")
    parser.add_argument("--output", help="Output file to save the generated README")
    parser.add_argument("--models", nargs="+", help="List of models to use for generation")
    parser.add_argument("--api_key", help="API key for Groq client")
    parser.add_argument('--token', '-t', action='store_true', help="Display token usage after generating README")
    parser.add_argument("--config", help="Path to a config file (TOML format)")
    parser.add_argument('--version', '-v', action='store_true', help="Show the tool's version")
    
    # Parse arguments
    args = parser.parse_args()

    # Load config from TOML file if provided, or use default config file
    toml_dict = {}
    config_file = ".docbot-config.toml"
    
    try:
        with open(config_file, 'rb') as toml_file:
            toml_dict = tomli.load(toml_file)
    except FileNotFoundError:
        # If no config file is found, we continue with an empty dictionary
        toml_dict = {}
    except tomli.TOMLDecodeError:
        print("Error: Cannot parse TOML, invalid syntax", file=sys.stderr)
        sys.exit(1)

    return args, toml_dict
