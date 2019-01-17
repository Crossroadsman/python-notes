Flask
=====

Request Objects
---------------
### The Request Object ###
-Type: `flask.wrappers.Request` (presents as `werkzeug.local.LocalProxy`).
-Docs: <http://flask.pocoo.org/docs/1.0/api/#flask.Request>

### Accessing a Request object ###
Flask keeps a reference to the request context. This is available to anything 
on the same thread. Access it thus:
```python
from flask import request

...

print(request)
```

### Interesting Attributes on a Request Object ###

- `args` (?): The query string as key value pairs;
- `base_url` (`str`): The URL. E.g., `'https://www.myhost.com/api/v1/todos'`;
- `content_encoding` (? | `None`): Specified content encoding, if any. Otherwise None;
- `content_type` (? | `None`): Specified content type, if any. Otherwise None;
- `data` (`bytes`): The request data, if any, otherwise empty bytestring;
- `endpoint` (`str`): The API endpoint name (added to request object by Flask Api?);
- `files` (`wekzeug ImmutableMultiDict`): ???;
- `form` (`wekzeug ImmutableMultiDict`): ???;
- `full_path` (`str`): The portion of the URL after the hostname. E.g., `'/api/v1/todos?'` (note the trailing `?`);
- `get_data()` (`() -> bytes`): Method to generate the data attribute;
- `get_json()` (`() -> ??? | None`): Method to generate the json attribute;
- `json` (? | `None`): The request data as JSON, if any, otherwise None;
- `headers` (`werkzeug.datastructures.EnvironHeaders` object (dict-like, with repr that looks like multiline string): The request 
  headers;
- `host` (`str`): The hostname portion of the URL (including port (if not port 80?)). E.g., `'www.myhost.com'`;
- `host_url` (`str`): The hostname as URL. E.g., `'https://www.myhost.com/'`;
- `method` (`str`): The request method. E.g., `'DELETE'`;
- `path` (`str`): Like `full_path` but without any query string component. E.g., `'/api/v1/todos'`;
- `query_string` (`bytes`): The query string, if any, as a bytestring;
- `remote_addr` (`str`): The IP of the remote computer;
- `url` (`str`): The full URL. Like `base_url` if no query string. E.g., `'https://www.myhost.com/api/v1/todos'`;
- `url_root` (`str`): Like `host_url` unless ?. E.g., `'https://www.myhost.com/'`.


Response Objects
----------------
Interesting attributes on `Response` (type: `flask.wrappers.Response`) include:
- `content_encoding` : The content encoding if provided, otherwise None; TYPE 
  IF NOT NONE?
- `data` : The response body as a `bytes`;
- `get_data()` : Seems to return the same value as in `data`. Are there options 
  we can pass?
- `status_code` : The HTTP status code (e.g., 200) as an `int`
- `json`: ??? if provided, otherwise None
- `get_json()` : HOW/WHAT? Probably returns the same value as in `json`. 
  Unknown if there are options we can pass.
- `headers` : The HTTP headers (as a `werkzeug.datastructures.Headers` object)
  (presents as a multiline string). Has dict-like methods available to it:
  `items()`, `keys()`, `values()`, `to_list`
- `location` : ??? if provided, otherwise None
