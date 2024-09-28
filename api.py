import os
import sys
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Available models for the users to use
AVAILABLE_MODELS = ["llama3-8b-8192", "mixtral-8x7b-32768", "llava-v1.5-7b-4096-preview"]

# Function to initialize Groq client with optional API key
def initialize_groq_client(api_key=None):
    api_key_value = api_key if api_key else os.environ.get("GROQ_API_KEY")
    if not api_key_value:
        print("Error: No API key provided or found in environment variables.", file=sys.stderr)
        sys.exit(1)  # Exiting if the API key is missing
    return Groq(api_key=api_key_value)

# Function to generate README using multiple models
def generate_readme(source_file, output_file=None, models=None, api_key=None, token=None):
    if models is None:
        models = AVAILABLE_MODELS

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

    # Iterate through each model to generate README
    for model in models:
        print(f"Generating README using model: {model}", file=sys.stderr)
        try:
            chat_completion = client.chat.completions.create(
                messages=[{
                    "role": "user",
                    "content": f"Generate a README description for the following code:\n\n{source_content}",
                }],
                model=model,
            )
            readme_content = chat_completion.choices[0].message.content

            # Check if token usage should be displayed
            if token:
                usage = chat_completion.usage
                print(f"Token usage for model {model}:")
                print(f"  Total tokens: {usage.total_tokens}")
                print(f"  Prompt tokens: {usage.prompt_tokens}")
                print(f"  Completion tokens: {usage.completion_tokens}")

            if output_file:
                # Generate unique output filename for each model
                model_output_file = f"{os.path.splitext(output_file)[0]}_{model}_README.md"
                try:
                    with open(model_output_file, 'w') as readme_file:
                        readme_file.write(f"# README FILE (Model: {model})\n\n## Content generated using {model} \n\n{readme_content}\n")
                    print(f"README file created at {model_output_file}")
                except IOError as e:
                    print(f"Error writing to {model_output_file}: {str(e)}", file=sys.stderr)
                    sys.exit(1)  # Exiting if writing to the file fails
            else:
                # Print to terminal if no output file specified
                sys.stdout.write(f"\n\n# README FILE (Model: {model})\n\n{readme_content}\n")
        
        except Exception as e:
            print(f"Error generating README with model {model}: {str(e)}", file=sys.stderr)
            sys.exit(1)  # Exiting with an error if the Groq API request fails
