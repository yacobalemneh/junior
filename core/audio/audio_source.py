import speech_recognition as sr

class AudioSource:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        
    def record(self):
        with sr.Microphone() as microphone:
            self.recognizer.adjust_for_ambient_noise(microphone)
            return self.recognizer.record(microphone)

    def listen(self):
        with sr.Microphone() as microphone:
            self.recognizer.adjust_for_ambient_noise(microphone)
            return self.recognizer.listen(microphone)