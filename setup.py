from setuptools import find_packages, setup

# Read long description from the README.md file
with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="docbot_ai",
    version="1.0.1",
    description="A LLM tool that generates README files for your files. Uses Groq AI",
    package_dir={"": "app"},  # Map packages starting from "app/"
    packages=find_packages(where="app"),  # Discover all packages under "app/"
    entry_points={
        "console_scripts": [
            "docbot-ai=docbot_app.src.DocBot:main",  # Path to main function
        ],
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ajogseneca/DocBot",
    author="Ajo George",
    author_email="ageorge55@myseneca.ca",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.12",
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
            "flake8",
            "pytest",
            "twine>=4.0.2",
        ],
    },
    python_requires=">=3.10",
)
