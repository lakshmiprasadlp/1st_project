# Folder Structure:
# /your_project
#   /src
#       /DimondPricePrediction
#           /pipelines
#               /prediction_pipeline.py
#   /static
#       /css
#           style.css
#   /templates
#       index.html
#       form.html
#       result.html
#   app.py

# app.py

from src.DimondPricePrediction.pipelines.prediction_pipeline import CustomData, PredictPipeline
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
def predict_datapoint():
    if request.method == "GET":
        return render_template("form.html")
    else:
        data = CustomData(
            carat=float(request.form.get('carat')),
            depth=float(request.form.get('depth')),
            table=float(request.form.get('table')),
            x=float(request.form.get('x')),
            y=float(request.form.get('y')),
            z=float(request.form.get('z')),
            cut=request.form.get('cut'),
            color=request.form.get('color'),
            clarity=request.form.get('clarity')
        )
        final_data = data.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(final_data)
        result = round(pred[0], 2)
        return render_template("result.html", final_result=result)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)

# style.css

/* static/css/style.css */
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
    margin: 0;
    padding: 0;
}

.container {
    max-width: 600px;
    margin: 20px auto;
    background-color: #fff;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

form {
    display: flex;
    flex-direction: column;
}

button {
    background-color: #4caf50;
    color: #fff;
    border: none;
    padding: 10px;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #45a049;
}

/* Add more styles as needed */

# index.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    <title>Your App</title>
</head>
<body>
    <div class="container">
        <!-- Your content here -->
    </div>
</body>
</html>

# form.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    <title>Your Form</title>
</head>
<body>
    <div class="container">
        <!-- Your form content here -->
    </div>
</body>
</html>

# result.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    <title>Your Result</title>
</head>
<body>
    <div class="container">
        <!-- Your result content here -->
    </div>
</body>
</html>
