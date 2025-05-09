from langchain_community.llms import Ollama

# Test if we can initialize the Ollama model
try:
    llm = Ollama(model="llama2")
    print("Successfully initialized Ollama with llama2 model!")
    print("Testing a simple prompt...")
    response = llm.invoke("What is 2+2?")
    print("Response:", response)
except Exception as e:
    print("Error:", str(e)) 