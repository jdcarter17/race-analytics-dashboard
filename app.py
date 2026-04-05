from flask import Flask
import plotly.express as px
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return "Race Analytics Dashboard Running"

@app.route("/chart")
def chart():
    df = pd.read_csv("Participants_2026.csv")

    fig = px.bar(df, x="gender", y="count", title="Participants by Gender (2026)")
    chart_html = fig.to_html(full_html=False, include_plotlyjs='cdn')

    return f"""
    <html>
    <head>
        <title>Race Analytics Dashboard</title>
    </head>
    <body>
        <h1>Race Analytics Dashboard</h1>
        <h2>Participant Distribution by Gender</h2>
        {chart_html}
    </body>
    </html>
    """ 
    
if __name__ == "__main__":
    app.run(debug=True)
