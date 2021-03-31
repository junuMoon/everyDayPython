from flask import Flask, render_template, request, abort
from ner_client import NerClient

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/ner', methods=['POST'])
def ner():
    try:
        sent = request.form['sentence']
        if len(sent) == 0:
            return render_template('home.html')
        else:
            model = NerClient()
            ents = model.get_ents(sent)
            return render_template('home.html', data=ents)
    except Exception:
        abort(404)
        return ""


if __name__ == "__main__":
    app.run(debug=True)