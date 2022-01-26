from gtts import *
import sys

NEEDED_ARGUMENTS = 3


def create_audio(file_path, result_file_name):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        txt = ''.join(lines)
        tts = gTTS(txt, lang='en', tld='ca')
        tts.save(result_file_name)
        print("finished")


def validate_arguments():
    if len(sys.argv) != NEEDED_ARGUMENTS:
        raise RuntimeError('invalid usage! usage = <text_file_path> <audio_file_name>')


def parse_arguments():
    return sys.argv[1], sys.argv[2]


if __name__ == "__main__":
    try:
        validate_arguments()
        (text_file_path, audio_file_name) = parse_arguments()
        create_audio(text_file_path, audio_file_name)
    except RuntimeError as e:
        print(e)
