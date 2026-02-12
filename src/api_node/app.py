from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    if request.method == "GET":
        diction = {
            1 : "hello world",
            2 : ["a!",True,22.32]
        }
        return jsonify(diction)
    else: return "Hello world"

if __name__ == "__main__":
    app.run(debug=True)

print("hello world")