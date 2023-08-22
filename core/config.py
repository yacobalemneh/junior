import json

class Config:
    def __init__(self):
        self.config = {}
        self.load()

    def load(self):
        with open('config/hotwords.json', 'r') as f:
            self.config['hotwords'] = json.load(f)
        with open('config/responses.json', 'r') as f:
            self.config['responses'] = json.load(f)

    def get(self, key, default=None):
        return self.config.get(key, default)