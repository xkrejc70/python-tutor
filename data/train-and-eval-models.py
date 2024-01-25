from datasets import load_dataset
from setfit import SetFitModel, SetFitTrainer, sample_dataset
from sentence_transformers.losses import CosineSimilarityLoss
import time

# Define a list of model IDs to iterate over
model_ids_old = [
    "sentence-transformers/paraphrase-mpnet-base-v2",
    "sentence-transformers/all-mpnet-base-v2",
    "sentence-transformers/all-MiniLM-L6-v2",
    "sentence-transformers/all-MiniLM-L12-v2",
    "sentence-transformers/distiluse-base-multilingual-cased-v2",
    "flax-sentence-embeddings/st-codesearch-distilroberta-base",
    "intfloat/multilingual-e5-large",
    "intfloat/e5-small-v2",
    "intfloat/e5-large-v2",
    "krlvi/sentence-msmarco-bert-base-dot-v5-nlpl-code_search_net",
    "AISE-TUDelft/python-summary-classifier",
    "AISE-TUDelft/python-usage-classifier"
]

model_ids = [
    "krlvi/sentence-msmarco-bert-base-dot-v5-nlpl-code_search_net",
    "AISE-TUDelft/python-summary-classifier",
    "AISE-TUDelft/python-usage-classifier"
]

dataset_id = "hojzas/proj8-label2"
dataset_valid_id = "hojzas/proj8-label-validation"

dataset = load_dataset(dataset_id)
train_dataset = dataset["train"]
print(train_dataset)

dataset = load_dataset(dataset_valid_id)
eval_dataset = dataset["validation"]
print(eval_dataset)

# Open a file for writing metrics
with open("metrics_output_2.txt", "w") as file:
    # Iterate over the list of model IDs
    for model_id in model_ids:
        
        # Load the model
        model = SetFitModel.from_pretrained(model_id)

        # Create a new trainer for each model
        trainer = SetFitTrainer(
            model=model,
            train_dataset=train_dataset,
            eval_dataset=eval_dataset,
            loss_class=CosineSimilarityLoss,
            num_iterations=20,
            column_mapping={"sentence": "text", "label": "label"},
        )

        # Record start time
        start_time = time.time()

        # Train the model
        trainer.train()

        # Record end time
        end_time = time.time()

        # Calculate duration
        duration = round(end_time - start_time, 2)

        # Evaluate the model
        metrics = trainer.evaluate()
        
        # Write the metrics to the file
        file.write(f"{metrics} (dur: {duration}): {model_id}\n")
