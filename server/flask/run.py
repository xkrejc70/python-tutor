from app import app
import os
import logging

debug_log = os.path.join("logs", "debug.log")
FORMAT = '%(asctime)s : %(levelname)s : %(name)s : %(message)s'
logging.basicConfig(filename=debug_log, level=logging.DEBUG, format=FORMAT)

if __name__ == "__main__":
    app.run(debug=True, port=8084)