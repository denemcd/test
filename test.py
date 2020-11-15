import json

config_file = open("config.json")
config_data = json.load(config_file)
config_file.close()

dene = {"Userid": config_data["UserID"], "Name": config_data["Username"],
        "Email": config_data["Email"], "apiKey": config_data["apiKey"]}


print(dene["Name"])
