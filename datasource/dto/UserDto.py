class UserDto:

    def __init__(self):
        self.id = None
        self.username = None
        self.password = None

    def __repr__(self):
        return f"{self.id}, {self.username}, {self.password}"

    def getInfo(self):
        return f"{self.username}"

    @staticmethod
    def createFromResult(result: tuple):
        userDto = UserDto()
        userDto.id = result[0]
        userDto.username = result[1]
        userDto.password = result[2]
        return userDto

    @staticmethod
    def createFromTkModel(tkModel):
        userDto = UserDto()
        userDto.id = tkModel.id
        userDto.username = tkModel.username.get()
        userDto.password = tkModel.password.get()
        return userDto
