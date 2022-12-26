
import gptools.functions as ai


ai.api_login()
text = ai.generate_text("a paragraph about a cat")
print(text)
story = ai.generate_story(text, "friendship", "cat", "neighborhood")
print(story)
refined, critique = ai.refine_text(story)
print(critique)
print(refined)
biased, evaluation = ai.analyze_text(refined, "biased")
print(biased)
print(evaluation)
title = ai.generate_title(refined, "Story")
print(title)




