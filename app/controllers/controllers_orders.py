from functools import wraps

def get_order(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print('Calling decorated function')
        return f(*args, **kwds)
    return wrapper

@get_order
def verifica_order():
    """Docstring"""
    print('Called example function')

