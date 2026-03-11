from flask import Flask, jsonify
import logging
import sys

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    stream=sys.stdout,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

@app.route("/")
def home():
    print("Home endpoint accessed")
    logging.info("Home endpoint accessed")
    return jsonify({"message": "AIRMAN Cloud Ops Service Running"})

@app.route("/health")
def health():
    print("Health check endpoint accessed")
    logging.info("Health check endpoint accessed")
    return jsonify({"status": "healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)