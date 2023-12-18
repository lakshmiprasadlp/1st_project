from flask import Flask, request, render_template, redirect, url_for
from src.DimondPricePrediction.pipelines.prediction_pipeline import CustomData, PredictPipeline

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
        
        # Redirect to the result page with the result as a parameter
        return redirect(url_for('result_page', final_result=result))

@app.route("/result/<final_result>")
def result_page(final_result):
    return render_template("result.html", final_result=final_result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
