import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI( model ="gpt-6-luna", reasoning=None)

messages = [
    SystemMessage(content= "Translate the following from English to German"),
    HumanMessage(content= "hey what is going on there?")
]

parser = StrOutputParser()
chain = model | parser

if __name__ == "__main__":
    print(chain.invoke(messages))


