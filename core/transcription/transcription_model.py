import whisper
from core.transcription.transcription_data_class import TranscriptionResult


class TranscriptionModel:
  def __init__(self, config):
    self.config = config
    self.model = None
    self.model_type = None
    self.pad_audio = whisper.pad_or_trim

  def load(self, model_type):
    if model_type != self.model_type:
      print('Model type:', model_type)
      self.model = whisper.load_model(model_type)
      self.model_type = model_type

  def transcribe(self, audio):
    if self.model is None:
        raise ValueError("Model not loaded.")
    audio = self.pad_audio(audio)
    result_dict = self.model.transcribe(audio, fp16=False, language='English')
    result = TranscriptionResult.from_dict(result_dict)
    return result