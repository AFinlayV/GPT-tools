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
# def identity_test():
# """
#    test the prompt constructor in the Prompt class, and the Identity class and the Memory class
#    the end goal is to be able to generate several identities, let them interact with one another
#    and save each individual's memories to a file, then use that file to generate a context for future interactions
#    it's going ok i guess, but i keep getting stuck with the token limit in GPT. I tried summarizing the memories, with
#    ai.generate_summary() in the main generate_text function, but that led to my query getting lost in the summary
#    to fix this i should probably make a separate function that generates a summary of the memories, and then
#    appends that summary to the query, and then generates the text. I think that would work, but i'm not sure.
#    i'm going to go play some video games for a while, and then come back to this later.
#    """
#     bill = ai.Identity()
#     try:
#         bill.load_identity("bill.json")
#     except Exception as e:
#         print(f"identity not found: {e}, generating new identity")
#         bill.name = "Bill"
#         bill.generate_description(details="55 years old, computer programmer, lives in Seattle")
#
#     prompt = ai.Prompt()
#     topics = ai.generate_list("topics about hobbies", 3)
#     print(topics)
#     memory = bill.memory.data
#     for topic in topics:
#         questions = ai.generate_list(f"personal questions about {topic}to try to get to know Bill", 5)
#         print(questions)
#         for question in questions:
#             if ai.num_tokens(bill.memory.data) > 1000:
#                 if bill.memory.summary is None:
#                     print(f"memory is too long for GPT, generating summary...")
#                     bill.memory.generate_summary()
#                     print(bill.memory.summary)
#                 memory = bill.memory.summary
#             prompt.prompt_constructor(identity=bill.description,
#                                       context=memory,
#                                       format_example="",
#                                       query=question)
#             print(prompt.query)
#             print(f"prompt is {ai.num_tokens(prompt.prompt)} tokens long")
#             print(f"generating response...")
#             text = bill.get_response(prompt)
#             print(f"response is {ai.num_tokens(text)} tokens long")
#             print(text)
#     bill.memory.generate_summary(max_tokens=2000)
#     # print(f"summary is {ai.num_tokens(summary)} tokens long")
#     print(bill.memory.summary)
#     bill.generate_description_from_memories()
#     print(bill.description)
#     bill.save_identity("bill.json")
#

def main():
    mod_bool, mod_dict = ai.moderate_text("I am testing my moderation function to see if it catches bad words, "
                                          "and dangerous content before sending prompts to dalle or gpt: "
                                          "porn"
)
    print(mod_bool)
    for category in mod_dict['results'][0]['category_scores']:
        print(f"{category}: {format(mod_dict['results'][0]['category_scores'][category], '.4%')}")






if __name__ == "__main__":
    main()
