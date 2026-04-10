from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import get_peft_model, LoraConfig

def load_model():
    model = AutoModelForCausalLM.from_pretrained("gpt2")
    tokenizer = AutoTokenizer.from_pretrained("gpt2")

    config = LoraConfig(
        r=8,
        lora_alpha=16,
        target_modules=["c_attn"],
        lora_dropout=0.1,
        bias="none"
    )

    model = get_peft_model(model, config)

    return model, tokenizer