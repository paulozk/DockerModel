import flask
from flask import request, render_template, redirect

from src.predict import make_a_prediction
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return render_template("home.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        # Alternatively

        sepal_width = int(request.form["sepal_width"])
        sepal_length = int(request.form["sepal_length"])
        petal_width = int(request.form["petal_width"])
        petal_length = int(request.form["petal_length"])


        prediction = make_a_prediction(sepal_width, sepal_length, petal_width, petal_length)
        return render_template("predict.html", prediction=str(prediction))

        return redirect(request.url)

    return render_template("predict.html")


if __name__ == "__main__":
    app.run(debug=True)
