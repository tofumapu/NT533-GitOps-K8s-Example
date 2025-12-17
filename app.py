from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <h1>Nhom09 - Test Python!</h1>
    <p>Current Date & Time:</p>
    <h2>{now}</h2>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
