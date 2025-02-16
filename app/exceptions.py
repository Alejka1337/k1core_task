from fastapi import HTTPException, status


class BlockNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail="Block not found")


class CurrencyOrProviderNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail="Currency or Provider not found")


class UserNotFoundException(HTTPException):
    def __init__(self):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")


class NotValidCredentialsException(HTTPException):
    def __init__(self):
        super().__init__(status_code=401, detail="Could not validate credentials")


class UserDoesExistsExException(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail="User with this name already exists")
