from openai import OpenAI
import json


with open("train_data/config.json", "r") as config_file:
    config = json.load(config_file)

# Extract data_path from the config
data_path = config.get("data_path", "")
api_key = config.get("api_key", "")
suffix_name = config.get("suffix_name", "")
model_name = config.get("model_name", "")

client = OpenAI(api_key=api_key)


file = client.files.create(
  file=open(data_path, "rb"),
  purpose="fine-tune"
)

print(f"File ID: {file.id}, File status: {file.status}")

job = client.fine_tuning.jobs.create(
  training_file=file.id, 
  model=model_name,
  suffix=suffix_name
)

print(f"Job ID: {job.id}, Job status: {job.status}")