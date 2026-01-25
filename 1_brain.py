# {image(Encoding) + query} ---> LLM ----> O/P

import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

import base64

with open('ra.jpg','rb') as f:
    ima_b64 = base64.b64encode(f.read()).decode('utf-8')

from groq import Groq

client = Groq()
model = "meta-llama/llama-4-maverick-17b-128e-instruct"

query = "can You give me name of the diseases"

messages = [
    {
        "role": "user",
        "content": [
            {
                "type":"text",
                "text": query
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