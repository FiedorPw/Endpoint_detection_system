'''
GEN.MGMT.5 Wprowadzić komunikację ze Zdalnym Kolektorem Zdarzeń.

GEN.MGMT.5.1 Metodą komunikacji aplikacji głównej ze Zdalnym Kolektorem Zdarzeń alertów jest
REST API.
'''

import requests

def sendRuleDetection(rule_name,description):
    new_item = {'rule_name': rule_name, 'description': description}
    response = requests.post('http://127.0.0.1:5000/api/items', json=new_item)


if __name__ == '__main__':
# GET
    response = requests.get('http://127.0.0.1:5000/api/getlogs')
    print(response.json())
    #post
    new_item = {'name': 'item1', 'description': 'A new item'}
    response = requests.post('http://127.0.0.1:5000/api/items', json=new_item)
    print(response.json())
