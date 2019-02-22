import json
import functools

def to_json(func):
    @functools.wraps(func)
    def wrapped(*args,**kwargs):
        obj = func(*args,**kwargs)
        result = json.dumps(obj)
        return result
    return wrapped
@to_json
def get_data():
    return None
get_data()  # вернёт '{"data": 42}'
