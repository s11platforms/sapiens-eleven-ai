from typing import Tuple

import requests
import json
from ..LargeLanguageModelService import LargeLanguageModelService
from OpenAIServiceUtils import execute_chat_completions_api_request

class OpenAIService(LargeLanguageModelService):

    def getExpertResponse(self, payload: dict) -> tuple[dict, dict]:
        """
        Handles logic for Mixture of Experts (see designs folder for more info)
        :param payload: sent by client (front UI/UX)
        :return: Payload containing response to question/instruction
        """
        #TODO: add logic to make Mixture of Experts
        response = execute_chat_completions_api_request(payload, False)

        # TODO: form final payloads to send back to client
        return response

    def getSimpleResponse(self, payload: dict) -> tuple[dict, dict]:
        """
        Handles logic for Mixture of Experts (see designs folder for more info)
        :param payload: sent by client (front UI/UX)
        :return: Payload containing response to question/instruction
        """
        # TODO: add logic to make Mixture of Experts
        # TODO: form final payloads to send back to client
        response, function = execute_chat_completions_api_request(payload, True)
        return response