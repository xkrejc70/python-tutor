from app import app
from app.log.logging_config import logging_config

if __name__ == "__main__":
    app.run(debug=True, port=8084)
