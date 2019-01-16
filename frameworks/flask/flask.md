Flask
=====

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
