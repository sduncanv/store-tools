class CustomError(Exception):

    def __init__(self, message: str, status_code: int = 400):
        self.message: str = message
        self.status_code = status_code
        super().__init__(self.message)

    def __str__(self) -> str:
        return self.message
