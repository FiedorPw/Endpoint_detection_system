from flask import Flask, jsonify, request

app = Flask(__name__)

logi = ["cynk by elkaSysMon","bieniasz zapodał projekt" ,"sepczuk zhakował windowsa", "komandos uwalił 69% ludzi"]

@app.route('/api/getlogs', methods=['GET'])
def get_logs():
    # Implement logic to return a list of items
    return jsonify({'items': logi})

@app.route('/api/items', methods=['POST'])
def create_item():
    # Implement logic to create a new item
    item = request.json
    print(item)
    return jsonify(item), 201

if __name__ == '__main__':
    app.run(debug=True)
