from ..S11DatabaseService.S11DatabaseService import S11DatabaseService
from ..S11LargeLanguageModelProvider.S11LargeLanguageModelProvider import S11LargeLanguageModelProvider
from ..S11LargeLanguageModelServices.S11LargeLanguageModelService import S11LargeLanguageModelService

"""
FILE CONTENTS AND DESCRIPTION:

"""

"""
CONSTANTS
"""
USER = "S11User"
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


"""
FUNCTIONS
"""

"""
Instantiation utils functions
"""
# TODO: validate all part of the client payload
def validate_payload(payload: dict):
    return None

def get_database_service() -> S11DatabaseService:
    return S11DatabaseService()

def get_user_record(user: str, database_service: S11DatabaseService) -> dict:
    return {

    }

def get_current_utc_date_time() -> str:
    return ""

def get_expert(prompt: str) -> str:
    return ""

def get_provider(user: dict, access: str) -> S11LargeLanguageModelProvider:
    return S11LargeLanguageModelProvider()

def build_error_payload(error_type: Exception, llm_service: S11LargeLanguageModelService) -> dict:
    return

"""
get_response() utils functions
"""
def build_client_payload(llm_service: S11LargeLanguageModelService) -> dict:
    return {

    }

def get_request_cost() -> float:
    return 0.0