from google.cloud import texttospeech
from features.text_to_speech.azure.data.speech_config import SpeechConfig
from features.text_to_speech.text_to_speech import TextToSpeechService


class GoogleTextToSpeechService(TextToSpeechService):
    def __init__(self):
        self.client = texttospeech.TextToSpeechClient()

    def synthesize_speech(self, text, config=SpeechConfig()):
        input_text = texttospeech.SynthesisInput(text=text)
        voice = texttospeech.VoiceSelectionParams(
            language_code=config.language)
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3)

        response = self.client.synthesize_speech(
            input=input_text, voice=voice, audio_config=audio_config)

        # The response's audio_content is binary.
        with open("output.mp3", "wb") as out:
            out.write(response.audio_content)
            print('Audio content written to file "output.mp3"')
