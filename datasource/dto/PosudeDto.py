import json
from utils.JSONSerializator import JSONSerializator

class PosudeDto(JSONSerializator):

    def __init__(self):
        self.id = None
        self.name = None
        self.biljka = None
        self.temperature = None
        self.humidity = None
        self.ph = None
        self.light = None
        self.salinity = None


    def __repr__(self):
        return f"{self.id}, {self.name}, {self.biljka}, {self.temperature},{self.humidity}, {self.ph}, {self.light}, {self.salinity}"

    def getInfo(self):
        return f"{self.name}"

    @staticmethod
    def createFromResult(result: tuple):
        posudeDto = PosudeDto()
        posudeDto.id = result[0]
        posudeDto.name = result[1]
        posudeDto.biljka = result[2]
        posudeDto.temperature = result[3]
        posudeDto.humidity = result[4]
        posudeDto.ph = result[5]
        posudeDto.light = result[6]
        posudeDto.salinity = result[7]
        return posudeDto

    @staticmethod
    def createFromResultName(result: tuple):
        posudeDto = PosudeDto()
        posudeDto.biljka = result[0]
        return posudeDto

    @staticmethod
    def createFromTkModel(tkModel):
        posudeDto = PosudeDto()
        posudeDto.id = tkModel.id
        posudeDto.name = tkModel.name.get()
        posudeDto.biljka = tkModel.biljka.get()
        posudeDto.temperature = tkModel.temperature.get()
        posudeDto.humidity = tkModel.humidity.get()
        posudeDto.ph = tkModel.ph.get()
        posudeDto.light = tkModel.light.get()
        posudeDto.salinity = tkModel.salinity.get()
        return posudeDto

    def getJson(self):
        model = {
            'temperature': self.temperature,
            'humidity': self.humidity,
            'pressure': self.ph,
            'light': self.light,
            'salinity': self.salinity
        }
        return json.dumps(model)
