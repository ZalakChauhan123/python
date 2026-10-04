import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# 1. Load the model and its tokenizer 
model_id = "microsoft/Phi-3-mini-4k-instruct"

tokenizer = AutoTokenizer.from_pretrained(model_id)

model = AutoModelForCausalLM.from_pretrained(
    model_id, 
    device_map="auto", 
    torch_dtype="auto", 
    trust_remote_code=True
)

# 2. Create a generation pipeline 
# This simplifies the process of tokenization and text generation
generator = pipeline(
    "text-generation", 
    model=model, 
    tokenizer=tokenizer, 
    return_full_text=False, 
    max_new_tokens=50
)

# 3. Give the prompt and get the output 
prompt = "Write a short email subject line about a new AI book."
outputs = generator(prompt)

# Print the generated answer
print(outputs[0]["generated_text"])