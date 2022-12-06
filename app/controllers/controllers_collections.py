from functools import wraps


def get_collections(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print('Calling decorated function')
        return f(*args, **kwds)
    return wrapper



@get_collections
def verifica_collections():
    """Docstring"""
    print('Called example function')

