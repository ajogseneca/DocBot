import sys
import unittest
from io import StringIO
from unittest.mock import patch

from DocBot import main, show_version


class TestShowVersion(unittest.TestCase):
    def test_show_version_output(self):
        # capture output of console
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the function with expected tool name and version
        show_version("DocBot", "0.3")

        # Reset stdout
        sys.stdout = sys.__stdout__

        # Assert that the output is as expected
        self.assertEqual(captured_output.getvalue().strip(), "DocBot, version 0.3")


class TestFileInput(unittest.TestCase):
    @patch("sys.stdout", new_callable=StringIO)
    @patch("sys.stderr", new_callable=StringIO)
    @patch("sys.argv", new=["docbot.py"])
    def test_no_files_provided(self, mock_stderr, mock_stdout):
        # Run the main function with no files provided
        with self.assertRaises(SystemExit):  # Expecting the program to exit
            main()

        # Check that the error message about missing files is printed to stderr
        error_message = mock_stderr.getvalue().strip()
        self.assertEqual(
            error_message, "error: the following arguments are required: file"
        )


if __name__ == "__main__":
    unittest.main()