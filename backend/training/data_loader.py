from datasets import load_dataset

def load_data():
    dataset = load_dataset("gsm8k", "main")
    return dataset