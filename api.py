# api.py

import os
import sys
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# Function to generate README
def generate_readme(source_file, generated_file="README.md"):
    try:
        with open(source_file, 'r') as f:
            source_content = f.read()
    except FileNotFoundError:
        print(f"Error: Source file {source_file} not found.", file=sys.stderr)
        return

    # Generate a basic Readme.md description using Groq API
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"Generate a README description for the following code:\n\n{source_content}",
                }
            ],
            model="llama3-8b-8192",
        )
        readme_content = chat_completion.choices[0].message.content

        # Print the generated file to CLI, when no file name is mentioned to write
        if generated_file == "cli_print":
            sys.stdout.write(readme_content + "\n")
        else:
            with open(generated_file, 'w') as readme_file:
                readme_file.write(f"# README FILE\n\n## Content generated using Groq AI \n\n{readme_content}\n")
            print(f"README file created at {generated_file}")

    except Exception as e:
        print(f"Error writing to {generated_file}: {str(e)}", file=sys.stderr)
