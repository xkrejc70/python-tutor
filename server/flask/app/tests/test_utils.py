from app import app
import yaml
import os

MODELS = 'tips.yaml'
CONFIG = 'config'

# Model and Test urls
class Url:
    # TODO:production
    MODEL = 'http://localhost:5050'
    TEST = 'http://localhost:5080'

def load_tips_from_yaml(project, category):
    file_p = os.path.join(CONFIG, MODELS)
    with open(file_p, 'r') as file:
        tips_data = yaml.safe_load(file)
    
    # Check if the project and category exist in the loaded data
    if project in tips_data and category in tips_data[project]:
        return tips_data[project][category]
    
    return None
