from abc import ABC, abstractmethod
class S11LargeLanguageModelProvider(ABC):
    type: str
    prompt: str
    request_payload_builder: OpenAIRequestBuilder
    request: dict
    openai_api_key: str
    model: str

    def __init__(self, ):
    def get_exepert_response(self):
        return None