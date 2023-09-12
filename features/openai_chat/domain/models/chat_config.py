class ChatConfig:
    def __init__(self, model='gpt-3.5-turbo', response_type='stream'):
        self.model = model
        self.response_type = response_type