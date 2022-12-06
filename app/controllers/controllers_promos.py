from functools import wraps

def get_promos(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print('Calling decorated function')
        return f(*args, **kwds)
    return wrapper

@get_promos
def verifica_promos():
    """Docstring"""
    print('Called example function')

