from flask import Flask, render_template, request, abort, make_response
from ner_client import NerClient
import uuid

app = Flask(__name__)
app.secret_key = 'double'
model = NerClient()


@app.route('/', methods=['GET'])
def index():
    response = make_response(render_template('home.html'))
    # userId = {'userId': 'fakeID'}
    response.set_cookie('userID', 'fakeID')
    return response


@app.route('/ner', methods=["POST"])
def ner():
    try:
        sent = request.form['sentence']
        ents = model.get_ents(sent)['ents']
        return render_template('home.html', ents=ents)
    except Exception:
        abort(404)
        return ""


if __name__ == "__main__":
    app.run(debug=True)