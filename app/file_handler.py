import sys

from app.api import generate_readme


def handle_output(args, toml_dict, models_to_use, api_key, token):
    # Handles output based on the specified output file or defaults to terminal output.
    output_path = args.output or toml_dict.get("output")

    if output_path:
        try:
            with open(output_path, "w") as output_file:
                process_files(args.files, output_file, models_to_use, api_key, token)
        except Exception as e:
            print(
                f"An error occurred while writing to {output_path}: {str(e)}",
                file=sys.stderr,
            )
            sys.exit(1)
    else:
        # If no output file specified, print to terminal
        process_files(args.files, None, models_to_use, api_key, token)


def process_files(files, output_file, models_to_use, api_key, token):
    # Processes each input file and generates the README.
    for file in files:
        try:
            print(f"Processing file: {file}", file=sys.stderr)
            if output_file:
                generate_readme(
                    file,
                    output_file=output_file,
                    models=models_to_use,
                    api_key=api_key,
                    token=token,
                )
            else:
                generate_readme(
                    file, models=models_to_use, api_key=api_key, token=token
                )
        except Exception as e:
            print(
                f"An error occurred while processing {file}: {str(e)}", file=sys.stderr
            )
            sys.exit(1)  # Exit with error if file processing fails
