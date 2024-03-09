from abc import ABC, abstractmethod

API_KEY = "S11API_Key"
PROMPT = "S11Prompt"
PROVIDER = "S11Provider"
ACCESS = "S11Access"
FULL_ACCESS = "S11Full_Access"
EXPERT = "S11Expert"
MEDICAL_EXPERT = "S11Medical_Expert"
MENTAL_HEALTH_EXPERT = "S11Mental_Health_Expert"
EXERCISE_EXPERT = "S11Exercise_Expert"
NUTRITION_EXPERT = "S11Nutrition_Expert"
SAPIEN_ELEVEN_EXPERT = "S11Sapien_Eleven_Expert"



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



