# TODO: Add custom exceptions for each input type i.e. make sure age isn't a negative number
# TODO: Also figure out how to map an exception to the input type. Do that in the class definition?


class MyException(ValueError):
    def __init__(self, msg):
        super().__init__(msg)


class HeaderException(MyException):
    def __init__(self, msg):
        super().__init__(msg)


class InputException(MyException):
    def __init__(self, msg):
        super().__init__(msg)
