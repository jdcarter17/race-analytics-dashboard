from flask import Flask

@app.route("/api/test")
def test():
    return {"participants": 120, "male": 70, "female": 50}

app = Flask(__name__)

@app.route("/")
def home():
    return "Race Analytics Dashboard Running"

if __name__ == "__main__":
    app.run(debug=True)
