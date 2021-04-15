class Request:
    def __init__(self, method, path, headers, *data):
        self.method = method
        self.path = path
        self.headers = headers
        self.data = data
