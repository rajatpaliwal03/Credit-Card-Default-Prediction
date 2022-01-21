from flask import Flask,render_template,url_for,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/predict', methods=["GET","POST"])
def predict():
    if request.method == "POST":
        rawtext = request.form["rawtext"]
    return render_template("index.html", rawtext=rawtext.upper())


if __name__ == '__main__':
    app.run(debug=True)
