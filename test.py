import json

config_file = open("config.json")
config_data = json.load(config_file)
config_file.close()

print(config_data)
