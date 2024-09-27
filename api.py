import os
import sys
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Function to initialize Groq client with optional API key
def initialize_groq_client(api_key=None):
    api_key_value = api_key if api_key else os.environ.get("GROQ_API_KEY")
    if not api_key_value:
        print("Error: No API key provided or found in environment variables.", file=sys.stderr)
        sys.exit(1)  # Exiting if the API key is missing
    return Groq(api_key=api_key_value)

# Function to generate README
def generate_readme(source_file, generated_file="README.md", api_key=None, token=None):
    # Initialize Groq client
    try:
        client = initialize_groq_client(api_key)
    except Exception as e:
        print(f"Error initializing Groq client: {str(e)}", file=sys.stderr)
        sys.exit(1)  # Exiting if there is an error initializing the client

    # Try to read the source file
    try:
        with open(source_file, 'r') as f:
            source_content = f.read()
    except FileNotFoundError:
        print(f"Error: Source file {source_file} not found.", file=sys.stderr)
        sys.exit(1)  # Exiting with an error if the file is not found
    except Exception as e:
        print(f"Error reading source file {source_file}: {str(e)}", file=sys.stderr)
        sys.exit(1)  # Exiting with an error if reading the file fails

    # Generate a basic Readme.md description using Groq API
    try:
        chat_completion = client.chat.completions.create(
            messages=[{
                "role": "user",
                "content": f"Generate a README description for the following code:\n\n{source_content}",
            }],
            model="llama3-8b-8192",
        )
        readme_content = chat_completion.choices[0].message.content

        # Check if token usage should be displayed
        if token:
            usage = chat_completion.usage
            print(f"Token usage:")
            print(f"  Total tokens: {usage.total_tokens}")
            print(f"  Prompt tokens: {usage.prompt_tokens}")
            print(f"  Completion tokens: {usage.completion_tokens}")

        # Print the generated README content to CLI, if no file is specified
        if generated_file == "cli_print":
            sys.stdout.write(readme_content + "\n")
        else:
            try:
                with open(generated_file, 'w') as readme_file:
                    readme_file.write(f"# README FILE\n\n## Content generated using Groq AI \n\n{readme_content}\n")
                print(f"README file created at {generated_file}")
            except IOError as e:
                print(f"Error writing to {generated_file}: {str(e)}", file=sys.stderr)
                sys.exit(1)  # Exiting if writing to the file fails

    except Exception as e:
        print(f"Error generating README content: {str(e)}", file=sys.stderr)
        sys.exit(1)  # Exiting with an error if the Groq API request fails
