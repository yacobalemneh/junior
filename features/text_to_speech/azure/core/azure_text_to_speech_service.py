import azure.cognitiveservices.speech as speechsdk
from features.text_to_speech.azure.data.speech_config import SpeechConfig
from features.text_to_speech.text_to_speech import TextToSpeechService
from infrastructure.utils.api_key_provider import ApiKeyProvider


class AzureTextToSpeechService(TextToSpeechService):
    def __init__(self, key_provider: ApiKeyProvider):
        self.speech_config = speechsdk.SpeechConfig(subscription=key_provider.get_key(
            'AZURE_SPEECH_KEY'), region=key_provider.get_key('AZURE_SPEECH_REGION'))

    def set_audio_output_to_default_speaker(self):
        self.audio_config = speechsdk.audio.AudioOutputConfig(
            use_default_speaker=True)

    def set_audio_output_to_file(self, filename):
        self.audio_config = speechsdk.audio.AudioOutputConfig(
            filename=filename)

    def set_audio_output_to_stream(self, stream):
        self.audio_config = speechsdk.audio.AudioOutputConfig(stream=stream)

    def set_audio_output_to_device(self, device_name):
        self.audio_config = speechsdk.audio.AudioOutputConfig(
            device_name=device_name)

    def synthesize_speech(self, text, config=SpeechConfig()):
        self.speech_config.speech_synthesis_voice_name = config.voice
        self.speech_synthesizer = speechsdk.SpeechSynthesizer(
            speech_config=self.speech_config, audio_config=self.audio_config)
        speech_synthesis_result = self.speech_synthesizer.speak_text_async(
            text).get()
        if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("Speech synthesized for text [{}]".format(text))
        elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_synthesis_result.cancellation_details
            print("Speech synthesis canceled: {}".format(
                cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    print("Error details: {}".format(
                        cancellation_details.error_details))
                    print("Did you set the speech resource key and region values?")

    def synthesize_speech_from_ssml(self, ssml, config=SpeechConfig()):
        self.speech_config.speech_synthesis_voice_name = config.voice
        self.speech_synthesizer = speechsdk.SpeechSynthesizer(
            speech_config=self.speech_config, audio_config=self.audio_config)
        speech_synthesis_result = self.speech_synthesizer.speak_ssml_async(
            ssml).get()
        if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            print("Speech synthesized for SSML [{}]".format(ssml))
        elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_synthesis_result.cancellation_details
            print("Speech synthesis canceled: {}".format(
                cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    print("Error details: {}".format(
                        cancellation_details.error_details))
                    print("Did you set the speech resource key and region values?")
