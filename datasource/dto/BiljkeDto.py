class BiljkeDto:

    def __init__(self):
        self.id = None
        self.name = None
        self.temperature = None
        self.humidity = None
        self.ph = None
        self.light = None
        self.salinity = None

    def __repr__(self):
        return f"{self.id}, {self.name}, {self.temperature},{self.humidity}, {self.ph}, {self.light}, {self.salinity}"

    def getInfo(self):
        return f"{self.id} {self.name}"

    @staticmethod
    def createFromResult(result: tuple):
        biljkeDto = BiljkeDto()
        biljkeDto.id = result[0]
        biljkeDto.name = result[1]
        biljkeDto.temperature = result[2]
        biljkeDto.humidity = result[3]
        biljkeDto.ph = result[4]
        biljkeDto.light = result[5]
        biljkeDto.salinity = result[6]
        return biljkeDto

    @staticmethod
    def createFromResultName(result: tuple):
        biljkeDto = BiljkeDto()
        biljkeDto.name = result[0]
        return biljkeDto


    @staticmethod
    def createFromTkModel(tkModel):
        biljkeDto = BiljkeDto()
        biljkeDto.id = tkModel.id
        biljkeDto.name = tkModel.name.get()
        biljkeDto.temperature = tkModel.temperature.get()
        biljkeDto.humidity = tkModel.humidity.get()
        biljkeDto.ph = tkModel.ph.get()
        biljkeDto.light = tkModel.light.get()
        biljkeDto.salinity = tkModel.salinity.get()
        return biljkeDto
