"""
A clone of Chat GPT, but with langchain's ability to reference searches, wolfram alpha, and math
A project to learn the syntax of langchain's modules
"""
from langchain.agents import Tool
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain import OpenAI
from langchain.utilities import GoogleSearchAPIWrapper
from langchain.agents import initialize_agent
from langchain.utilities.wolfram_alpha import WolframAlphaAPIWrapper
from langchain.utilities import PythonREPL
from langchain import LLMMathChain
import os

OPENAI_API_KEY_PATH = "/Users/alexthe5th/Documents/API Keys/OpenAI_API_key.txt"
with open(OPENAI_API_KEY_PATH, "r") as f:
    OPENAI_API_KEY = f.read().strip()

GOOGLE_API_KEY_PATH = "/Users/alexthe5th/Documents/API Keys/GoogleSearchAPI_key.txt"
with open(GOOGLE_API_KEY_PATH, "r") as f:
    GOOGLE_API_KEY = f.read().strip()

GOOGLE_CX_PATH = "/Users/alexthe5th/Documents/API Keys/GoogleSearch_ID.txt"
with open(GOOGLE_CX_PATH, "r") as f:
    GOOGLE_CX = f.read().strip()

WOLFRAM_ALPHA_API_KEY_PATH = "/Users/alexthe5th/Documents/API Keys/wolfram_id.txt"
with open(WOLFRAM_ALPHA_API_KEY_PATH, "r") as f:
    WOLFRAM_ALPHA_API_KEY = f.read().strip()

TMDB_API_KEY_PATH = "/Users/alexthe5th/Documents/API Keys/TMDB_api_key.txt"
with open(TMDB_API_KEY_PATH, "r") as f:
    TMDB_API_KEY = f.read().strip()

os.environ["WOLFRAM_ALPHA_APPID"] = WOLFRAM_ALPHA_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
os.environ["GOOGLE_CSE_ID"] = GOOGLE_CX
os.environ["TMDB_API_KEY"] = TMDB_API_KEY


template = """Assistant is a large language model trained by OpenAI.

Assistant is designed to be able to assist with a wide range of tasks, from answering simple questions to providing 
in-depth explanations and discussions on a wide range of topics. As a language model, Assistant is able to generate 
human-like text based on the input it receives, allowing it to engage in natural-sounding conversations and provide 
responses that are coherent and relevant to the topic at hand.

Assistant is constantly learning and improving, and its capabilities are constantly evolving. It is able to process 
and understand large amounts of text, and can use this knowledge to provide accurate and informative responses to a 
wide range of questions. Additionally, Assistant is able to generate its own text based on the input it receives, 
allowing it to engage in discussions and provide explanations and descriptions on a wide range of topics.

Overall, Assistant is a powerful tool that can help with a wide range of tasks and provide valuable insights and 
information on a wide range of topics. Whether you need help with a specific question or just want to have a 
conversation about a particular topic, Assistant is here to assist. 

{history}
Human: {human_input}
Assistant:"""

template2 = """You are a human with a desire to say the most confusing and absurd response to the prompt"""
llm = OpenAI(temperature=0)
search = GoogleSearchAPIWrapper()
wolfram = WolframAlphaAPIWrapper()
repl = PythonREPL()
llm_math = LLMMathChain(llm=llm,
                        verbose=True)
tools = [
    Tool(
        name="Current Search",
        func=search.run,
        description="useful for when you need to answer questions about "
                    "current events or the current state of the world"
    ),
    Tool(
        name="Wolfram Alpha",
        func=wolfram.run,
        description="A wolfram alpha search engine. Useful for when you need to answer questions about Math, Science, "
                    "Technology, Culture, Society and Everyday Life. Input should be a search query."
    ),
    Tool(
        name="Repl",
        func=repl.run,
        description="A python REPL. Useful for when you need to run python code. Input should be a python expression."
    ),
    Tool(
        name="Math",
        func=llm_math.run,
        description="A math chain. Useful for when you need to do math. Input should be a math expression."
    )
]
memory = ConversationBufferMemory(memory_key="chat_history")
agent_chain = initialize_agent(tools,
                               llm,
                               agent="conversational-react-description",
                               verbose=False,
                               memory=memory,
                               template=template)


while True:
    user_input = input("Human: ")
    if user_input == "exit":
        break
    response = agent_chain.run(input=user_input)
    print(response)
