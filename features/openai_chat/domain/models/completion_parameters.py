class CompletionParameters:
    def __init__(self, temperature=0.7, max_tokens=100, frequency_penalty=0.0):
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.frequency_penalty = frequency_penalty