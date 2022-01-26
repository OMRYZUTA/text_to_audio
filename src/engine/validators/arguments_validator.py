import sys


class ArgumentsValidator:
    REQUIRED_ARGUMENTS = 3

    def validate(self):
        if len(sys.argv) != self.REQUIRED_ARGUMENTS:
            raise RuntimeError('invalid usage! usage = <text_file_path> <audio_file_name>')
