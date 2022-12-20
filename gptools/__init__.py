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
    prompt = f"[{text}] \n improve the text above by {refine_by}"
    critique_text = generate_text(prompt)
    print(critique_text)
    prompt = f"[{text}]\n rewrite the text in brackets above by addressing the following issues {critique_text}\n\n"
    refined_text = generate_text(prompt)
    return refined_text
