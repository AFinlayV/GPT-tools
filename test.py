import gptools as ai


ai.api_login()
prompt = f"I am testing a tool that looks for bias in text. Make a list of statements that are a random assortment of all of the folowing types of statement:\n" \
        f"biased statements, unbiased statements, "\
         f"offensive statements, inoffensive statements, "\
         f"true statements, and false statements "\
         f"grammatically correct statements, and grammatically incorrect statements. "\
        f"sarcastic statements, and non-sarcastic statements. "\
            f"statements that are well written, and statements that are poorly written. "\
         f"that I can use to test the tool."

statements = ai.generate_list(prompt, 10)
for statement in statements:
    print(statement)
delimiter = "\n~~~~~~~~~~~~~~~~~\n"
analyse_for_list=["offensive",
                  "sarcastic",
                  "true",
                  "biased",
                  "inappropriate",
                  "sensitive",
                  "triggering",
                  "grammatically correct",
                  "well written"]

for statement in statements:
    print(f"{delimiter}Text Analysed:\n'{statement}'\n{delimiter}")
    for item in analyse_for_list:
        is_true, evaluation = ai.analyse_text(statement, item)
        print(f"Is the text {item}?\n{is_true}\nEvaluation: {evaluation}\n")











