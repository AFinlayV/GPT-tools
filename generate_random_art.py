import gptools as ai
import random
import re

ai.api_login()
num_images = 40
num_styles = 40
prompts = ai.generate_text(f"Make a list of {num_images} detailed vivid visual descriptions of the subject and background of a beautiful image, painting or photograph.")
styles = ai.generate_text(f"Make a list of {num_styles} detailed vivid visual descriptions of the colors, textures, lighting, and mood of different styles of visual art.")
#format the prompts and styles as lists
prompts = prompts.split("\n")
styles = styles.split("\n")
# use regex to remove all numbers, periods and "\n" from the prompts and styles
prompts = [re.sub(r"\d+\.|\n", "", x) for x in prompts]
styles = [re.sub(r"\d+\.|\n", "", x) for x in styles]

# remove empty list items
styles = [style for style in styles if style != ""]
prompts = [prompt for prompt in prompts if prompt != ""]
print(f"prompts:{prompts}")
print(len(prompts))
print(f"styles:{styles}")
print(len(styles))
for prompt in prompts:
    style = random.choice(styles)
    print(prompt, style)
    ai.generate_image_from_text(prompt,style, f"/Users/alexthe5th/Pictures/AI Art/{prompt+style}.png")

