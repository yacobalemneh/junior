import numpy as np
from scipy.io import wavfile
from io import BytesIO

class AudioProcessor:
    @staticmethod
    def process(audio, mode="raw"):
        if mode == "raw":
            audio_data = audio.get_raw_data(convert_rate=16000, convert_width=2)
            audio_array = np.frombuffer(audio_data, np.int16).astype(np.float32) / 32768.0
        elif mode == "wav":
            audio_data = audio.get_wav_data(convert_rate=16000, convert_width=2)
            sample_rate, audio_array = wavfile.read(BytesIO(audio_data))
            audio_array = audio_array.astype(np.float32) / 32768.0 if audio_array.dtype == np.int16 else audio_array.astype(np.float32)
        return audio_array