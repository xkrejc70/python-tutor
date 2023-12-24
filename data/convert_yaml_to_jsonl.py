import sys
import yaml
import json

def yaml_to_jsonl(yaml_content):
    jsonl_messages = []

    for i in range(0, len(yaml_content), 2):
        assistant_text = yaml_content[i]['assistant']
        user_content = yaml_content[i + 1]['user'].strip()

        jsonl_message = {
            "messages": [
                {"role": "system", "content": ""},
                {"role": "user", "content": user_content},
                {"role": "assistant", "content": assistant_text}
            ]
        }

        jsonl_messages.append(json.dumps(jsonl_message))

    return jsonl_messages

def main(yaml_file_path, jsonl_file_path):
    with open(yaml_file_path, "r") as yaml_file:
        yaml_content = yaml.load(yaml_file, Loader=yaml.FullLoader)

    with open(jsonl_file_path, "w") as jsonl_file:
        for jsonl_message in yaml_to_jsonl(yaml_content):
            jsonl_file.write(jsonl_message + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert_yaml_to_jsonl.py <input_yaml_file> <output_jsonl_file>")
        sys.exit(1)

    input_yaml_file = sys.argv[1]
    output_jsonl_file = sys.argv[2]

    main(input_yaml_file, output_jsonl_file)
