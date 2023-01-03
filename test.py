import gptools.gptools as ai
import inspect


API_KEY_PATH = "/Users/alexthe5th/Documents/API Keys/OpenAI_API_key.txt"
ai.api_login(API_KEY_PATH)

"""
a sandbox for brainstorming interactions between the functions in gptools.functions and the OpenAI API

"""


def main():
    prompt = "write a blog post about a new beer release for a beer called 'bitch slap'. it is a double IPA being released " \
             "by 'fuck you brewing' in asheville north carolina on may 4th 2023. " \
             "the release will feature a performance by the psych folk band 'of the stars'"
    prompt_obj = ai.Prompt(prompt)
    text_obj = ai.Text(prompt_obj.generate_text())
    print(text_obj.original_text)
    print("-_-_-_-_-_-")
    refine_list = [
        "make it more interesting",
        "make it more engaging",
        "make the language and sentence structure varied and interesting",
        "make the tone jovial and funny"
        "make it grammatically correct",
    ]
    text_obj.refine(refine_list)
    print(text_obj.refined_text)
    # text_obj.check_list = [""]
    text_obj.check_refined()
    for check in text_obj.check_results:
        print(f"{check}: {text_obj.check_results[check]['result']}")










if __name__ == "__main__":
    main()