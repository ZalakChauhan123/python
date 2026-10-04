from transformers import AutoTokenizer

# Load pre trained tokenizer
tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-4k-instruct")

# Convert text into token IDs
prompt = "Write an email apologizing to Sarah for the tragic gardening mishap. Explain how it happened.<|assistant|>"
inputIds = tokenizer(prompt).input_ids

# See the numerical IDs the model actually receives
print("Input Ids : ", inputIds)

for id in inputIds:
    print(tokenizer.decode(id))
