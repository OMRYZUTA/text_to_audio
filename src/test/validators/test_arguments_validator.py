import unittest
import sys
from src.engine.validators.arguments_validator import ArgumentsValidator


class ArgumentsValidatorTestCase(unittest.TestCase):
    def setUp(self):
        sys.argv = ["make_audio.py"]

    def test_when_not_getting_required_params_raises_runtime_error(self):
        self.assertRaises(RuntimeError, ArgumentsValidator().validate)

    def test_when_getting_required_params_does_not_raises(self):
        sys.argv.append("file1")
        sys.argv.append("file2")
        try:
            ArgumentsValidator().validate()
        except RuntimeError:
            self.fail("ArgumentsValidator().validate() raised RuntimeError unexpectedly!")


if __name__ == '__main__':
    unittest.main()
