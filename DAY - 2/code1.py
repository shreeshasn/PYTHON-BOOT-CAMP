from flask import Flask
import printing as p

app = Flask(__name__)

@app.route("/hi")

def home():
    return  "Hello, Flask is actually interesting!!! \n"

if __name__ == "__main__":
    app.run(debug=True)

    
