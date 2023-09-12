class TranscriptionInteractor:
    def __init__(self, transcription_service):
        self.transcription_service = transcription_service

    def transcribe(self, audio):
        return self.transcription_service.transcribe(audio)
