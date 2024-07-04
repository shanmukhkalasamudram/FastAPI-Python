class ErrorDecorator(Exception):
    def __init__(self, name: str, status: int):
        self.name = name
        self.status = status
        