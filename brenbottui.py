import os
import openai
import anthropic
import getpass
import json

class TextBasedChatBot:
    def __init__(self):
        self.system_message = "You are a friendly chatbot called BBot."
        self.conversation = []
        self.api_key = ""
        self.api_provider = ""
        self.model = ""
        self.initialize_api()

    def initialize_api(self):
        print("Welcome to BBot!")
        
        while True:
            provider_choice = input("Select API Provider:\n1. Anthropic\n2. OpenAI\nEnter 1 or 2: ").strip()
            if provider_choice == "1":
                self.api_provider = "anthropic"
                break
            elif provider_choice == "2":
                self.api_provider = "openai"
                break
            else:
                print("Invalid choice. Please enter 1 for Anthropic or 2 for OpenAI.")

        if self.api_provider == "anthropic":
            self.load_anthropic_api_key()
        else:
            key_input_method = input("Choose API key input method:\n1. Enter securely\n2. Read from file\nEnter 1 or 2: ").strip()

            if key_input_method == "1":
                self.api_key = getpass.getpass(f"Enter your OpenAI API key: ")
            elif key_input_method == "2":
                file_path = input("Enter the path to your API key file: ").strip()
                self.read_api_key_from_file(file_path)
            else:
                print("Invalid input. Please restart and choose a valid option.")
                exit(1)

        if self.api_provider == "openai":
            openai.api_key = self.api_key
            self.model = input("Enter OpenAI model (e.g., gpt-3.5-turbo): ").strip()
        elif self.api_provider == "anthropic":
            self.anthropic_client = anthropic.Client(api_key=self.api_key)
            self.model = input("Enter Anthropic model (e.g., claude-3-opus-20240229): ").strip()

    def load_anthropic_api_key(self):
        try:
            with open('apifile.json', 'r') as file:
                data = json.load(file)
                self.api_key = data.get("anthropic")
                if not self.api_key:
                    print("Anthropic API key not found in apifile.json.")
                    exit(1)
            print("Anthropic API key loaded successfully from apifile.json.")
        except FileNotFoundError:
            print("apifile.json not found in the current directory.")
            exit(1)
        except json.JSONDecodeError:
            print("Invalid JSON in apifile.json.")
            exit(1)

    def read_api_key_from_file(self, file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                self.api_key = data.get(self.api_provider)
                if not self.api_key:
                    print(f"API key for {self.api_provider} not found in the file.")
                    exit(1)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            exit(1)
        except json.JSONDecodeError:
            print(f"Invalid JSON in file: {file_path}")
            exit(1)

    def chat(self):
        print("\nChat started. Type 'quit' to exit.")
        while True:
            user_message = input("\nYou: ").strip()
            if user_message.lower() == 'quit':
                break

            if not self.conversation:
                self.conversation.append({"role": "system", "content": self.system_message})

            self.conversation.append({"role": "user", "content": user_message})
            self.get_ai_response(user_message)

    def get_ai_response(self, user_message):
        try:
            if self.api_provider == "openai":
                completion = openai.ChatCompletion.create(
                    model=self.model,
                    messages=self.conversation
                )
                ai_response = completion['choices'][0]['message']['content']
            elif self.api_provider == "anthropic":
                messages = [{"role": "user", "content": user_message}]
                completion = self.anthropic_client.messages.create(
                    model=self.model,
                    messages=messages,
                    max_tokens=1000
                )
                ai_response = completion.content[0].text if completion.content else "No response from AI."

            self.conversation.append({"role": "assistant", "content": ai_response})
            print(f"\nBBot: {ai_response}")
        except Exception as e:
            print(f"\nError: {str(e)}")

if __name__ == "__main__":
    chatbot = TextBasedChatBot()
    chatbot.chat()