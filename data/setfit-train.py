from datasets import load_dataset
from setfit import SetFitModel, SetFitTrainer, sample_dataset
from sentence_transformers.losses import CosineSimilarityLoss

dataset_id = "hojzas/proj8-label2"
model_id = "sentence-transformers/paraphrase-mpnet-base-v2"

dataset = load_dataset(dataset_id)
dataset

# train_dataset = sample_dataset(dataset["train"])
train_dataset = dataset["train"]
print(train_dataset)

model = SetFitModel.from_pretrained(model_id)


trainer = SetFitTrainer(
    model=model,
    train_dataset=train_dataset,
    loss_class=CosineSimilarityLoss,
    num_iterations=20,
    column_mapping={"sentence": "text", "label": "label"},
)

trainer.train()
trainer.push_to_hub("hojzas/setfit-proj8", use_auth_token="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")