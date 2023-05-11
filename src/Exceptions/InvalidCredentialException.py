from Exceptions.LOLcapsuleException import LOLcapsuleException

class InvalidCredentialsException(LOLcapsuleException):
    def __init__(self):
        super().__init__(f"Invalid account credentials.")