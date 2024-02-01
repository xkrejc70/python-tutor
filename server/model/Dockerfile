FROM python:3.9-slim
WORKDIR /app

COPY . .
RUN pip install -r requirements.txt

#EXPOSE 6000
CMD gunicorn --bind 0.0.0.0:6000 app:app