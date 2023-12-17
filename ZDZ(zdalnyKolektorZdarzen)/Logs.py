import json
from datetime import datetime

class Logs:
    def __init__(self, rule, description, time):
        self.rule = rule
        self.description = description
        self.time = time

    @staticmethod
    def _process_description(description_str):
        """
        Split description into an array of strings, removing newline symbols.
        """
        return description_str.strip().split('\n')

    def to_json(self):
        """
        Serialize the Log instance to a JSON-formatted str.
        """
        return json.dumps({
            'rule_name': self.rule,
            'description': self.description,
            'time': self.time
        })

    @staticmethod
    def from_json(json_data):
        """
        Deserialize a JSON-formatted str to a Log instance.
        """
        data = json.loads(json_data)
        return Logs(data['rule_name'], data['description'], data['time'])

