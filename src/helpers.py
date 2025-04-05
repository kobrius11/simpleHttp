
def dependancy_injector(obj_class: object):
    """
    Decorator to inject dependencies into a function.
    """
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            obj = obj_class()
            return func(self, obj, *args, **kwargs)
        return wrapper
    return decorator