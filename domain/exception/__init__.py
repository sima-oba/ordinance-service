class EntityNotFound(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class EntityAlreadyExists(Exception):
    def __init__(self, message: str):
        super().__init__(message)
