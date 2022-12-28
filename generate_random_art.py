import gptools.gptools as ai
import random
import re

ai.api_login()
NUM_PROMPTS = 20
NUM_STYLES = 10
NUM_IMAGES = 5
PATH = "/Users/alexthe5th/Pictures/AI Art/"
PROMPT = "a cityscape"
STYLE = "abstract art"


def generate_random_prompts(num_prompts: int, num_styles: int):
    prompts = ai.generate_list(
        f"detailed vivid visual descriptions of the subject and background for different images of {PROMPT}.",
        num_prompts)
    styles = ai.generate_list(
        f"detailed vivid visual descriptions of the colors, textures, lighting, and mood of different styles of {STYLE}.",
        num_styles)
    return prompts, styles


def generate_art(prompt, style):
    print(prompt, style)
    filename = f"{prompt} {style}"
    if len(filename) > 200:
        filename = filename[:200]
    ai.generate_image_from_text(prompt, style, f"{PATH}{filename}.png")


def main():
    prompts, styles = generate_random_prompts(NUM_PROMPTS, NUM_STYLES)
    for image in range(NUM_IMAGES):
        prompt = random.choice(prompts)
        style = random.choice(styles)
        generate_art(prompt, style)


if __name__ == "__main__":
    main()
