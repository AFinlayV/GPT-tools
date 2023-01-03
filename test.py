import gptools.gptools as ai
import datetime


API_KEY_PATH = "/Users/alexthe5th/Documents/API Keys/OpenAI_API_key.txt"
ai.api_login(API_KEY_PATH)

"""
a sandbox for brainstorming interactions between the functions in gptools.functions and the OpenAI API

"""


def main():
    prompt = ""
    prompt_obj = ai.Prompt(prompt)
    check_prompt = prompt_obj.check()
    for check in check_prompt:
        print(f"{check}: {check_prompt[check]['result']}\nExplanation: {check_prompt[check]['evaluation']}\n")
    text_obj = ai.Text(prompt_obj.generate_text())
    print(text_obj.original_text)











if __name__ == "__main__":
    main()