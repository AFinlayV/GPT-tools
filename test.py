import gptools as ai

ai.api_login()
class story
    def __init__(self, plot, themes, characters, setting):
        self.plot = plot
        self.themes = themes
        self.characters = characters
        self.setting = setting
        self.story = ai.generate_story(plot, themes, characters, setting)
        self.refined_story = ai.refine_text(self.story, "make general improvements")
        self.character_descriptions = ai.generate_character_descriptions(self.refined_story)
        self.image_prompts = ai.generate_character_image_prompts(self.character_descriptions)
        self.images = ai.generate_images(self.image_prompts)
        self.storybook = ai.generate_storybook(self.refined_story, self.character_descriptions, self.images)
        self.storybook.save("storybook.pdf")