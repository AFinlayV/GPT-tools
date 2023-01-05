import gptools.gptools as ai
import json

API_KEY_PATH = "/Users/alexthe5th/Documents/API Keys/OpenAI_API_key.txt"
ai.api_login(API_KEY_PATH)

"""
a sandbox for brainstorming interactions between the functions and classes in gptools.py

"""


# def this_thing():
#     topic_list = ai.generate_list("unusual subjects for children's stories", 3)
#     for topic in topic_list:
#         print(topic)
#         gpt_prompt = ai.GPTprompt()
#         gpt_prompt.prompt = f"write children's storybook about {topic}"
#         gpt_text = ai.GPTtext()
#         gpt_text.text = gpt_prompt.generate_text()
#         print(gpt_text.text)
#         gpt_text.title_type = "children's storybook"
#         gpt_text.get_meta()
#         for key in gpt_text.meta:
#             print(f"{key}:\n {gpt_text.meta[key]}")
#         print(f"\n~~~~~~new {gpt_text.title_type}~~~~~~~~\n")
#         gpt_text.save(f"text/{gpt_text.title}.txt")
#  def that_thing():
#      """
#          test the methods in ai.GPTtext object
#          """
#      story = ai.Story()
#      story.plot = "a cute dog goes on an adventure"
#      story.genre = "children's storybook"
#      story.get_story_prompt()
#      story.get_story()
#      story.get_meta()
#      print(story.text)
#      for key in story.meta:
#          print(f"{key}:\n {story.meta[key]}")
#      story.refined_text = story.text
#      for critique in story.critiques:
#          story.refined_text = ai.refine_text(story.refined_text, critique)
#          print(f"\nCritique: \n\n {critique} \n New Draft of Story:\n\n {story.refined_text}")

# def summary_test():
#     prompt = ai.GPTprompt()
#     try:
#         text = ai.load_text("essay.txt")
#     except Exception as e:
#         text = ""
#         print(f"text not found: {e}, generating new text")
#         prompt.prompt = f"write a 3000 word essay about the history of the computers. " \
#                         f"make it as close to 3000 words as possible, even if that means repeating some information"
#         text += prompt.generate_text()
#         print(text)
#
#         prompt.prompt = f"write a 3000 word essay about the history of the internet. " \
#                         f"make it as close to 3000 words as possible, even if that means repeating some information"
#         text += prompt.generate_text()
#         print(text)
#         ai.save_text(text, "essay.txt")
#     # prompt.prompt = "write a 3000 word essay about the history of the AI"
#     # text += prompt.generate_text()
#     # print(text)
#     # prompt.prompt = "write a 3000 word essay about the history of the western civilization"
#     # text += prompt.generate_text()
#     # print(text)
#     print(f"text is {ai.num_tokens(text)} tokens long\n")
#     print(text)
#     print(f"summarizing text...")
#     summary = ai.generate_summary(text,
#                                   summary_tokens=100,
#                                   max_tokens=2000,
#                                   summary_topic="the specific dates mentioned in the essay")
#     print(f"summary is {ai.num_tokens(summary)} tokens")
#     print(summary)

def main():
    """
    test the prompt constructor in the GPTprompt class, and the GPTidentity class

    """
    bill = ai.GPTidentity(name="Bill")
    bill.generate_description(details="55 years old, computer programmer, lives in Seattle, knows a lot about cars, all of his answers are object oriented programming metaphors")
    prompt = ai.GPTprompt()
    prompt.prompt_constructor(identity=bill.description,
                              context="",
                              format="text with stage directions",
                              query="what is the difference between a banana and a cheese sandwich?")
    print(prompt.prompt)
    print(f"prompt is {ai.num_tokens(prompt.prompt)} tokens long")
    print(f"generating text...")
    text = prompt.generate_text()
    print(f"text is {ai.num_tokens(text)} tokens long")
    print(text)


if __name__ == "__main__":
    main()
