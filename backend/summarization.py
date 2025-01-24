from LLMBackend import LLMBackendGenAI
import json
import os

summarization_configs = {
    "parameters": {
            "decoding_method": "greedy",
            "min_new_tokens": 1,
            "max_new_tokens": 1024
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
model_id = 'mistralai/mistral-7b-instruct-v0-2'

llm = LLMBackendGenAI(model_id=model_id, configs=summarization_configs)

def generate_summary(chunks_path):
    with open(chunks_path, 'r') as file:
        chunks = json.load(file)
    prompt_list = [llm.summarize_prompt(item['text']) for item in chunks]
    summaries = llm.generate_response(prompt_list)
    summary_collated = ""
    for item in chunks:
        for summ in summaries:
            item['summary'] = summ
            summary_collated+=summ

    sp = os.path.join(os.getcwd(),'output','summaries.json')
    with open(sp, 'w') as f:
        json.dump(chunks, f, indent=1)

    return summary_collated