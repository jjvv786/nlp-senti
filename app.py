from flask import Flask, render_template, request
import joblib

txb = joblib.load("txb.pkl")

app = Flask(__name__)

@app.route("/")
def function():
    return render_template("bindex.html")

@app.route("/sub", methods=['POST'])
def submit():
    if request.method == "POST":
        sen = request.form["sen"]
        dt = txb(sen)
        finalPrediction=dt.sentiment.polarity
    
        if finalPrediction < 0:
          return render_template("ion.html",  finalResult="Negative")
        elif finalPrediction == 0:
          return render_template("ion.html",  finalResult="Neutral")
        else:
          return render_template("ion.html",  finalResult="Possitive")

if __name__ == "__main__":
    app.run(debug=True)