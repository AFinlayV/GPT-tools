import gptools.gptools as ai
import datetime


API_KEY_PATH = "/Users/alexthe5th/Documents/API Keys/OpenAI_API_key.txt"
ai.api_login(API_KEY_PATH)

"""
a sandbox for brainstorming interactions between the functions in gptools.functions and the OpenAI API

"""


def main():
    prompt = "write a blog post about a new beer release for a beer called 'mouthfeel'. it is a belgian farmhouse ale being released " \
             "by 'loveyou brewing' in asheville north carolina on may 4th 2023. " \
             "the release will feature a performance by the psych folk band 'of the stars'" \
             "be sure to mention the abv and ibu of the beer, as well as the type of hops used"

    prompt_obj = ai.Prompt(prompt)
    check_prompt = prompt_obj.check()
    for check in check_prompt:
        print(f"{check}: {check_prompt[check]['result']}\nExplanation: {check_prompt[check]['evaluation']}\n")

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
    while True:
        print("Would you like to refine the text further?")
        refine = input("y/n: ")
        if refine == "y":
            print("What would you like to refine?")
            refine = input("refine: ")
            refine_list.append(refine)
            text_obj.refine(refine_list)
            print(text_obj.refined_text)
        elif refine == "n":
            break
        else:
            print("please enter 'y' or 'n'")
    text_obj.check_refined()
    for check in text_obj.check_results:
        print(f"{check}: {text_obj.check_results[check]['result']}\nExplanation: {text_obj.check_results[check]['evaluation']}\n")
    print("Would you like to save the text?")
    save = input("y/n: ")
    if save == "y":
        print("What would you like to name the file?")
        file_name = input("file name: ")
        text_obj.save(file_name)
    elif save == "n":
        pass
    else:
        print("please enter 'y' or 'n'")










if __name__ == "__main__":
    main()