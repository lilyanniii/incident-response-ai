import random
from datetime import datetime, timedelta
from models import Incident

services = ["api-gateway", "auth-service", "payment-service", "database", "cache", "notification-service"]

incidents_templates = [
    {
        "title": "Database connection timeout",
        "description": "Production database not accepting new connections, connection pool exhausted",
        "root_cause": "Connection pool limit too low for traffic spike",
        "resolution": "Increased connection pool size from 10 to 50, restarted affected services",
        "tags": ["database", "timeout", "connection-pool"]
    },
    {
        "title": "High API latency",
        "description": "API response times spiked above 5 seconds, users experiencing slow requests",
        "root_cause": "Inefficient database query missing index on frequently queried column",
        "resolution": "Added database index, query time dropped from 4s to 50ms",
        "tags": ["latency", "performance", "database"]
    },
    {
        "title": "Service returning 500 errors",
        "description": "Elevated 500 error rate on multiple endpoints, started after recent deploy",
        "root_cause": "Bad configuration value pushed in latest deployment",
        "resolution": "Rolled back deployment, fixed config value, redeployed",
        "tags": ["500-errors", "deploy", "configuration"]
    },
    {
        "title": "Memory leak causing OOM crashes",
        "description": "Service memory usage growing steadily over time, pods restarting due to OOM",
        "root_cause": "Event listener not being cleaned up, accumulating in memory",
        "resolution": "Fixed event listener cleanup, deployed fix, memory usage stabilized",
        "tags": ["memory", "oom", "leak"]
    },
    {
        "title": "Cache unavailable",
        "description": "Redis cache not responding, all requests falling back to database causing high load",
        "root_cause": "Redis ran out of memory and crashed due to no eviction policy set",
        "resolution": "Set LRU eviction policy, increased Redis memory limit, restarted Redis",
        "tags": ["cache", "redis", "memory"]
    },
]

def generate_incidents(count: int = 100) -> list[Incident]:
    incidents = []

    for i in range(count):
        template = random.choice(incidents_templates)
        service = random.choice(services)
        severity = random.randint(1, 4)
        created_at = datetime.now() - timedelta(days=random.randint(1, 365))
        resolved_at = created_at + timedelta(hours=random.randint(1, 8))

        incident = Incident(
            id=f"INC-{str(i + 1).zfill(4)}",
            title=f"{template['title']} on {service}",
            description=template["description"],
            severity=severity,
            status="resolved",
            service=service,
            root_cause=template["root_cause"],
            resolution=template["resolution"],
            tags=template["tags"],
            created_at=created_at,
            resolved_at=resolved_at
        )
        incidents.append(incident)

    return incidents


if __name__ == "__main__":
    incidents = generate_incidents(100)
    for inc in incidents[:3]:
        print(inc.model_dump())