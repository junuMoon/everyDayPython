from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def hello_whale():
    dummy_dict = {
        'Whale': 'Ballena',
        'Banana': 'Platano',
        'Book': 'Libro'
    }
    return render_template('./index.html', spanish_dictionary=dummy_dict)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
