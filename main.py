import time
import yaml
import requests
import time
from collections import defaultdict
from urllib.parse import urlparse

# Function to load configuration from the YAML file
def load_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def get_domain(url):
    parsed_url = urlparse(url)
    return parsed_url.hostname

# Function to perform health checks
def check_health(endpoint):
    url = endpoint['url']
    method = endpoint.get('method', 'GET').upper()
    headers = endpoint.get('headers')
    body = endpoint.get('body')
    jsbody = json.loads(body) if body else None

    try:
        response = requests.request(method, url, headers=headers, json=jsbody, timeout=0.5)
        elapsed_ms = response.elapsed.total_seconds() * 1000
        if elapsed_ms > 500:
            return "DOWN"

        if 200 <= response.status_code < 300:
            return "UP"
        else:
            return "DOWN"
    except requests.RequestException:
        return "DOWN"

# Main function to monitor endpoints
def monitor_endpoints(file_path):
    config = load_config(file_path)
    domain_stats = defaultdict(lambda: {"up": 0, "total": 0})

    while True:
        cycle_start = time.time()
        for endpoint in config:
            domain = get_domain(endpoint["url"])
            result = check_health(endpoint)

            domain_stats[domain]["total"] += 1
            if result == "UP":
                domain_stats[domain]["up"] += 1

        # Log cumulative availability percentages
        for domain, stats in domain_stats.items():
            availability = round(100 * stats["up"] / stats["total"])
            print(f"{domain} has {availability}% availability percentage")

        print("---")
        elapsed = time.time() - cycle_start
        sleep_duration = max(0, 15 - elapsed)
        time.sleep(sleep_duration)

# Entry point of the program
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python monitor.py <config_file_path>")
        sys.exit(1)

    config_file = sys.argv[1]
    try:
        monitor_endpoints(config_file)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
