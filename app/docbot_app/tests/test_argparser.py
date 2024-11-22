import unittest
from unittest.mock import patch

from ..src.arg_parser import (
    parse_arguments,
)


class TestParseArguments(unittest.TestCase):
    # Test case for parsing arguments with models and files
    @patch("sys.argv", ["cli_tool.py", "file1.py", "--models", "model1"])
    def test_parse_arguments_with_files_and_models(self):
        args, toml_dict = parse_arguments()

        # Assert files are parsed correctly
        self.assertEqual(args.files, ["file1.py"])

        # Assert models are parsed correctly
        self.assertEqual(args.models, ["model1"])

        # Assert TOML config is empty
        self.assertEqual(toml_dict, {})

    # Test case with --token flag
    @patch("sys.argv", ["cli_tool.py", "file1.py", "--token", "--models", "model1"])
    def test_parse_arguments_with_token(self):
        args, toml_dict = parse_arguments()

        self.assertEqual(args.files, ["file1.py"])

        self.assertEqual(args.models, ["model1"])

        self.assertEqual(args.token, True)

        self.assertEqual(toml_dict, {})


if __name__ == "__main__":
    unittest.main()
