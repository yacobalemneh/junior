import os
from dotenv import load_dotenv
from infrastructure.utils.api_key_provider import ApiKeyProvider


class EnvApiKeyProvider(ApiKeyProvider):
    def __init__(self):
        load_dotenv("../.env")  # load the .env file from the parent directory

    def get_key(self, key_name):
        return os.getenv(key_name)
