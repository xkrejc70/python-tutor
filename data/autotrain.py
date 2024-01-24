"""
autotrain llm --train --project-name mistral-proj8 --model teknium/OpenHermes-2.5-Mistral-7B --data-path hojzas/proj8-chatML --use-peft --quantization int4 --lr 2e-4 --train-batch-size 12 --epochs 3 --trainer sft --push-to-hub --token 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 --repo-id hojzas/proj8-mistral-new > training.log
"""

from datasets import load_dataset 

# Load the dataset

"""
dataset = load_dataset("hojzas/proj8-chatML") 
train = dataset['train']

train.to_csv('train2.csv', index = False)
"""

# parametes
project_name = 'my-mommygpt'
model_name = 'hakurei/mommygpt-3B'
push_to_hub = True
hf_token = "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"
repo_id = "hojzas/my-mommygpt"

learning_rate = 2e-4
num_epochs = 3
batch_size = 25 # dataset size
block_size = 128
trainer = "sft"
warmup_ratio = 0.1
weight_decay = 0.01
gradient_accumulation = 4
use_fp16 = True
use_peft = True
use_int4 = True
lora_r = 16
lora_alpha = 32
lora_dropout = 0.045

command = [
    "autotrain", "llm",
    "--train",
    "--model", model_name,
    "--project-name", project_name,
    "--data-path", "./data/",
    "--text-column", "text",
    "--lr", str(learning_rate),
    "--batch-size", str(batch_size),
    "--epochs", str(num_epochs),
    "--block-size", str(block_size),
    "--warmup-ratio", str(warmup_ratio),
    "--lora-r", str(lora_r),
    "--lora-alpha", str(lora_alpha),
    "--lora-dropout", str(lora_dropout),
    "--weight-decay", str(weight_decay),
    "--gradient-accumulation", str(gradient_accumulation),
]

# Add optional flags based on conditions
if use_fp16:
    command.extend(["--mixed-precision", "fp16"])
if use_peft:
    command.append("--use-peft")
if use_int4:
    command.extend(["--quantization", "int4"])
if push_to_hub:
    command.extend(["--push-to-hub", "--token", hf_token, "--repo-id", repo_id])

import subprocess

# Convert the command list to a space-separated string
full_command = ' '.join(command)

# Run the command
subprocess.run(full_command, shell=True)