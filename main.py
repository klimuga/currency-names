import requests
import math
import flask
import json
from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello():
    text = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').text
    currencies = json.loads(text)
    result = ''
    for currency in currencies['Valute']:
        result += str(currency) + '<br>'
    return result


if __name__ == "__main__":
    app.run()
