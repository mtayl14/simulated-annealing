class Result:
    def __init__(self, okay, value):
        self.okay = okay
        self.value = value

    def Ok(value):
        return Result(True, value)
    
    def Err(error):
        return Result(False, error)
    
    def is_ok(self):
        return self.okay
    
    def get_err(self):
        if not self.okay:
            return self.value
        else:
            raise Exception("Tried to get error from valid result!")
    
    def unwrap_or_else(self, other):
        if self.okay:
            return self.value
        else:
            return other

    def unwrap(self):
        if self.okay:
            return self.value
        else:
            raise Exception("Tried to get value of invalid result!")