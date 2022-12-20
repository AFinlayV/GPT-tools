import openai
import dalle2
import requests


def api_login():
    # load a text file containing the api key
    with open("/Users/alexthe5th/Documents/API Keys/OpenAI_API_key.txt", "r") as f:
        api_key = f.read()
    openai.api_key = api_key
    dalle2.api_key = api_key


def generate_text(prompt, model="text-davinci-003", temperature=0.5, n=1):
    completions = openai.Completion.create(engine=model, prompt=prompt, max_tokens=1024, temperature=temperature, n=n)
    responses = [choice.text for choice in completions.choices]
    return responses[0]


def refine_text(text, refine_by):
    if refine_by == "":
        refine_by = "make general improvements"
    prompt = f"[{text}] \n make a list of 5 ways to improve the text in brackets above, in the following way: {refine_by}\n"
    critique_text = generate_text(prompt)
    print(critique_text)
    prompt = f"[{text}]\n rewrite the text in brackets above, by addressing all of the following issues: \n{critique_text}\n\n"
    refined_text = generate_text(prompt)
    return refined_text


def generate_story(plot, themes, characters, setting):
    story = generate_text(
        f"write a story about the following:\n plot:{plot} \n themes: {themes} \n characters: {characters} \n setting: {setting}")
    return story


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


def generate_image_prompt(text):
    prompt = f"generate an image prompt for DALL-E2 from the following text: \n {text} \n"
    response = generate_text(prompt)
    return response


def generate_image(prompt, style, filename):
    if check(prompt):
        print("This prompt is OK")
    else:
        print("This prompt is not allowed")
    image_response = openai.Image.create(
        prompt=prompt + style,
        n=1,
        size="1024x1024"
    )
    image_url = image_response["data"][0]["url"]
    print(image_url)
    # download the image from the address stored in image_url
    image = requests.get(image_url)
    # save the image to a file
    with open(filename, "wb") as f:
        f.write(image.content)

