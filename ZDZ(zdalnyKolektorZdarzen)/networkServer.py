from flask import Flask, jsonify, request
from Logs import Logs
import sqliteConnection

test_string = ""

app = Flask(__name__)

logi = ["log1","log2" ,"log3", "log4"]

@app.route('/api/getlogs', methods=['GET'])
def get_logs():
    # Implement logic to return a list of items
    return jsonify({'items': logi})


@app.route('/api/items', methods=['POST'])
def recive_log():
    print("dostałem posta")
    # Implement logic to create a new item
    json_string = request.json
    print(json_string,"\n")

    json_str_corrected = json_string.replace('\n', '\\n')

    # Create an instance of Log from the corrected JSON string

    log = Logs.from_json(json_str_corrected)
    test_string = log.rule
    print(log.rule,log.description, log.time)
    sqliteConnection.insert_log_db(log)

    # print("jestem przed ifem")
    # print(CLI.print_to_cli, CLI.save_to_db)
    # if CLI.print_to_cli:
    #     # Output the deserialized object
    # if CLI.save_to_db:
    #     print("niby zapis do bazy tututut")

    return jsonify(json_string), 201

if __name__ == '__main__':
    app.run(debug=True)

def run():
    app.run(debug=True)

def printuj():
    print("print z serwera placek")