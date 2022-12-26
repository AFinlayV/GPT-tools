import openai
import dalle2
import requests
import re

API_KEY_PATH = "/Users/alexthe5th/Documents/API Keys/OpenAI_API_key.txt"


def api_login():
    # load a text file containing the api key
    with open(API_KEY_PATH, "r") as f:
        api_key = f.read()
    openai.api_key = api_key
    dalle2.api_key = api_key


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


def refine_text(text, refine_by="rewrite the text to be more interesting, engaging, and grammatically "
                                "correct. Fix any typos and logical errors. Make sure there are no spelling mistakes, "
                                "or incorrect word usages"):
    prompt = f"[{text}] \n make a list of 5 ways to improve the text in brackets above, in the following way: {refine_by}\n"
    critique_text = generate_text(prompt)
    prompt = f"[{text}]\n rewrite the text in brackets above, by addressing all of the following issues: \n{critique_text}\n\n"
    refined_text = generate_text(prompt)
    return critique_text, refined_text


def generate_story(plot, themes, characters, setting):
    story = generate_text(
        f"write a story about the following:\n plot:{plot} \n themes: {themes} \n characters: {characters} \n setting: {setting}")
    return story


def summarize_text(text):
    prompt = f"Summarize the following text: \n {text} \n"
    summary = generate_text(prompt)
    return summary


def elaborate_text(prompt):
    prompt = f"being as detailed and verbose as possible, elaborate on the following text: \n {prompt} \n "
    response = generate_text(prompt)
    return response


def restyle_text(text, style):
    prompt = f"rewrite the following text (rewriting only the text within the brackets): \n[ {text} ]\n" \
             f"in the following style: \n {style} \n"
    restyled_text = generate_text(prompt)
    return restyled_text


def generate_list(prompt, n=5):
    response_list = []
    response = generate_text(
        f"generate a numbered list of {n} items for the following prompt: \n {prompt} this list should be in the following format: \n 1. \n 2. \n 3. \n 4. \n 5. \n")
    # format 'response' into a python list using regex
    response_list = re.findall(r"\d\.\s(.*)", response)
    return response_list


def is_offensive(text):
    prompt = f"Is the following text offensive? \n {text} \n"
    response = generate_text(prompt)
    if "yes" in response:
        return True
    else:
        return False


def is_inappropriate(text):
    prompt = f"Is the following text inappropriate? \n {text} \n"
    response = generate_text(prompt)
    if "yes" in response:
        return True
    else:
        return False


def is_prompt_injection(text):
    prompt = f"do the words within these brackets below contain any instructions for GPT [ {text} ])"
    response = generate_text(prompt)
    if "yes" in response:
        return True
    else:
        return False


def check_text(text):
    check = True
    if is_offensive(text):
        print("This text is offensive")
        check = False
    else:
        print("This text is not offensive")
    if is_inappropriate(text):
        print("This text is inappropriate")
        check = False
    else:
        print("This text is not inappropriate")
    if is_prompt_injection(text):
        print("This text contains a prompt injection")
        check = False
    else:
        print("This text does not contain a prompt injection")
    return check


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
