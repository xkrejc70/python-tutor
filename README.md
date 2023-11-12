# Python tutor

## Flask Server with Nginx Load Balancer and ReactJS Client

This project includes a Flask server, a Nginx load balancer, and a ReactJS client, all orchestrated using Docker Compose. The Flask server is served by Gunicorn, and Nginx acts as a load balancer to distribute requests. The ReactJS client communicates with the Flask API.

## Deployment

### Prerequisites

Make sure you have Docker and Docker Compose installed on your machine.

Make sure proxy in `package.json` is set to `http://localhost:5000"`

### To Deploy:

1. Build and run the containers:

    ```bash
    docker-compose up -d --build --scale flask-app=3
    ```

    This command builds the images, starts the containers, and scales the Flask app service to three instances. Adjust the scale value based on your requirements.

2. To stop and remove the containers:

    ```bash
    docker-compose down
    ```

3. View running containers:

    ```bash
    docker ps
    ```

### Development

To run the project for development, use the provided start script:

```bash
./start.sh
```

Make sure proxy in `package.json` is set to `"http://nginx:4000"`
