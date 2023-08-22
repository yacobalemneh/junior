import torch
import whisper

# transcription_model.py
class TranscriptionModel:
    def __init__(self, config):
        self.config = config
        self.model = None

    def load(self, model_type = 'base.en'):
        print('Model type:', model_type)
        self.model = whisper.load_model(model_type)
        self.pad_audio = whisper.pad_or_trim

    
    def transcribe(self, audio):
        if self.model is None:
            self.load()
        audio = self.pad_audio(audio)
        return self.model.transcribe(audio, fp16=False, language='English')

