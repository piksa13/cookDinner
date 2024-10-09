from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import os


_ = load_dotenv(find_dotenv())
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_llm_response(prompt):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an AI assistant.",
            },
            {
                "role": "user",
                "content": prompt
            },
        ],
        temperature=0.0,
    )
    response = completion.choices[0].message.content
    return response

# prompt = input("hey, I am a chatbot, ask me a question: ")
# print(get_llm_response(prompt))
