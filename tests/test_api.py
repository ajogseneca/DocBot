import unittest
from io import StringIO
from unittest.mock import MagicMock, patch

from app.api import generate_readme


class TestGenerateReadme(unittest.TestCase):
    @patch("api.Groq")  # Patched path to GorqAI
    def test_generate_readme_with_mocked_api(self, MockGroq):
        # Mocking the Groq client and chat completions
        mock_client = MagicMock()
        MockGroq.return_value = mock_client

        # Mocking the chat completion response
        mock_chat_completion = MagicMock()
        mock_chat_completion.choices = [
            MagicMock(message=MagicMock(content="README content generated"))
        ]
        mock_client.chat.completions.create.return_value = mock_chat_completion

        # Input parameters for the function
        source_file = "test_code.py"
        output_file = None
        models = ["llama3-8b-8192"]

        # Running the generate_readme function with the mock objects
        with patch("builtins.open", unittest.mock.mock_open(read_data="Sample code")):
            with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                generate_readme(source_file, output_file, models)

                # Check if the output was printed to stdout
                output = mock_stdout.getvalue().strip()
                self.assertIn("README FILE (Model: llama3-8b-8192)", output)
                self.assertIn("README content generated", output)

    @patch("api.Groq")
    def test_generate_readme_with_missing_file(self, MockGroq):
        # Mocking the Groq client and chat completions
        mock_client = MagicMock()
        MockGroq.return_value = mock_client

        # Simulating a missing file scenario with the mock objects
        with patch("builtins.open", side_effect=FileNotFoundError):
            with patch("sys.stderr", new_callable=StringIO) as mock_stderr:
                with self.assertRaises(SystemExit):
                    generate_readme("nonexistent_file.py")

                # Check that the error message is printed to stderr
                error_message = mock_stderr.getvalue().strip()
                self.assertIn(
                    "Error: Source file nonexistent_file.py not found.", error_message
                )


if __name__ == "__main__":
    unittest.main()
