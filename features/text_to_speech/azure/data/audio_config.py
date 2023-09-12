class AudioConfig:
    def __init__(self, use_default_speaker=True, filename=None, stream=None, device_name=None):
        self.use_default_speaker = use_default_speaker
        self.filename = filename
        self.stream = stream
        self.device_name = device_name