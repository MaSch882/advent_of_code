class IllegalArgumentError(ValueError):

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)


class IllegalStateError(ValueError):

    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
