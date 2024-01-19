from tkinter import StringVar, BooleanVar
from PIL import Image, ImageTk
from datasource.dto.PosudeDto import PosudeDto


class TkPosude():

    def __init__(self):
        self.id = None
        self.name = StringVar()
        self.biljka = StringVar()
        self.temperature = StringVar()
        self.humidity = StringVar()
        self.ph = StringVar()
        self.light = StringVar()
        self.salinity = StringVar()


    def fillFromDto(self, posudeDto: PosudeDto):
        self.id = posudeDto.id
        self.name.set(posudeDto.name)
        self.biljka.set(posudeDto.biljka)
        self.temperature.set(posudeDto.temperature)
        self.humidity.set(posudeDto.humidity)
        self.ph.set(posudeDto.ph)
        self.light.set(posudeDto.light)
        self.salinity.set(posudeDto.salinity)


    def clear(self):
        self.id = None
        self.name.set("")
        self.biljka.set("")
        self.temperature.set("")
        self.humidity.set("")
        self.ph.set("")
        self.light.set("")
        self.salinity.set("")


    def loadImage(self, url):
        self.image = Image.open(url)
        self.tkImagePosude = ImageTk.PhotoImage(self.image)



