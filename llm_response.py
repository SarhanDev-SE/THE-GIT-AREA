from llm_call import llm_caller
import os

os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")

response = llm_caller({"question":"Who is the PM of Pakistan"})

print(response)