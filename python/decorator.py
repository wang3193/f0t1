import functools
def log(text):
    def do (func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
           print(text)
           return func(*args, **kw)
        return wrapper
    return do

import datetime

@log("test log")
def now():
    print(datetime.datetime.now())

now()

