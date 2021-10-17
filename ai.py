import os
import openai


class Conversation:
    def __init__(self, engine: str, temperature: str):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.engine = engine
        self.temperature = temperature
        self.existing_conversation = ""

    @classmethod
    def continue_conversation(self, input_text: str):
        self.existing_conversation += "Human: " + input_text + "\n"

        start_sequence = "\nAI:"
        restart_sequence = "\nHuman: "

        input_prompt = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\n" + self.existing_conversation + "AI: "

        response_data = openai.Completion.create(
            engine=self.engine,
            temperature=self.temperature,
            max_tokens=64,
            prompt=input_prompt,
            stop=["\n", " Human:", " AI:"]
        )

        response = "AI: " + response_data["choices"][0]["text"] + "\n"

        self.existing_conversation += response
        return response
