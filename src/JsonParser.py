import json

class JsonParser():

    def __init__(self, json_file):
        self.json_file = json_file
	with open(json_file) as file:
            self.json_contents = json.load(file)
    
    def get(self):
        return self.json_contents
