import flask
from flask import request, render_template, redirect

from src.model_predict import model_predict
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return render_template("home.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        # Alternatively

        sepal_length = int(request.form["sepal_length"])
        sepal_width = int(request.form["sepal_width"])
        petal_length = int(request.form["petal_length"])
        petal_width = int(request.form["petal_width"])

        prediction = model_predict([sepal_length, sepal_width, petal_length, petal_width])
        return render_template("predict.html", prediction=str(prediction))

        #return redirect(request.url)

    return render_template("predict.html")


if __name__ == "__main__":
    app.run(debug=True)
