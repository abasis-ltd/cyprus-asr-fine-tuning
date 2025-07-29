import os
from datasets import Dataset, Audio
from huggingface_hub import login

login("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")

audio_files = [f for f in os.listdir('.') if f.endswith('.mp3')]

data = [{"audio": f} for f in audio_files]
ds = Dataset.from_list(data).cast_column("audio", Audio(sampling_rate=16000))

ds.push_to_hub("Elormiden/cooking-show-raw", private=True)
