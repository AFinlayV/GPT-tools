import gptools as ai

ai.api_login()
prompt = input("Enter a prompt: ")
text = ai.generate_story(prompt)
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
