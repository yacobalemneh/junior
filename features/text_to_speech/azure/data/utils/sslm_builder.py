class SSMLBuilder:
    def __init__(self):
        self.ssml = "<speak>"

    def add_text(self, text):
        self.ssml += text
        return self

    def add_break(self, strength=None, time=None):
        # implementation goes here
        pass

    # add more methods for each SSML element and attribute

    def build(self):
        self.ssml += "</speak>"
        return self.ssml