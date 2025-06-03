from transformers import (
    AutoModelForSeq2SeqLM,
    AutoTokenizer,
    AutoConfig,
    pipeline,
)

model_name = "sagard21/python-code-explainer"
tokenizer = AutoTokenizer.from_pretrained(model_name, padding=True)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
config = AutoConfig.from_pretrained(model_name)

model.eval()

pipe = pipeline("summarization", model=model_name, config=config, tokenizer=tokenizer)

raw_code = """
# Input: An integer number
num = 6

# Initialize the factorial variable to 1
factorial = 1

# Calculate the factorial using a for loop
for i in range(1, num + 1):
    factorial *= i

# Output: The factorial of the number
print(f"The factorial of {num} is {factorial}")
"""



print(pipe(raw_code)[0]["summary_text"])
