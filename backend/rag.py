from LLMBackend import LLMBackendGenAI
import json
import os
from nearest_text import nearest_reference

configs = {
    "parameters": {
                    "decoding_method": "greedy",
                    "stop_sequences": [
                    "\\n\\nPlease provide the actual"
                    ],
                    "include_stop_sequence": False,
                    "min_new_tokens": 1,
                    "max_new_tokens": 2048
                },
    "moderations": {
        "hap": {
        "threshold": 0.75,
        "input": True,
        "output": True
        },
        "stigma": {
        "threshold": 0.75,
        "input": True,
        "output": True
        }
    }
}

model_id = 'ibm-mistralai/mixtral-8x7b-instruct-v01-q'

llm = LLMBackendGenAI(model_id=model_id, configs=configs)

def rag_qna(file_path, question = "This is a test question"):
    #print("I am working")

    with open(file_path, 'r') as file:
        text = file.read()
   # return text
    topn_chunks = nearest_reference(question, text)
    prompt = llm.rag_prompt(question, topn_chunks)
    res = llm.generate_response(prompt)
    return res