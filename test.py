import gptools.gptools as ai
import datetime


API_KEY_PATH = "/Users/alexthe5th/Documents/API Keys/OpenAI_API_key.txt"
ai.api_login(API_KEY_PATH)

"""
a sandbox for brainstorming interactions between the functions in gptools.functions and the OpenAI API

"""


def main():
    delim = "\n~~~~~~~~~~~~~~\n"
    prompt = "an article about the history of music"
    prompt_obj = ai.Prompt(prompt)
    text_obj = ai.Text(prompt_obj.generate_text())
    print(text_obj.original_text, delim)
    text_obj.summarize()
    print(text_obj.summary, delim)
    text_obj.elaborate()
    print(text_obj.elaboration, delim)
    text_obj.analyze("about animals")
    print(text_obj.analysis, delim)
    text_obj.criticize("good engaging writing", 3)
    print(text_obj.critiques, delim)
    for critique in text_obj.critiques:
        print(critique, delim)
        print(text_obj.refine(critique), delim)
    print(text_obj.refined_text, delim)
    text_obj.get_outline(10)
    print(text_obj.outline, delim)
    text_obj.get_questions(10)
    print(text_obj.questions, delim)
    text_obj.restyle("like a journal entry, written by a 12 year old")
    print(text_obj.refined_text, delim)
    text_obj.analyze_sentiment()
    print(text_obj.sentiment, delim)
    text_obj.get_title("an article")
    print(text_obj.title, delim)















if __name__ == "__main__":
    main()