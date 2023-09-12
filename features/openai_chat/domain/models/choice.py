from features.openai_chat.domain.models.chat_completion_chunk import Delta
from features.openai_chat.domain.models.message import Message


class Choice:
    def __init__(self, finish_reason, index):
        self.finish_reason = finish_reason
        self.index = index


class ChunkChoice(Choice):
    def __init__(self, finish_reason, index, delta, output='', token_estimate=0):
        super().__init__(finish_reason, index)
        self.delta = delta
        self.output = output
        self.token_estimate = token_estimate

    @classmethod
    def from_dict(cls, data):
        finish_reason = data['finish_reason']
        index = data['index']
        content = data['delta']['content'] if 'content' in data['delta'] else ''
        delta = Delta(content)
        output = content
        # estimate the number of tokens as the number of words
        token_estimate = len(content.split())
        return cls(finish_reason, index, delta, output, token_estimate)


class NonChunkChoice(Choice):
    def __init__(self, finish_reason, index, message, text=''):
        super().__init__(finish_reason, index)
        self.message = message
        self.text = text

    @classmethod
    def from_dict(cls, data):
        finish_reason = data['finish_reason']
        index = data['index']
        message = Message(data['message']['role'], data['message']['content'])
        text = data['message']['content']
        return cls(finish_reason, index, message, text)
