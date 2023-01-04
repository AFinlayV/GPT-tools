import gptools.gptools as ai

API_KEY_PATH = "/Users/alexthe5th/Documents/API Keys/OpenAI_API_key.txt"
ai.api_login(API_KEY_PATH)

"""
a sandbox for brainstorming interactions between the functions and classes in gptools.py

"""


def this_thing():
    topic_list = ai.generate_list("unusual subjects for children's stories", 3)
    for topic in topic_list:
        print(topic)
        gpt_prompt = ai.GPTprompt()
        gpt_prompt.prompt = f"write children's storybook about {topic}"
        gpt_text = ai.GPTtext()
        gpt_text.text = gpt_prompt.generate_text()
        print(gpt_text.text)
        gpt_text.title_type = "children's storybook"
        gpt_text.get_meta()
        for key in gpt_text.meta:
            print(f"{key}:\n {gpt_text.meta[key]}")
        print(f"\n~~~~~~new {gpt_text.title_type}~~~~~~~~\n")
        gpt_text.save(f"text/{gpt_text.title}.txt")


def main():
    """
    test the methods in ai.GPTtext object
    """
    story = ai.Story()
    story.plot = "a cute dog goes on an adventure"
    story.genre = "children's storybook"
    story.get_story_prompt()
    story.get_story()
    story.get_meta()
    print(story.text)
    for key in story.meta:
        print(f"{key}:\n {story.meta[key]}")
    print(story.critiques)

    print(story.refined_text.text)


if __name__ == "__main__":
    main()
