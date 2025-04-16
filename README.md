DESCRIPTION:

As a Site Reliability Engineer, it is our job to not only identify issues that will impact the reliability 
of systems, but also develop processes and procedures that will make it easier for others to do 
the same work in the future. 
This code will get a YAML file as an input containing a domain enpoints URLs, methods, bodies of the request
then periodically (every 15 seconds) will check if the endpoints are UP or DOWN and print the site availability
percentage as output.

The criteria for availability is that:
    - The request should respond with HTTP codes 200-299 AND
    - The resonse time is less than or equal to 500 ms


INSTALLATION:

    - Python 2 or above
    - Python packages required:
        - requests: pip install requests
        - yaml: pip install pyyaml


RUN THE CODE:
    - Run main.py as following:

    python main.py domain.yaml

    where domain.yaml is a YAML file containing the endpoints of the domain with the format explained below.


YAML FILE FORMAT:

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

ISSUES FIXED:

    - Default method GET was not set in the code causing None method.
    - Response elapsed time was not measured or checked against 500 ms

