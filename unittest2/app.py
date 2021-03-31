from flask import Flask, render_template, request
from ner_client import NerClient

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/ner', methods=['POST'])
def ner():
    try:
        sent = request.get_json().get('sentence')
        model = NerClient()
        ents = model.get_ents(sent)
        return ents
    except Exception:
        return ""


if __name__ == "__main__":
    app.run(debug=True)