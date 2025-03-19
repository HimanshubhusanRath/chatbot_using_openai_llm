# ChatBot using OpenAI and Local LLMs
* Run the OpenAI based Chatbot : <code>streamlit run app.py</code>
* Run the Local LLM (LLAMA2 on Ollama) based Chatbot : <code>streamlit run local_lamma.py</code>

# Chatbot using routes:
* Here, different models are used for different type of requests.
* To generate essay, we are using OpenAI API here and to generate poem, we are using local model (LLAMA2 on Ollama).
* Routes are defined in the main application (let's say API Server) which maps the type (essay/poem) of request to specific model.
* A client application (Streamlit based chat app) calls this API server internally to get the result from models.    
* Go to 'app' folder : <code> cd app </code>
* Run the API server : <code> python mainApp.py</code>
* Run the client application : <code> streamlit run client.py</code>


## Pre-requisites
* LLAMA2 model on Ollama should be up and running in the local system.
* To use different models, the model names need to be updated in the code. Example : <code>model_localLLM = OllamaLLM(model="llama2")</code>