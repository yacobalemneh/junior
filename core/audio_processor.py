
import numpy as np
import speech_recognition as sr
from scipy.io import wavfile
from io import BytesIO
# utils.py
from core.services.state import State

class AudioProcessor:
    def __init__(self, hotwords, config, hotword_detector, transcription_service):
        self.hotwords = hotwords
        self.hotword_detector = hotword_detector
        self.transcription_service = transcription_service
        self.r = sr.Recognizer()
        self.m = sr.Microphone()
        with self.m as source:
            self.r.adjust_for_ambient_noise(source)

    def callback(self, recognizer, audio_data, mode="raw"):
        if mode == "raw":
            audio_array = np.frombuffer(audio_data, np.int16).astype(np.float32) / 32768.0
        elif mode == "wav":
            sample_rate, audio_array = wavfile.read(BytesIO(audio_data))
            audio_array = audio_array.astype(np.float32) / 32768.0 if audio_array.dtype == np.int16 else audio_array.astype(np.float32)

        if self.hotword_detector.task_manager.current_state == State.IDLE:
            self.hotword_detector.detect(audio_array)
        elif self.hotword_detector.task_manager.current_state == State.LISTENING:
            transcription = self.transcription_service.transcribe(audio_array)
            print(f"Transcription: {transcription}")
            if any(word in transcription for word in self.hotwords):
                print(f"Hot word detected: {transcription}")

    def listen(self, mode="raw"):
        try:
            with self.m as source:
                while True:  # Continuous loop for listening
                    print(f'Listening... State: {self.h}')  # Optionally, print a message indicating that the system is ready to listen
                    audio = self.r.listen(source)
                    if mode == "raw":
                        audio_data = audio.get_raw_data(convert_rate=16000, convert_width=2)
                    elif mode == "wav":
                        audio_data = audio.get_wav_data(convert_rate=16000, convert_width=2)

                    self.callback(self.r, audio_data, mode)  # Pass the processed data to the callback
        except KeyboardInterrupt:  # Allow for a graceful exit with a keyboard interrupt
            print("Listening stopped")

