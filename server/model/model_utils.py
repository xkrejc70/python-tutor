from datasets import load_dataset
import os
from setfit import SetFitModel, SetFitTrainer, sample_dataset
from sentence_transformers.losses import CosineSimilarityLoss

def save_locally():
    model_id = "hojzas/proj8-lab2"
    save_directory = "./models/proj8/"

    os.makedirs(save_directory, exist_ok=True)

    model = SetFitModel.from_pretrained(model_id)
    model._save_pretrained(save_directory)

def load():
    model_directory = "./models/proj8/"

    model = SetFitModel._from_pretrained(model_directory)

    preds = model(
	    [
		"""
            def first_with_given_key(iterable, key = lambda x: x):
                seen = set()
                for x in iterable:
                    if repr(key(x)) not in seen:
                        seen.add(repr(key(x)))
                        yield x
		"""
        ]
    )
    print(preds)

# save_locally()
# load()