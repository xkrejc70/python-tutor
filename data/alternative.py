import requests

import torch
from transformers import pipeline, AutoConfig
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForSequenceClassification, LlamaTokenizer


# Test Hugging face API - free model
def test1():

    API_URL = "https://api-inference.huggingface.co/models/teknium/OpenHermes-2-Mistral-7B"
    headers = {"Authorization": "Bearer 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"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
        
    output = query({
        "inputs": "Can you please let us know feedback about this code: print('hi')",
    })

    return output

def output():

    #model_name = "teknium/OpenHermes-2.5-Mistral-7B"
    model_name = "hojzas/proj8-mistral-new"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)

    """
    #model = AutoModelForCausalLM.from_config(config, trust_remote_code=True)
    #model.tie_weights()
    pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)
    example = "What is Madrid city?"

    ner_results = pipe(example)
    print(ner_results)
    """

    #ChatML format
    input_text = "\
    <|im_start|>system:\nYou are expert python tutor providing specific feedback on code efficiency.<|im_end|>\
    <|im_start|>user:\ndef first_with_given_key(iterable, key=lambda value: value):\n        it = iter(iterable)\n        saved_keys = []\n        while True:\n            try:\n                value = next(it)\n                if key(value) not in saved_keys:\n                    saved_keys.append(key(value))\n                    yield value\n            except StopIteration:\n                break<|im_end|>\
    <|im_start|>tutor:\n"

    input_ids = tokenizer(input_text, return_tensors="pt").input_ids

    outputs = model.generate(input_ids, max_new_tokens=1000)
    print(tokenizer.decode(outputs[0]))





print(test1())