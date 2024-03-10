from abc import ABC, abstractmethod





class LargeLanguageModelService(ABC):

    @abstractmethod
    def getExpertResponse(self, payload) -> dict:
        """
        Sends a request to the language model to generate a response based on the input messages.
        """
        pass

    @abstractmethod
    def getSimpleResponse(self, payload) -> dict:
        """
        Sends a request to the language model to generate a response based on the input messages.
        """
        pass



