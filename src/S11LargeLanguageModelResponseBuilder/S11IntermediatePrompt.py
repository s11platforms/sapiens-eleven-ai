class S11IntermediatePrompt:
    prompt: str
    complete: bool

    def __init__(self, prompt: str):
        self.prompt = prompt
        self.complete = False

    def is_complete(self) -> bool:
        return self.complete

    def prompt_is_complete(self):
        self.complete = True