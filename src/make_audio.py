from engine.validators.arguments_validator import ArgumentsValidator
from engine.parsers.cli_arguments_parser import CLIArgumentsParser
from engine.fetchers.text_fetcher import TextFetcher
from engine.audio_makers.gtts_audio_maker import GttsAudioMaker


if __name__ == "__main__":
    try:
        ArgumentsValidator().validate()
        (text_file_path, audio_file_name) = CLIArgumentsParser().parse()
        text = TextFetcher().fetch_from_path(text_file_path)
        GttsAudioMaker().create_audio_file_from_text(text, audio_file_name)

    except RuntimeError as e:
        print(e)
