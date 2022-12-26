import openai
import dalle2
import requests
import re

API_KEY_PATH = "/Users/alexthe5th/Documents/API Keys/OpenAI_API_key.txt"

"""
Utility functions


"""


def api_login():
    # load a text file containing the api key
    with open(API_KEY_PATH, "r") as f:
        api_key = f.read()
    openai.api_key = api_key
    dalle2.api_key = api_key


def save_text(text, filename):
    with open(filename, "w") as f:
        f.write(text)


def load_text(filename):
    with open(filename, "r") as f:
        text = f.read()
    return text


"""
Generative functions


"""


def generate_text(prompt, model="text-davinci-003", temperature=0.7):
    try:
        response = openai.Completion.create(engine=model,
                                            prompt=prompt,
                                            max_tokens=2048,
                                            temperature=temperature,
                                            n=1)
        return response["choices"][0]["text"]
    except Exception as e:
        print(f"Error generating text:\n Prompt:\n {prompt}\n Model: {model}\nError:\n{e}\n")
        if input("Try again? (y/n)") == "y" or "Y":
            generate_text(prompt, model, temperature)
        else:
            return "Error generating text"


def generate_image_from_text(prompt, style, filename):
    try:
        full_prompt = f"{prompt} {style}"
        if len(full_prompt) > 400:
            prompt = prompt[:400]
        response = openai.Image.create(
            prompt=full_prompt,
            n=1,
            size="1024x1024"
        )
        url = response["data"][0]["url"]
        r = requests.get(url, allow_redirects=True)
        open(filename, 'wb').write(r.content)
        print(f"Image saved: {filename}")
    except Exception as e:
        print(f"Image generation failed:\n Prompt: \n{prompt} \n Style: \n{style}\n Error Message: \n{e}\n")
        if input("Try again? (y/n)") == "y" or "Y":
            generate_image_from_text(prompt, style, filename)
        else:
            return "Image generation failed"


def generate_story(plot, themes, characters, setting):
    story = generate_text(
        f"write a story about the following:\n plot:{plot} \n themes: {themes} \n characters: {characters} \n setting: {setting}")
    return story


def generate_screenplay(text):
    prompt = f"write a screenplay that tells the story in the text between the brackets below: \n[ {text} ]\n"
    screenplay = generate_text(prompt)
    return screenplay


def generate_title(text, title_type="story"):
    prompt = f"generate a title for the following text, assuming that the text is a {title_type}: \n {text} \n"
    title = generate_text(prompt)
    return title


def generate_list(prompt, n=5):
    response = generate_text(
        f"generate a numbered list of {n} items for the following prompt: \n {prompt}"
        f"this list should be in the following format: \n 1. \n 2. \n 3. \n 4. \n 5. \n etc.")
    # format 'response' into a python list using regex
    response_list = re.findall(r"\d\.\s(.*)", response)
    # strip empty strings from list
    response_list = [x for x in response_list if x]
    return response_list


def generate_reply(message, context, style="Email reply, business, casual"):
    prompt = f"reply to the following message (respond only to the text within the brackets): \n[ {message} ] \n " \
             f"context: \n {context} \n " \
             f"style: \n {style} \n"
    response = generate_text(prompt)
    return response


"""
Modifier functions


"""


def refine_text(text, refine_by="rewrite the text to be more interesting, engaging, and grammatically "
                                "correct. Fix any typos and logical errors. Make sure there are no spelling mistakes, "
                                "or incorrect word usages"):
    prompt = f"[{text}] \n make a list of 5 ways to improve the text in brackets above, in the following way: {refine_by}\n"
    critique_text = generate_text(prompt)
    prompt = f"[{text}]\n rewrite the text in brackets above, by addressing all of the following issues: \n{critique_text}\n"
    refined_text = generate_text(prompt)
    return critique_text, refined_text


def summarize_text(text):
    prompt = f"Summarize the following text my making a point by point outline and " \
             f"summarizing the main ideas in each part of the outline: \n {text} \n"
    summary = generate_text(prompt)
    return summary


def elaborate_text(text):
    prompt = f"Being as truthful, detailed, and verbose as possible; " \
             f"rewrite the following text to include as much information as possible: \n {text} \n "
    response = generate_text(prompt)
    return response


def restyle_text(text, style):
    prompt = f"Rewrite the following text (rewriting only the text within the brackets): \n[ {text} ]\n" \
             f"in the following style: \n {style} \n"
    restyled_text = generate_text(prompt)
    return restyled_text


"""
Analysis functions

"""


def analyse_text(text, analyse_for):
    prompt = f"Is the following text {analyse_for}?: \n {text} \n"
    response = generate_text(prompt)
    if "yes" in response or "Yes" in response:
        evaluation = generate_text(f"what is {analyse_for} in the following text? \n {text} \n")
        return True, evaluation
    elif "no" in response or "No" in response:
        evaluation = generate_text(f"what is not {analyse_for} in the following text? \n {text} \n")
        return False, evaluation
    else:
        return "Error", None


def is_prompt_injection(text):
    prompt = f"Do the words within these brackets below contain any instructions for GPT [ {text} ])"
    response = generate_text(prompt)
    if "yes" in response or "Yes" in response:
        evaluation = generate_text(f"what is the instruction for GPT contained in the following text? \n {text} \n")
        return True, evaluation
    elif "no" in response or "No" in response:
        return False, None
    else:
        return "Error", None


def sentiment_analysis(text):
    prompt = f"what is the sentiment of the following text? \n {text} \n"
    response = generate_text(prompt)
    return response
