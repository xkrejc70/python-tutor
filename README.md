# Python tutor

## Flask Server with Nginx Load Balancer and ReactJS Client

This project includes a Flask server, a Nginx load balancer, and a ReactJS client, all orchestrated using Docker Compose. The Flask server is served by Gunicorn, and Nginx acts as a load balancer to distribute requests. The ReactJS client communicates with the Flask API.

## Deployment

### Prerequisites

Make sure you have Docker and Docker Compose installed on your machine.

### Deployment:

1. Set environment:

    ```bash
    ./set-env.sh
    ```

2. Build and run containers:

    ```bash
    docker compose up -d --build --scale flask-app=3
    ```

    This command builds the images, starts containers, and scales the Flask app service to three instances. Adjust the scale value based on your requirements.

3. To stop and remove containers:

    ```bash
    docker compose down
    ```

4. View running containers:

    ```bash
    docker ps
    ```

5. App is running on `http://localhost:3000/`

### Development

For developing there is no need to use Docker and scaling.

1. To run the project for development, use these commands:

```bash
./start-client.sh
```

For client, it changes proxy in `package.json` to `http://localhost:5000` (no use of load balancer)

Frontend is running on `http://localhost:3000/`

```bash
python3 server/flask/run.py
```

Backend is running on `http://localhost:5000/`


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
