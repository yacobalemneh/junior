import os
import json

def load_json_file(file_path):
    """
    Loads a JSON file from the given file path.
    """
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def save_json_file(file_path, data):
    """
    Saves the given data as a JSON file to the given file path.
    """
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def get_config_file_path(file_name):
    """
    Returns the file path for the given config file name.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_dir = os.path.join(current_dir, '..', 'config')
    file_path = os.path.join(config_dir, file_name)
    return file_path