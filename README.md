TODO

server - flask
load balancer - nginx
client - react

Deploy:
docker compose up -d --build --scale flask-app=3
docker compose down
docker ps

"proxy": "http://nginx:4000",

Develop:
./start.sh