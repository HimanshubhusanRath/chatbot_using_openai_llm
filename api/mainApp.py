from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
from langchain_ollama import OllamaLLM
import uvicorn
import os
from dotenv import load_dotenv
from pathlib import Path

parent_dir = Path(__file__).parent.parent
print(os.path.join(parent_dir, '.env'))
load_dotenv(os.path.join(parent_dir, '.env'))

# Define the App
app = FastAPI(
		title="Langchain Server",
		version = "1.0",
		description = "A simple API server for LLMs"
	) 

# Define Default route
add_routes(
		app,
		ChatOpenAI(),
		path="/openai"
	)

model_openai = ChatOpenAI()
model_localLLM = OllamaLLM(model="llama2")

prompt_1 = ChatPromptTemplate.from_template("Write me a essay about {topic} with 50 words")
prompt_2 = ChatPromptTemplate.from_template("Write me a poem about {topic} with 30 words")

## Define specific routes
add_routes(
		app,
		prompt_1|model_openai,
		path = "/essay"
	)

add_routes(
		app,
		prompt_2|model_localLLM,
		path = "/poem"
	)


if __name__ == "__main__":
	uvicorn.run(app,host="localhost",port=8000)







