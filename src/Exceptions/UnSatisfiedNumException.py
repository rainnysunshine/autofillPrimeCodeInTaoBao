from Exceptions.LOLcapsuleException import LOLcapsuleException

class UnsatisfiedNumException(LOLcapsuleException):
    def __init__(self):
        super().__init__(f"账号数量和网址数量不对应")