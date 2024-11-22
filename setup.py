from setuptools import find_packages, setup

# Read long description from the README.md file
with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="DocBot",
    version="1.0.0",
    description="A LLM tool that generates README files for your files. Uses Groq AI",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ajogseneca/DocBot",
    author="Ajo George",
    author_email="ageorge55@myseneca.ca",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.12.6",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "flake8",  # Code style checker
        "pytest",  # Testing framework
        "python-dotenv",  # Manage .env files for environment variables
        "groq",  # Groq AI integration
    ],
    extras_require={
        "dev": [
            "flake8",  # for linting
            "pytest",  # for testing
        ],
        "dotenv": [
            "python-dotenv",  # to handle environment variables from .env files
        ],
    },
    python_requires=">=3.10",
)
