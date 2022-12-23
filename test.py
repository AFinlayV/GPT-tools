import gptools as ai
import random


ai.api_login()
prompts = ai.generate_text("Make a list of 100 descriptions of beautiful images")
styles = ai.generate_text("Make a list of 20 visual art styles")
#format the prompts as a list
styles = styles.split("\n")
prompts = prompts.split("\n")
# remove empty list items
styles = [style for style in styles if style != ""]
prompts = [prompt for prompt in prompts if prompt != ""]
print(prompts)
for prompt in prompts:
    style = random.choice(styles)
    print(prompt, style)
    ai.generate_image_from_text(prompt,style, f"{prompt+style}.png")

