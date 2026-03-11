from flask import Flask, request, jsonify
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory storage for events
events = []

VALID_SEVERITY = ["info", "warning", "error", "critical"]


# Home endpoint
@app.route("/")
def home():
    return jsonify({
        "message": "AIRMAN Cloud Ops Service Running"
    })


# Health endpoint
@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "service": "skynet-ops-audit-service",
        "environment": "dev",
        "timestamp": datetime.utcnow().isoformat()
    })


# POST /events → create event
@app.route("/events", methods=["POST"])
def create_event():

    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    required_fields = ["type", "tenantId", "severity", "message", "source"]

    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({"error": f"{field} is required"}), 400

    if data["severity"] not in VALID_SEVERITY:
        return jsonify({"error": "Invalid severity"}), 400

    event = {
        "eventId": "evt_" + uuid.uuid4().hex[:12],
        "type": data["type"],
        "tenantId": data["tenantId"],
        "severity": data["severity"],
        "message": data["message"],
        "source": data["source"],
        "metadata": data.get("metadata", {}),
        "occurredAt": data.get("occurredAt", datetime.utcnow().isoformat()),
        "storedAt": datetime.utcnow().isoformat()
    }

    events.append(event)

    return jsonify({
        "success": True,
        "eventId": event["eventId"],
        "storedAt": event["storedAt"]
    }), 201


# GET /events → retrieve events
@app.route("/events", methods=["GET"])
def get_events():

    tenantId = request.args.get("tenantId")
    severity = request.args.get("severity")
    limit = int(request.args.get("limit", 20))
    offset = int(request.args.get("offset", 0))

    filtered_events = events

    if tenantId:
        filtered_events = [e for e in filtered_events if e["tenantId"] == tenantId]

    if severity:
        filtered_events = [e for e in filtered_events if e["severity"] == severity]

    filtered_events = filtered_events[::-1]  # newest first

    result = filtered_events[offset: offset + limit]

    return jsonify({
        "items": result,
        "total": len(filtered_events),
        "limit": limit,
        "offset": offset
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)