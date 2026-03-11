from flask import Flask, jsonify
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    logging.info("Home endpoint accessed")
    return jsonify({"message": "AIRMAN Cloud Ops Service Running"})

@app.route("/health")
def health():
    logging.info("Health check endpoint accessed")
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
