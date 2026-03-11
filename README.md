# AIRMAN Cloud Ops Assessment

## Project Overview
This project demonstrates a containerized cloud service using Python Flask and Docker.

The service exposes two endpoints:

- `/` → returns service message
- `/health` → returns health status

## Tech Stack
- Python (Flask)
- Docker
- Docker Compose
- WSL (Ubuntu)
- VS Code

## Run the service

Build and run:

## Architecture

Client
   ↓
HTTP Request
   ↓
Flask API (app.py)
   ↓
Docker Container
   ↓
Amazon ECR
   ↓
Amazon ECS Fargate
   ↓
CloudWatch Logs


## Endpoints

GET /health
Returns service health status.

Example:
http://13.204.63.134:5000/health

POST /events
Creates a new event record.

GET /events
Returns stored events.

## Example API Calls

Create Event

curl -X POST http://13.204.63.134:5000/events \
-H "Content-Type: application/json" \
-d '{
"type":"roster_update",
"tenantId":"academy_001",
"severity":"info",
"message":"test event",
"source":"skynet-api"
}'

Get Events

curl http://13.204.63.134:5000/events

## Deployment

The service is containerized using Docker and deployed to AWS ECS Fargate.

Steps performed:
1. Build Docker image
2. Push image to Amazon ECR
3. Create ECS cluster
4. Run ECS task
5. Expose service via public IP

## Logging

Application logs are available in AWS CloudWatch Logs.

This allows monitoring and debugging of running containers.

## Proof of Deployment

Below are screenshots showing the service running successfully on AWS ECS Fargate.

Health Endpoint:
http://13.204.63.134:5000/health

Events Endpoint:
http://13.204.63.134:5000/events