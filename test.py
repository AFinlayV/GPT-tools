import gptools as ai

ai.api_login()
prompt = input("Enter a prompt: ")
text = ai.generate_text(prompt)
print(text)
while True:
    refine_by = input("Enter a refinement: ")
    refined_text = ai.refine_text(text, refine_by)
    text = refined_text
    print(refined_text)
    user_input = input("Press enter to continue refining, or type 'q' to quit: ")
    if user_input == "q":
        break
    else:
        continue
