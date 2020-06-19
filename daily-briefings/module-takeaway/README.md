## Exposing module attributes/functions

- __all__ inside the module
- define inside `__init__py` attrs/funcs, import module gives it accessibility
- This was a think back while reading the python requests documentation


## Wraps in requests.

### Call stacks
- requests.get - this is obtained via the module.__init__, shortcut for requests.api.get
  - get accepts params
  - head accepts params
  - options accepts params
  - et cetera
  - all goes to function `requests.api.request()`
    - Inside which a :class:`Request <Request>` is constructed and sent, within a session.
      - With below form: `request(method, url, **kwargs)`
        - inside which there's this `session.request()`
          - `session.request` performs below actions
            - constructs a `models.Request` instance
            - prepare the specific instance
            - send the instance using `session.send`
            - returns the response

