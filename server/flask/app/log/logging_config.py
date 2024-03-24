import os
from logging.config import dictConfig

debug_log = os.path.join("logs", "debug.log")
os.makedirs(os.path.dirname(debug_log), exist_ok=True)
FORMAT = '%(asctime)s : %(levelname)s : %(name)s : %(message)s'

logging_config = {
    'version': 1,
    'formatters': {
        'standard': {
            'format': FORMAT,
        },
    },
    'handlers': {
        'file.handler': {
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': debug_log,
            'maxBytes': 10000000,
            'backupCount': 5,
            'level': 'DEBUG',
            'formatter': 'standard',
        },
    },
    'root': {  # Configuring the root logger
        'level': 'DEBUG',
        'handlers': ['file.handler'],
    },
}

dictConfig(logging_config)  # Configure logging
