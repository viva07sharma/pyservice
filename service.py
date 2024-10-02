import sys
from flask import Flask, jsonify
from werkzeug.security import gen_salt

serverhost="0.0.0.0"
app = Flask(__name__)

@app.route('/register_client', methods=['POST'])
def register_client():
    # Generate a unique client ID and secret
    client_id = gen_salt(32)
    client_secret = gen_salt(48)

    # Return the generated client ID and secret as JSON
    return jsonify({"client_id": client_id, "client_secret": client_secret}), 201


if __name__ == '__main__':
    #development mode
    if sys.argv[1] == "dev":
        app.run(host=serverhost, port=22000, debug = True)

    #production
    if sys.argv[1] == "prod":
        from waitress import serve
        serve(app, host=serverhost, port=22000)


#run via -> python service.py prod