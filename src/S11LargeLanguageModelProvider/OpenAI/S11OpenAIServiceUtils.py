import requests
from requests import Response

from src.S11LargeLanguageModelProvider.LargeLanguageModelService import EXPERT, PROMPT, ACCESS, FULL_ACCESS, MEDICAL_EXPERT, NUTRITION_EXPERT, EXERCISE_EXPERT, MENTAL_HEALTH_EXPERT, SAPIEN_ELEVEN_EXPERT, API_KEY

# TODO: Implement this as a builder class

# TODO: Implement the assistants api and the RAG service


"""
CONSTANTS
"""
GPT_4_TURBO = "gpt-4-0125-preview"
GPT_3_5_TURBO = "gpt-3.5-turbo-0125"
MODEL = "model"
MESSAGES = "messages"

def getModel(access: str) -> str:
    """
    :param access: str representing the level
    :return: str for the desired OpenAIModel based on access
    """
    if access == FULL_ACCESS:
        return GPT_4_TURBO
    else:
        return GPT_3_5_TURBO

def getTools(expert: str) -> dict:
    """
    :param expert: based on the expert (medical, nutrition... etc.) we will have different tools
    :return: JSON/dictionary (python) for the tools argument of the OpenAI payload
             ** contains the different functions we defined for function calling **
    """
    # TODO: make tools for each
    if expert == MEDICAL_EXPERT:
        return {

        }
    elif expert == MENTAL_HEALTH_EXPERT:
        return {

        }
    elif expert == NUTRITION_EXPERT:
        return {

        }
    elif expert == EXERCISE_EXPERT:
        return {

        }
    elif expert == SAPIEN_ELEVEN_EXPERT:
        return {

        }

def getToolChoice(expert: str) -> dict:
    """
    :param expert: based on the expert (medical, nutrition... etc.) we will have different tool choices
    :return: JSON/dictionary (python) for the tools argument of the OpenAI payload
             ** contains the different functions we defined for function calling **
    """
    # TODO: create a payload that is exactly like the tools choice
    return {

    }

def isSapienElevenCall(expert: str) -> bool:
    """
    The Sapiens 11 Expert needs to redirect the questions to our other Sapiens 11 Experts,
    not answer questions or follow instructions. Therefore, we will need to know if the
    question needs re-directing, or if it needs to be answered
    :param expert: used to identify if it is the Sapiens 11 Expert
    :return: bool: (1) True if the expert is Sapiens 11
                   (2) False if the expert is not Sapiens 11
    """
    return expert == SAPIEN_ELEVEN_EXPERT

def getPrompt(prompt: str) -> str:
    """
    Eventually, I plan on including RAG (Retrival Augmented Generation - for more info
    look in the designs' folder)
    :param prompt:
    :return: str for the composed prompt
    """
    # TODO: RAG Service
    return prompt

def getAPIKey(api_key: str, model: str) -> str:
    """
    Based on their API_key and the model they are trying to use,
    we can get them their OpenAI Api Key
    :param api_key: their Sapiens 11 API Key
    :param model: needed to see what API Key we offer them
    :return: str containing the OpenAI API Key
    """
    # TODO: Use their API_KEY to search for the api_key for the model they want to use
    return api_key

def getContext(expert: str) -> str:
    return "You are a helpful assistant."


def buildJSONPayload(payload: dict) -> dict:
    """

    :param payload:
    :return:
    """
    messagesList = [
        {"role": "system", "content": getContext(payload.get(EXPERT))},
        {"role": "user", "content": getPrompt(payload.get(PROMPT))}
    ]

    OpenAIPayload = {
        MODEL: getModel(payload.get(ACCESS)),
        MESSAGES: messagesList
    }

    tools = getTools(payload.get(EXPERT))
    if tools is not None:
        OpenAIPayload.update({"tools": tools})

    tool_choice = getToolChoice(payload.get(EXPERT))
    if tool_choice is not None:
        OpenAIPayload.update({"tool_choice": tool_choice})

    return OpenAIPayload

def buildHeadersPayload(api_key: str):
    return {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + api_key,
    }


def execute_chat_completions_api_request(payload: dict, simple: bool) -> str:
    """

    :param payload:
    :return:
    """
    response = execute_http_request(
        buildHeadersPayload(payload.get(API_KEY)),
        buildJSONPayload(payload)
    ).json()

    # TODO: add functionality to check if function_call (tools_call) is in response to execute the function
    # response.get('choices')[0].get('message').get('tool_calls')[0].get("function").get("arguments"), \
    # response.json().get('choices')[0].get('message').get('tool_calls')[0].get("function").get("name")

    # TODO: add token usage to payload

    # TODO: store response with payload in DB

    return response.get("choices")[0].get("message").get("content")




def execute_http_request(headers: dict, json: dict) -> Response:
    try:
        return requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=json,
        )

    except Exception as e:
        # TODO: Make the exception handling better
        print("Unable to generate ChatCompletion response")
        print(f"Exception: {e}")
        return "Error", ""