import gptools.gptools as ai

API_KEY_PATH = "/Users/alexthe5th/Documents/API Keys/OpenAI_API_key.txt"
ai.api_login(API_KEY_PATH)

"""
a sandbox for brainstorming interactions between the functions and classes in gptools.py

"""


def main():
    """
    test the methods in ai.GPTtext object
    """
    topic_list = ai.generate_list("unusual subjects for song lyrics", 2)
    for topic in topic_list:
        print(topic)
        gpt_prompt = ai.GPTprompt(f"write song about {topic}")
        gpt_text = ai.GPTtext(gpt_prompt.generate_text())
        print(gpt_text.original_text)
        gpt_text.title_type = "song"
        gpt_text.get_meta()
        for key in gpt_text.meta:
            print(f"{key}:\n {gpt_text.meta[key]})
        print(f"\n~~~~~~NEW {gpt_text.title_type}~~~~~~~~\n")
        gpt_text.save(f"text/{gpt_text.title}.txt")


if __name__ == "__main__":
    main()
