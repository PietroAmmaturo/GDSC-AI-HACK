from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("google/gemma-1.1-2b-it")
model = AutoModelForSeq2SeqLM.from_pretrained("google/gemma-1.1-2b-it")

tokenizer.save_pretrained("./gemma/gemma-1.1-2b-it")
model.save_pretrained("./gemma/gemma-1.1-2b-it")
