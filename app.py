
from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)
model = joblib.load("model.pkl")

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        income = float(request.form["income"])
        loan = float(request.form["loan"])
        features = np.array([[income, loan]])
        prediction = model.predict(features)
        result = "✅ Loan Approved!" if prediction[0] == 1 else "❌ Loan Rejected."
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)

