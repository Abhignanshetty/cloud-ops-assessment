Operations Runbook

Service:
skynet-ops-audit-service

Start Service:
Run ECS task in airman-cluster.

Stop Service:
Stop running ECS tasks.

Health Check:
GET /health

Logs:
Available in Amazon CloudWatch.

Troubleshooting:
- Check ECS task status
- Verify container logs
- Ensure port 5000 is open in security group