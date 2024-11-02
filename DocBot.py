import sys
from arg_parser import parse_arguments  # Import the argument parsing function
from file_handler import handle_output  # Import the output handling function
from api import AVAILABLE_MODELS


# Main function to handle the CLI tool logic
def main():
    # Parse command-line arguments and TOML configuration
    args, toml_dict = parse_arguments()

    # Extract version information
    tool_name = "DocBot"
    tool_version = "0.3"

    # Check for version flag in arguments or TOML and display the version if needed
    if args.version or toml_dict.get("version"):
        show_version(tool_name, tool_version)
        sys.exit(0)

    # Check if any files were provided; if not, print usage and exit with error
    if not args.files:
        print("error: the following arguments are required: file", file=sys.stderr)
        sys.exit(1)

    # Determine which models to use: prioritize CLI arguments, then TOML, or use defaults
    models_to_use = get_models(args, toml_dict)

    # Set API key from CLI arguments or TOML configuration
    api_key = get_api_key(args, toml_dict)

    # Set token flag from CLI arguments or TOML configuration
    token = get_token(args, toml_dict)

    # Process each input file and generate the README
    handle_output(args, toml_dict, models_to_use, api_key, token)


# Function to display the tool's version
def show_version(tool_name, tool_version):
    print(f"{tool_name}, version {tool_version}")


# Function to resolve which models to use for README generation
def get_models(args, toml_dict):
    return args.models or toml_dict.get("models") or AVAILABLE_MODELS


# Function to resolve the API key from CLI arguments or TOML configuration
def get_api_key(args, toml_dict):
    return args.api_key or toml_dict.get("api_key")


# Function to resolve the token flag from CLI arguments or TOML configuration
def get_token(args, toml_dict):
    return args.token or toml_dict.get("token")


# Entry point of the script
if __name__ == "__main__":
    main()
