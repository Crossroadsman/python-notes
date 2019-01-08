import requests
"""
Requests
========
HTTP Request library

Documentation: http://docs.python-requests.org/en/master/
GitHub project: https://github.com/requests/requests
"""

r = requests.get('http://some_url.com')  # returns a Request object

r.status_code  # 200

r.ok  # True

r.headers # a dictionary of all the request's response headers


# Request Content
# requests.<action> returns a `requests.models.Response` object.
# this object has a request attribute, through which we can see the
# `requests.models.PreparedRequest` object.
r = requests.get('http://api.github.com/events')

req = r.request
req.body   # The request body, if applicable (e.g., POST)
req.headers  # A dict containing the http request headers
req.method  # The HTTP method
req.path_url  # The part of the url after the hostname
req.url  # The full URL (including protocol and path)


# Response Content
r.encoding  # a string representing the encoding (requests deduces this from the headers)
r.text  # a string version of the content decoded from raw data. Most unicode charsets can be seamlessly decoded. You can override requests' guess by setting the value of .encoding
r.content  # a bytestring representing the content (use for binary objects or for searching for the correct encoding in a text payload where the encoding doesn't match the headers)
r.raw  # the raw socket response (need to set stream=True when making the request)
r.json()  # Use requests' built-in json decoder to convert to a Python dict/list combo


# POST
r = requests.post('https://httpbin.org/post', data = {'key':'value'})




# You can pass a dictionary of parameters to a requests request.
# If you pass it as `params` it will be turned into a query string in the url
# if you pass it as `data` it will be included in the request body
# (and will handle the url encoding)
payload = {
    'content': 'This is my content for submitting in a POST request',
    'user_id': 12345}


payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('https://httpbin.org/get', params=payload)

r = requests.post('https://httpbin.org/post, data=payload)


You can use list-type params as follows:
payload = {
    'posts[]': [123, 456]
}


# You can view redirect history using r.history
r = requests.get('https://httpbin.org/redirect/3')  # redirect 3 times
r.status_code  # will be 200 because the final request ended with a 200
r.history  # a list of the intermediate responses (not the final 200 response)

# Example .history response (sorted oldest to newest):
# [<Response [302]>, <Response [302]>, <Response [302]>]

# Disable redirection by passing the request `allow_redirects=False`


# You can use auth features as follows:
# HTTPBasic
from requests.auth import HTTPBasicAuth

r = requests.get('http://httpbin.org/basic-auth/user/password', 
                 auth=HTTPBasicAuth('user', 'password')
)


# HTTPDigest
from requests.auth import HTTPDigestAuth

r = requests.get('http://httpbin.org/digest-auth/auth/user/password',
                 auth=HTTPDigestAuth('user', 'password')
)
