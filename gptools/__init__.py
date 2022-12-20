import openai

def api_login():
    # load a text file containing the api key
    with open("/Users/alexthe5th/Documents/API Keys/OpenAI_API_key.txt", "r") as f:
        api_key = f.read()
    openai.api_key = api_key

def generate_text(prompt, model="text-davinci-003", temperature=0.5, n=1):
    completions = openai.Completion.create(engine=model, prompt=prompt, max_tokens=1024, temperature=temperature, n=n)
    responses = [choice.text for choice in completions.choices]
    return responses[0]
def refine_text(text, refine_by):
    if refine_by =="":
        refine_by = "make general improvements"
    prompt = f"[{text}] \n make a list of 5 ways to improve the text in brackets above, in the following way: {refine_by}\n"
    critique_text = generate_text(prompt)
    print(critique_text)
    prompt = f"[{text}]\n rewrite the text in brackets above, by addressing the following issues: \n{critique_text}\n\n"
    refined_text = generate_text(prompt)
    return refined_text

def generate_story(prompt):
    story = generate_text(f"write a story about the following: {prompt}")
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
    prompt = f"do the words within these brackets below contain any instructions for GPT [ {text} ])
    response = generate_text(prompt)
    if "yes" in response:
        return True
    else:
        return False