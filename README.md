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
    docker-compose down
    ```

4. View running containers:

    ```bash
    docker ps
    ```

5. App is running on `http://localhost:3000/`

### Development

For developing there is no need to use Docker and scaling.

1. To run the project for development, use tese commands:

```bash
./start-client.sh
```

For client, It changes proxy in `package.json` to `http://localhost:5000`

Frontend is running on `http://localhost:3000/`

```bash
python3 server/app/wsgi.py
```

Backend is running on `http://localhost:5000/`
