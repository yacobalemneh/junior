import json
from features.openai_chat.domain.models.chat_completion_chunk import ChatStream

from features.openai_chat.domain.models.choice import ChunkChoice, NonChunkChoice


class ChatResponseHandler:
    def __init__(self, response, config):
        self.response = response
        self.config = config
        self.text = ''
        self.total_tokens = 0

    def handle_response(self):
        if self.config.response_type == 'stream':
            return self._handle_chunked_response()
        else:
            return self._handle_non_chunked_response()

    def stream_text(self):
        for chunk in self.response:
            choices = [ChunkChoice.from_dict(choice)
                       for choice in chunk['choices']]
            data = choices[-1]  # Get the last choice
            self.text += data.output
            self.total_tokens += data.token_estimate
            # Yield a ChatStream object
            yield ChatStream(self.text, self.total_tokens, chunk)

    def _handle_chunked_response(self):
        return self.stream_text()  # Return the generator function

    def _handle_non_chunked_response(self):
        choices = [NonChunkChoice.from_dict(choice)
                   for choice in self.response['choices']]
        self.text = choices[0].text if choices else ''
        self.usage = self.response['usage']
        self.total_tokens = None
        return self  # Return self instead of chunks
