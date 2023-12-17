from openai import OpenAI

api_key = "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"
data_path = "data/proj4_data_1.jsonl"

client = OpenAI(api_key=api_key)


file = client.files.create(
  file=open(data_path, "rb"),
  purpose="fine-tune"
)

print(f"File ID: {file.id}, File status: {file.status}")

job = client.fine_tuning.jobs.create(
  training_file=file.id, 
  model="gpt-3.5-turbo-1106"
)

print(f"Job ID: {job.id}, Job status: {job.status}")