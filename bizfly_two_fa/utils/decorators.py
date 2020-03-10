import requests
import time
from functools import wraps

from bizfly_two_fa.constants import DEFAULT_REQUEST_TIMEOUT, DEFAULT_MAX_REQUEST_RETRY


def request_connection_handler(func):
    @wraps(func)
    def handle(*args, **kwargs):

        if 'timeout' not in kwargs:
            kwargs['timeout'] = DEFAULT_REQUEST_TIMEOUT

        counter = 0
        error = None
        while counter < DEFAULT_MAX_REQUEST_RETRY:
            try:
                response = func(*args, **kwargs)
                return response
            except (requests.ConnectTimeout, requests.ConnectionError) as e:
                error = e
                counter += 1

            time.sleep(counter ** 2)
        raise error

    return handle
