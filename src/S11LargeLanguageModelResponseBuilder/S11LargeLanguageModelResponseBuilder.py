from S11LargeLanguageModelResponseBuilderUtils import generate_intermediate_prompts
from S11IntermediatePrompt import S11IntermediatePrompt
class S11LargeLanguageModelResponseBuilder:
    initial_prompt: str
    intermediate_prompts: list[S11IntermediatePrompt]
    final_responses: list[str]
    synthesized_response: str

    def __init__(self, prompt: str):
        self.initial_prompt = prompt
        self.intermediate_prompts = generate_intermediate_prompts()
        self.final_responses = list()
        self.synthesized_response = ""

    def intermediate_prompts_complete(self):
        counter = 0
        for i in self.intermediate_prompts:
            if i.is_complete():
                counter += 1

        return counter == len(self.intermediate_prompts)

    def synthesized_response_is_complete(self):
        return self.synthesized_response != ""