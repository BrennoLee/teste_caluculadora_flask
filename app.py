from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def primary():
    return render_template('index.html')


@app.route("/calculadora", methods=["POST"])
def calculaEApresenta():
    firtsNumber = request.form['n1']
    secundNumber = request.form['n2']
    operator = request.form['operador']

    return f"Primeiro número {firtsNumber}, segundo número {secundNumber} e o operador é {operator}"



if __name__ == "__main__":
    app.run(debug=True)