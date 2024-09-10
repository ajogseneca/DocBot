import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def generate_readme(source_file, generated_file="README.md"):
    # Read the source file, check if the path exist or not
    try:
        with open(source_file, 'r') as source_file:
            source_content = source_file.read()
    except FileNotFoundError:
        print(f"Source file {source_file} not found.") 
        return

    # Generate a basic Readme.md description using Groq API
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

    # Write the generated description to a README file
    try:
        with open(generated_file, 'w') as readme_file:
            readme_file.write(f"# README FILE\n\n## Content generated using Groq AI \n\n{readme_content}\n")
        print(f"README file created at {generated_file}")
    except Exception as e:
        print(f"Error writing to {generated_file}: {str(e)}")

# Calling the functions
source_file_path = ""
generate_readme(source_file_path)
