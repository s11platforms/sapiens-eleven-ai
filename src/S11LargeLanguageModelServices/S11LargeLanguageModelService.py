"""
IMPORTS
"""
# Import Classes
from ..S11LargeLanguageModelProvider.S11LargeLanguageModelProvider import S11LargeLanguageModelProvider
from ..S11DatabaseService.S11DatabaseService import S11DatabaseService

# Import Utils functions
from S11LargeLanguageModelServiceUtils import (validate_payload, get_expert, get_provider, get_current_utc_date_time
                                               , get_database_service, get_user_record, build_client_payload, build_error_payload)

# Import Utils Constants
from S11LargeLanguageModelServiceUtils import USER, PROMPT, API_KEY, ACCESS
from ..S11DatabaseService.S11DatabaseServiceUtils import MESSAGES_TABLE

"""
S11LargeLanguageModelService CLASS DESCRIPTION:

"""
class S11LargeLanguageModelService:
    prompt: str
    user: dict
    provider: S11LargeLanguageModelProvider
    initial_request_time: str
    final_request_time: str
    request_time: str
    response_time: str
    api_key: str
    access: str
    expert: str
    request_payload: dict
    answer: str
    input_token_usage: int
    output_token_usage: int
    usage_cost: float
    database_service: S11DatabaseService

    def __init__(self, payload: dict):
        try:
            # Validate Payload First (Make sure everything is in order)
            validate_payload(payload)

            # class members populated by Client Payload
            self.request_payload = payload
            self.database_service = get_database_service()
            self.user = get_user_record(payload.get(USER), self.database_service)
            self.prompt = payload.get(PROMPT)

            # class members populated by Utils methods
            self.initial_request_time = get_current_utc_date_time()
            self.api_key = self.user.get(API_KEY)
            self.access = self.user.get(ACCESS)
            self.expert = get_expert(self.prompt)

            # class members population depends on other Utils provided class members
            self.provider = get_provider(self.user, self.access)

            # class members populated after response
            self.request_time = "None"
            self.response_time = "None"
            self.answer = "None"
            self.final_request_time = "None"
            self.input_token_usage = 0
            self.output_token_usage = 0
            self.usage_cost = 0.0

        except Exception as e:
            # TODO: define Instantiation exception to take in specific exceptions for others and wrap them
            print("Error")



    def get_response(self) -> dict:
        """

        :return:
        """
        # Get time stamp right before we make a request (used for analytics later)
        self.request_time = get_current_utc_date_time()
        try:
            self.answer, self.input_token_usage, self.output_token_usage \
                = self.provider.get_exepert_response()
        except Exception as e:
            # TODO: error handling
            print("Error")
            return build_error_payload(e, self)

        # Get time stamp right after we make a request (used for analytics later)
        self.response_time = get_current_utc_date_time()

        # TODO: save request and answer in DB
        try:
            self.database_service.save(self, MESSAGES_TABLE)
        except Exception as e:
            # TODO: error handling
            print("Error")
            return build_error_payload(e, self)

        return build_client_payload(self)