import requests

# GET
response = requests.get('http://127.0.0.1:5000/api/getlogs')
print(response.json())

#post
new_item = {'name': 'item1', 'description': 'A new item'}
response = requests.post('http://127.0.0.1:5000/api/items', json=new_item)
print(response.json())
