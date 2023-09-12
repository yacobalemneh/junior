class ChatCompletionResponse:
    def __init__(self, choices, created, id, model, object, usage, text=''):
        self.choices = choices
        self.created = created
        self.id = id
        self.model = model
        self.object = object
        self.usage = usage
        self.text = text