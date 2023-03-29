from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    print("hello world'!)
    return "Hello, Sevco!"

if __name__ == "__main__":
    app.run(debug=True)

