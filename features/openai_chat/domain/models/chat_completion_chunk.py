class ChatCompletionChunk:
    def __init__(self, id, object, created, model, choices, text='', token_estimate=0):
        self.id = id
        self.object = object
        self.created = created
        self.model = model
        self.choices = choices
        self.text = text
        self.token_estimate = token_estimate

class Delta:
    def __init__(self, content, role='assistant'):
        self.role = role
        self.content = content


class ChatStream:
    def __init__(self, text, total_tokens, chunk):
        self.text = text
        self.total_tokens = total_tokens
        self.chunk = chunk