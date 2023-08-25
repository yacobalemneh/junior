class ConversationInteractor:
    def __init__(self, conversation_service):
        self.conversation_service = conversation_service

    def start_conversation(self, audio_source, audio_processor):
        self.conversation_service.start_conversation(audio_source, audio_processor)