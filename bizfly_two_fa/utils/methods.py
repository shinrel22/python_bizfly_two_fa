import requests

from .decorators import request_connection_handler


@request_connection_handler
def do_request(method, url, **kwargs):
    method_handler = getattr(requests, method, None)
    if not method_handler:
        raise Exception('UnsupportedMethod')

    return method_handler(
        url=url,
        **kwargs
    )
