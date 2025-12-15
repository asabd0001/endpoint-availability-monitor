# Site Reliability Endpoint Monitor

## Overview
Site Reliability Engineering focuses on maintaining system availability through clear monitoring,
well-defined thresholds, and repeatable operational processes.

This repository contains a redesigned and improved **HTTP endpoint availability monitoring tool**
that periodically checks the health of configured endpoints and reports availability metrics based
on response status and latency thresholds.


## Functionality
The monitor consumes a YAML configuration file that defines a set of HTTP endpoints and their
request parameters. Each endpoint is checked at a fixed interval, and the tool reports whether
the endpoint is **UP** or **DOWN**, along with an aggregate availability percentage.

Checks are performed every **15 seconds**, accounting for request execution time to maintain a
consistent monitoring cadence.

## Availability Criteria
An endpoint is considered **available** if **both** of the following conditions are met:

- The HTTP response status code is in the **200–299** range
- The response time is **≤ 500 ms**

## Installation

### Requirements
- Python 2.7 or later

### Dependencies
Install required Python packages:
```bash
pip install requests
pip install pyyaml
