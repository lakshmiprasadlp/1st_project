import streamlit as st
import joblib
import numpy as np
import sklearn

from src.DimondPricePrediction.pipelines.prediction_pipeline import CustomData, PredictPipeline

"""
@author: lp
"""
def main():
    html_temp = """
    <div style="background-color:lightblue;padding:16px">
    <h2 style="color:black";text-align:center> Dimond Price Prediction </h2>
    </div>"""

    st.markdown(html_temp, unsafe_allow_html=True)

    carat = st.slider("Enter your carat", 0.0, 4.0, step=0.1)
    
    depth = st.slider("Enter your depth", 50.0, 72.0, step=0.1)

    table = st.slider("Enter the table ", 50.0, 80.0, step=0.1)
    
    
    x = st.slider("Enter the x ", 0.00, 10.00, step=0.01)

    y = st.slider("Enter the y ", 0.00, 10.00, step=0.01)

    z = st.slider("Enter the z ", 0.00, 32.00, step=0.01)

    cut_map = {"Fair": 1, "Good": 2, "Very Good": 3, "Premium": 4, "Ideal": 5}
    cut = st.selectbox("Select the cut ", list(cut_map.keys()))

    color_map = {"D": 1, "E": 2, "F": 3, "G": 4, "H": 5, "I": 6, "J": 7}
    color = st.selectbox("Select the Color ", list(color_map.keys()))

    clarity_map = {"I1": 1, "SI2": 2, "SI1": 3, "VS2": 4, "VS1": 5, "VVS2": 6, "VVS1": 7, "IF": 8}
    clarity = st.selectbox("Select the clarity ", list(clarity_map.keys()))

    


    model = joblib.load("artifacts\model.pkl")

    # Map categorical features to numerical values
    cut_num = cut_map[cut]
    color_num = color_map[color]
    clarity_num = clarity_map[clarity]

    if st.button("Predict"):
        
        pre = model.predict([[carat, depth, table, x, y, z,cut_num, color_num, clarity_num]])
        st.success("Your Diamond Cost is {}".format(pre[0]))


if __name__ == '__main__':
    main()
