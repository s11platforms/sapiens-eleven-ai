from ..S11LargeLanguageModelProvider import S11LargeLanguageModelProvider
from S11AssistantsOpenAIProviderUtils import OPENAI, get_model, get_header, get_api_key


class S11AssistantsOpenAIProvider(S11LargeLanguageModelProvider):
    def __init__(self, tier: str):
        super().__init__(OPENAI, tier)
        self.api_key = get_api_key(self.tier)
        self.model = get_model(self.tier)
        self.header = get_header(self.api_key)

    def build_request(self, expert: str, prompt: str):
        header = build_message_header(prompt)
        header = build_tools(expert, header)
        self.header = header
    def get_response(self, str: expert):
        self.build_request()

        openai_response = self.execute_request()

        return handle_answer(openai_response)
