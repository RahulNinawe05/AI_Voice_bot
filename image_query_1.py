# {image(Encoding) + query} ---> LLM ----> O/P

import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

import base64

with open('image_1.jpg','rb') as f:
    ima_b64 = base64.b64encode(f.read()).decode('utf-8')

from groq import Groq

client = Groq()
model = "meta-llama/llama-4-maverick-17b-128e-instruct"

if not client:
    raise Exception ("This is GroqApi Error")

system_prompt = """
    You are a Doctor 20 Year's of Exeperience. I have to Give some Question of any topic 
    You give the solution of deseases.
    You reply it in simple language i can understad propely 
    you are going to google giving image link of the deseases.
    """
query = "only name of deseases"

messages = [
    {
        "role": "user",
        "content": [
            {
                "type":"text",
                "text": query + system_prompt
            },
            {
                "type":"image_url",
                "image_url":{
                    "url": f"data:image/jpeg;base64,{ima_b64}"
                }
            }
        ]
    }
]

chat_complet = client.chat.completions.create(
    messages=messages,
    model=model
)

print(chat_complet.choices[0].message.content)