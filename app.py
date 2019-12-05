from flask import Flask
import requests
from flask_jwt import JWT, jwt_required


# Credentials for authorised user to generate a token for authorised API call
USER_DATA = {
    "lunatech": "devops"
}
URL = "http://0.0.0.0:8080/"


app = Flask(__name__)
# Secret key for token
app.config['SECRET_KEY'] = 'luna-secret'


class User(object):
    '''
    User Class setup to handle JWT
    '''
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return "User(id='%s')" % self.id


def verify(username, password):
    if not (username and password):
        return False
    if USER_DATA.get(username) == password:
        return User(id=100)


def identity(payload):
    user_id = payload['identity']
    return {"user_id": user_id}


jwt = JWT(app, verify, identity)


@app.route('/airports', methods=['GET'])
def airports():
    try:
        airports_info = requests.get("http://0.0.0.0:8080/airports", timeout=5).json()
        # print(airports_info)
    except (requests.RequestException, ValueError):
        return ValueError

    # return airports_info[0]["iso_country"]
    keys = [item['id'] for item in airports_info]
    return dict(zip(keys, airports_info))


@app.route('/airports/<query>',  methods=['GET'])
@jwt_required()
def airports_by_country_code(query):
    try:
        aport = requests.get("http://0.0.0.0:8080/airports"/{}.format(query), timeout=5).json()
        # print(airports_info)
    except (requests.RequestException, ValueError):
        return None

    return {
            "id": aport[0]["id"],
            "runways": aport[1]["runways"]
     }


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True)
