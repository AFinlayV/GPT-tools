import openai
import dalle2
import requests
import re
import gptools.functions as ai
"""

This file contains the objects used in the GPTools library.

"""

class GPT3:

    def __init__(self, api_key, engine="text-davinci-003", temperature=0.7, max_tokens=2048, top_p=1, frequency_penalty=0, presence_penalty=0, stop=["\
"], echo=False):
        self.api_key = api_key
        self.engine = engine
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty
        self.stop = stop
        self.echo = echo

