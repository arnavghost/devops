from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify(message="Hello, Flask from Docker!")

if __name__ == "__main__":
    # Bind to 0.0.0.0 so it's reachable from the container host
    app.run(host="0.0.0.0", port=5000, debug=False)
