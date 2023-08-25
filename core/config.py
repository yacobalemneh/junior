import json
import os

class Config:
    def __init__(self):
        self.hotwords = self.load_json('config/hotwords.json')
        self.responses = self.load_json('config/responses.json')
        self.LOGGING_LEVEL = os.environ.get('LOG_LEVEL', 'INFO').upper()

    def load_json(self, path):
        with open(path, 'r') as f:
            return json.load(f)