# Python tutor

![xkrejc70_poster](https://github.com/xkrejc70/python-tutor/assets/95762954/1fa6603a-c091-4038-87ac-8f2168fff012)


## Flask Server with Nginx Load Balancer and ReactJS Client

This project includes a Flask server, a Nginx load balancer, and a ReactJS client, all orchestrated using Docker Compose. The Flask server is served by Gunicorn, and Nginx acts as a load balancer to distribute requests. The ReactJS client communicates with the Flask API.

## Deployment

### Prerequisites

Make sure you have Docker and Docker Compose installed on your machine.

### Deployment:

2. Build and run containers:

    ```bash
    docker compose up -d --build
    ```

    This command builds the images, starts containers

3. To stop and remove containers:

    ```bash
    docker compose down
    ```

4. View running containers:

    ```bash
    docker ps
    ```

### Development

For developing there is no need to use Docker.

#### Frontend

For client, it needs to change `API_BASE_URL` to LOCALHOST

To start client frontend, run:

```bash
npm install && npm start
```

#### Backend

To start flask servers, navigate to each server directory (`/server/{falsk, model, test}`) and run:

```bash
pip install -r requirements.txt
flask run || python3 server/[servername]/[main_file].py
```

## Fine-tuning

1. Edit config for fine-tuning in `data/config.json`

2. Check laoding and format

```bash
python3 data/fine_tuning_data_validation.py
```
3. Start fine-tuning

```bash
python3 data/fine_tuning.py
```

Convert yaml to jsonl:

```bash
python3 convert_yaml_to_jsonl.py train_data.yaml train_data.jsonl
```
