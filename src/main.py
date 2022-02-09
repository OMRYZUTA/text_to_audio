from src.engine.audio_creation.audio_creator import AudioCreator
from engine.validators.arguments_validator import ArgumentsValidator
from engine.parsers.arguments_parser import ArgumentsParser

if __name__ == "__main__":
    try:
        ArgumentsValidator().validate()
        (text_file_path, audio_file_name) = ArgumentsParser().parse()
        AudioCreator.create(text_file_path, audio_file_name)
    except RuntimeError as e:
        print(e)
