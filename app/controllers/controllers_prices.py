from functools import wraps

def get_prices(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print('Calling decorated function')
        return f(*args, **kwds)
    return wrapper

@get_prices
def verifica_price():
    """Docstring"""
    print('Called example function')

