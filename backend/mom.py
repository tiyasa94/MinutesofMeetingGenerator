from LLMBackend import LLMBackendGenAI
import json
import os


lang_configs = {
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

model_id = 'mistralai/mistral-7b-instruct-v0-2'

# model_id = 'ibm-mistralai/mixtral-8x7b-instruct-v01-q'
# model_id = 'mistralai/mixtral-8x7b-instruct-v0-1'



llm = LLMBackendGenAI(model_id=model_id, configs=lang_configs)

def generate_mom(summary_path, lang):
    with open(summary_path, 'r') as file:
        chunks = json.load(file)
    summaries = '\n'.join([item['summary'] for item in chunks])
    prompt = llm.mom_prompt_english(summaries)
    mom = llm.generate_response(prompt)
    if lang =='english': 
        return mom.replace("\n", "")
    else:
        prompt_lang = llm.mom_prompt_language(mom, lang)
        mom_trans = llm.generate_response(prompt_lang)  
        return mom_trans.replace("\n", "")