from abc import ABC, abstractmethod
from S11LargeLanguageModelProviderUtils import get_model, get_api_key, get_header
class S11LargeLanguageModelProvider(ABC):
    llm_provider: str
    tier: str
    api_key: str
    model: str
    header: dict
    request: dict

    def __init__(self, llm_provider: str, tier:str):
        self.llm_provider = llm_provider
        self.tier = tier


    @abstractmethod
    def get_response(self, expert: str, prompt: str) -> dict:
        # Build Header with prompt and expert

        # Execute request

        # Return input tokens, output tokens and answer or function
        return {}