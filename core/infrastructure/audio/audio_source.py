import numpy as np
import speech_recognition as sr
import pyaudio
import queue

class AudioSource:
    def __init__(self, rate=16000, channels=1, format=pyaudio.paInt16, frames_per_buffer_duration=1):
        self.p = pyaudio.PyAudio()
        self.rate = rate
        self.format = format
        self.frames_per_buffer = self.seconds_to_frames(frames_per_buffer_duration, rate)
        self.stream = self.p.open(rate=rate, channels=channels, format=format, input=True, frames_per_buffer=self.frames_per_buffer, stream_callback=self.callback)
        self.audio_queue = queue.Queue()
        self.buffer = np.array([], dtype=np.int16)  # buffer to store the entire recording
        self.processing_buffer = np.zeros(self.frames_per_buffer, dtype=np.int16)  # buffer for the segment to be processed

    def callback(self, in_data, frame_count, time_info, status):
        chunk = np.frombuffer(in_data, np.int16)
        self.buffer = np.concatenate((self.buffer, chunk))
        self.processing_buffer = np.roll(self.processing_buffer, -len(chunk))
        self.processing_buffer[-len(chunk):] = chunk
        self.audio_queue.put(self.processing_buffer)
        return (None, pyaudio.paContinue)

    def start_stream(self):
        self.stream.start_stream()

    def stop_stream(self):
        self.stream.stop_stream()

    def terminate(self):
        self.stream.close()
        self.p.terminate()

    @staticmethod
    def seconds_to_frames(seconds, sample_rate):
        return int(seconds * sample_rate)