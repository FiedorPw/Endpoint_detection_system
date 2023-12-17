
import json
from datetime import datetime

class Log:
    def __init__(self, rule,description):
        self.description = description
        self.rule = rule
        self.time = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

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
    def from_json(json_str):
        """
        Deserialize a JSON-formatted str to a Log instance.
        """
        data = json.loads(json_str)
        log_instance = Log(data['rule_name'], data['description'])
        log_instance.time = data['time']  # Manually set the time field
        return log_instance


