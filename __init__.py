from flask import Flask
from pip import main
app = Flask(__name__)

@app.route('/')
def Hey():
    return "hello wold"

if __name__ == "__main__":
    app.run(debug=True)