from gtts import *
from engine.validators.arguments_validator import ArgumentsValidator


def create_audio(file_path, result_file_name):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        txt = ''.join(lines)
        tts = gTTS(txt, lang='en', tld='ca')
        tts.save(result_file_name)
        print("finished")




def parse_arguments():
    return sys.argv[1], sys.argv[2]


if __name__ == "__main__":
    try:
        ArgumentsValidator().validate()
        (text_file_path, audio_file_name) = parse_arguments()
        create_audio(text_file_path, audio_file_name)
    except RuntimeError as e:
        print(e)
