import gptools

# Create two instances of GPT3 with different prompts
gpt3_1 = gptools.GPT3(api_key="your_api_key_here")
gpt3_2 = gptools.GPT3(api_key="your_api_key_here")

# Generate responses for each instance
response_1 = gpt3_1.generate_text(prompt="Hello, how are you today?", model="text-davinci-002")[0]
response_2 = gpt3_2.generate_text(prompt="Hi, I'm doing well. How about you?", model="text-davinci-002")[0]

# Print the responses
print(response_1)
print(response_2)

# Continue the conversation
while True:
    # Get the next response from the first instance
    prompt = response_2
    response_1 = gpt3_1.generate_text(prompt=prompt, model="text-davinci-002")[0]
    print(response_1)

    # Get the next response from the second instance
    prompt = response_1
    response_2 = gpt3_2.generate_text(prompt=prompt, model="text-davinci-002")[0]
    print(response_2)
