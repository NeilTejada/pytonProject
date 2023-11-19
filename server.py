from flask import Flask

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello from Flask!"

app.run(debug=True)