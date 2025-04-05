class Route():
    def __init__(self, func, template_path: str = None, method: str = "GET", path: str = None):
        self.func = func
        self.template_path = template_path
        self.method = method
        self.path = path
