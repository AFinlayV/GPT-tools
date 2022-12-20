import gptools as ai

ai.api_login()
plot = input("Enter a plot: ")
themes = input("Enter themes: ")
characters = input("Enter characters: ")
setting = input("Enter setting: ")
text = ai.generate_story(plot, themes, characters, setting)
print(text)
while True:
    refine_by = input("Enter a refinement: ")
    refined_text = ai.refine_text(text, refine_by)
    print(refined_text)
    user_input = input("Would you like to refine again? (y/n): ")
    if user_input == "y":
        text = refined_text
    elif user_input == "n":
        break
