from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Ciao, mondo! Questa è una semplice applicazione Flask.</h1>"

@app.route('/saluto/<nome>')
def saluto(nome):
    return jsonify({'messaggio':f'Ciao, {nome}'})

if __name__ == '__main__':
    app.run(debug=True)