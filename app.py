from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Race Analytics Dashboard Running"

@app.route("/api/test")
def test():
    return {"participants": 120, "male": 70, "female": 50}

if __name__ == "__main__":
    app.run(debug=True)
