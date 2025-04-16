## Arshia Sabdar

# Site Reliability Endpoint Monitor

## Description:
As Site Reliability Engineers, it is our job to not only identify issues that will impact the reliability 
of systems, but also develop processes and procedures that will make it easier for others to do 
the same work in the future. This repo contains a reevaluated and improved code for an enpoint monintor

This code will get a YAML file as an input containing a domain enpoints URLs, methods, bodies of the request
then periodically (every 15 seconds) will check if the endpoints are UP or DOWN and print the site availability
percentage as output.

### An endpoint is considered available if
* The request responds with HTTP codes 200-299
<br/>AND
* The resonse time is less than or equal to 500 ms


## Installation
Python 2 or above
<br/> Python packages required:
<br/> requests:
```pip install requests```
<br/> yaml:
```pip install pyyaml```


## Run the Code:
Run main.py as following:

    python main.py domain.yaml

where domain.yaml is a YAML file containing the endpoints of the domain 
with the format explained below.


## YAML File Format:

    name  (string, required) — A free-text name to describe the HTTP endpoint. 
    url  (string, required) — The URL of the HTTP endpoint. -  
        You may assume that the URL is always a valid HTTP or HTTPS address. 
    method  (string, optional) — The HTTP method of the  endpoint. -  
        If this field is present, you may assume it’s a valid HTTP method (e.g. GET, POST, etc.). -  
        If this field is omitted, the default is GET. 
    headers  (dictionary, optional) — The HTTP headers  to include in the request. -  
        If this field is present, you may assume that the keys and values of this dictionary are 
        strings that are valid HTTP header names and values. -  
        If this field is omitted, no headers need to be added to or modified in the HTTP request. 
    body  (string, optional) — The HTTP body to include in the request. -  -  
        If this field is present, you should assume it's a valid JSON-encoded string. 
        If this field is omitted, no body is sent in the request

## Issues Fixed:
* Default method GET was not set in the code causing None method.
* Request timeout was not set to 500 ms.
* Response elapsed time was not measured or checked against 500 ms.
* Request body was not converted to string JSON
* Improper domain name extraction, it is better to use urlparse
* The check cycles to be 15 seconds regardless of endpoints needed a change as the response delay wasn't 
      taken into account

