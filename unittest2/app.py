from flask import Flask, render_template, request
from ner_client import NerClient
import json

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/ner', methods=['POST'])
def ner():
    try:
        data = json.loads(request.get_data())
        if len(data) == 0:
            return ""
        else:
            return data.get('data')
    except Exception:
        return ""




if __name__ == "__main__":
    app.run(debug=True)