import gptools.gptools as ai

API_KEY_PATH = "/Users/alexthe5th/Documents/API Keys/OpenAI_API_key.txt"
ai.api_login(API_KEY_PATH)

"""
a sandbox for brainstorming interactions between the functions in gptools.functions and the OpenAI API

"""


def main():
    """
    test the methods in ai.GPTtext object
    """

    topic_list = ai.generate_list("good subjects for sitcom pitches", 5)
    for topic in topic_list:
        print(topic)
        gpt_prompt = ai.GPTprompt(f"write sitcom pitch about {topic}")
        gpt_text = ai.GPTtext(gpt_prompt.generate_text())
        print(gpt_text.original_text)
        gpt_text.title_type = "sitcom"
        gpt_text.get_meta()
        for key in gpt_text.meta:
            print(key, gpt_text.meta[key])
        print("~~~~~~NEW TOPIC~~~~~~~~")
        gpt_text.save(f"text/{gpt_text.title}.txt")


if __name__ == "__main__":
    main()
