from flask import Flask, render_template, request, abort
from ner_client import NerClient

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def ner():
    if request.method == 'GET':
        return render_template('home.html')
    if request.method == 'POST':
        try:
            sent = request.form['sentence']
            model = NerClient()
            ents = model.get_ents(sent)['ents']
            return render_template('home.html', ents=ents)
        except Exception:
            abort(404)
            return ""


if __name__ == "__main__":
    app.run(debug=True)