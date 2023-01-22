"""
A Script that generates a quiz, given a topic, a number of questions, and difficulty level.
It then asks the user the questions and grades the quiz.

TODO:
    - Add a way to save the quiz to a file
    - Add a way to load a quiz from a file
    - Divide the code into functions and add a main function
    - Add a way to use agents, instead of just the LLM
    - Add a way to reference Wolfram Alpha and Google Search
    - Generate one question at a time, but save a list of questions so that they are not repeated
"""

from langchain import PromptTemplate
from langchain import OpenAI
from os import environ
import json

OPENAI_API_KEY_PATH = "/Users/alexthe5th/Documents/API Keys/OpenAI_API_key.txt"
with open(OPENAI_API_KEY_PATH, "r") as f:
    OPENAI_API_KEY = f.read().strip()

environ["OPENAI_API_KEY"] = OPENAI_API_KEY

quizmaster_template = """Quizmaster is a large language model trained by OpenAI.

Quizmaster is designed Generate quiz questions and answers. As a language model, Quizmaster is able to generate 
human-like Questions and Answers based on the topic it is given, the number of questions specified, and the dificulty level specified

Generate the questions using the following details:
--------------------
Topic: {topic}
Number of Questions: {num_questions}
Difficulty: {difficulty}
--------------------

FORMAT:
List only the question, followed by a "," and then the answer. For example:
1. What is the capital of France?, Paris
2. What is the capital of Germany?, Berlin

Quizmaster:"""

quizformat_template = """Quizformatter is a large language model trained by OpenAI.

Quizformatter will take in a quiz and reformat it into a different format. As a language model, Quizformatter is able to generate
json formatted data from a list of questions and answers. the json file will have the questions as keys, and the correct answer as the value.
it will use only the questions and answers provided, and will not generate any new questions or answers.

Quizformatter will take in the following data:
{quiz}

and will output the following json file:
"""
quizgrader_template = """Quizgrader is a large language model trained by OpenAI.

Quizgrader is designed to grade quiz questions and answers. Given the Json format data of the question and answer below
Quizgrader will evaluate the Human Input, and compare it to the correct answer. it will return a float value between 0 and 1
with 1 being a perfect score and 0 being a complete failure. 

Quizgrader will only return a floating point number between 0 and 1 in the following format:
0.00

Given the following questions and answers:

----------------------------------------
Question:
{question}

Correct Answer:
{answer}

Human input:
{human_input}
----------------------------------------
Quizgrader's Evaluation:"""

quiz_llm = OpenAI(model_name="text-davinci-003", temperature=0.9)
eval_llm = OpenAI(model_name="text-davinci-003", temperature=0)

topic = input("Topic: ")
num_questions = input("Number of Questions: ")
difficulty = input("Difficulty: ")
quiz_prompt = PromptTemplate(
    input_variables=["topic", "num_questions", "difficulty"],
    template=quizmaster_template
)
prompt = quiz_prompt.format(topic=topic, num_questions=num_questions, difficulty=difficulty)
quiz = quiz_llm(prompt)
format_prompt = PromptTemplate(
    input_variables=["quiz"],
    template=quizformat_template
)
prompt = format_prompt.format(quiz=quiz)
json_quiz = json.loads(eval_llm(prompt))
graded_quiz = {}
for question in json_quiz:
    print(question)
    human_input = input("Answer: ")
    grader_prompt = PromptTemplate(
        input_variables=["question", "answer", "human_input"],
        template=quizgrader_template)
    prompt = grader_prompt.format(question=question, answer=json_quiz[question], human_input=human_input)
    grade = float(eval_llm(prompt).strip())
    graded_quiz[question] = {}
    graded_quiz[question]['Answer Provided'] = human_input
    graded_quiz[question]['Correct Answer'] = json_quiz[question]
    graded_quiz[question]['Grade'] = grade

total_grade = 0
for question in graded_quiz:
    print(f"""
    Question: {question}
    Answer Provided: {graded_quiz[question]['Answer Provided']}
    Correct Answer: {graded_quiz[question]['Correct Answer']}
    Grade: {graded_quiz[question]['Grade']}
    """)
    total_grade += graded_quiz[question]['Grade']
total_grade = int(total_grade / len(graded_quiz) * 100)

print(f"Total Grade: {total_grade}")
