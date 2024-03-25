
"""
CONSTANTS
"""
OPENAI = "openai"
GPT_4_TURBO = "gpt-4-0125-preview"
GPT_3_5_TURBO = "gpt-3.5-turbo-0125"
MODEL = "model"
MESSAGES = "messages"

def get_api_key(tier: str) -> str:
    if tier == 'priority':
        return GPT_4_TURBO
    else:
        return GPT_3_5_TURBO

def get_model(tier: str) -> str:
    return ""

def get_header(api_key: str) -> dict:
    return {}