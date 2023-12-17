'''
GEN.MGMT.5 Wprowadzić komunikację ze Zdalnym Kolektorem Zdarzeń.

GEN.MGMT.5.1 Metodą komunikacji aplikacji głównej ze Zdalnym Kolektorem Zdarzeń alertów jest
REST API.
'''
from Log import Log
import requests

def sendRuleDetection(rule_name,description):
    new_item = {'rule_name': rule_name, 'description': description}
    response = requests.post('http://127.0.0.1:5000/api/items', json=new_item)




def sendLogObject(log_json):
    response = requests.post('http://127.0.0.1:5000/api/items', json=log_json)



if __name__ == '__main__':
# GET
    response = requests.get('http://127.0.0.1:5000/api/getlogs')
    print(response.json())
    #post
    new_item = Log("dupa","placek")
    json_log = new_item.to_json()
    response = requests.post('http://127.0.0.1:5000/api/items', json=json_log)
    print(response.json())