import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

model = ChatOpenAI( model ="gpt-6-luna", reasoning=None)

messages = [
    SystemMessage(content= "Translate the following from English to German"),
    HumanMessage(content= "hey what is going on there?")
]

if __name__ == "__main__":
    response = model.invoke(messages)
    print(response)


