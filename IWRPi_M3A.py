### Interfacing With the Raspberry Pi
## MODULE 3 
# Peer-graded Assignment: Use the http.client package to read the contents of the 
# www.uci.edu top level web page and print out the first 3 lines. You will need to use 
# http.client.HTTPSConnection() to make the connection to the www.uci.eduweb page. 
# Then you will need to use conn.request("GET", "/") to send the get request. 
# Then use conn.getresponse() to extract the response and use the read() method of the 
# response to return the contents of the webpage.

import http.client
conn = http.client.HTTPConnection("www.uci.edu") # performs DNS Lookup and establishes connection
conn.request("GET", "/") # sends request w/ key details and composes message and sends
response = conn.getresponse() # gets response 
print(response.status, response.reason) # Status code and reason phrase returned by server 
data = response.read()
print(data)