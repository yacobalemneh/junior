import openai
from features.openai_chat.data.chat_response_handler import ChatResponseHandler
from features.openai_chat.domain.chat_service import ChatService
from features.openai_chat.domain.models.chat_config import ChatConfig
from features.openai_chat.domain.models.completion_parameters import CompletionParameters

from infrastructure.utils.api_key_provider import ApiKeyProvider


class OpenAIChatService(ChatService):
    def __init__(self, key_provider: ApiKeyProvider):
        openai.api_key = key_provider.get_key("OPENAI_API_KEY")

    def create_chat(self, messages, config=ChatConfig(), parameters=CompletionParameters()):
        response = openai.ChatCompletion.create(
            model=config.model,
            messages=[message.__dict__ for message in messages],
            stream=config.response_type == 'stream',
            **parameters.__dict__
        )
        handler = ChatResponseHandler(response, config)
        return handler.handle_response()
