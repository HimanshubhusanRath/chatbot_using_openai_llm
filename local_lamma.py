from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

## Define the prompt template
prompt = ChatPromptTemplate.from_messages([
		("system", "You are a helpful assistant. Please respond to questions in max 10 words"), # Defines the way the chatbot should answer the questions
		("user","Question : {questions}") # Defines the format of questions by the user
	]);

## Streamlit Framework
st.title("Langchain Demo with Local - LLAMA2 model")
input_text = st.text_input("Search the topic you want")


## Call Ollama API
llm = OllamaLLM(model="llama2")
output_parser = StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
	st.write(chain.invoke({'questions' : input_text}))

