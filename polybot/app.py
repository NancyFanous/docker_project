import flask
from flask import request
import os
from bot import ObjectDetectionBot


app = flask.Flask(__name__)

with open("/run/secrets/telegram_token", "r") as f:  #get token from file in the container
    TELEGRAM_TOKEN = f.read().strip()


TELEGRAM_APP_URL = os.environ['TELEGRAM_APP_URL']


@app.route('/', methods=['GET'])
def index():
    return 'Ok'


@app.route(f'/{TELEGRAM_TOKEN}/', methods=['POST'])
def webhook():
    req = request.get_json()
    bot.handle_message(req['message'])
    return 'Ok'


if __name__ == "__main__":
    bot = ObjectDetectionBot(TELEGRAM_TOKEN, TELEGRAM_APP_URL)

    app.run(host='0.0.0.0', port=8443)
