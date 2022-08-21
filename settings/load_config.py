import yaml

def load_config() -> dict:
    with open("configuration.yml", 'r') as file:
        data = yaml.safe_load(file)
    return data