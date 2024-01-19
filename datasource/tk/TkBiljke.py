from tkinter import StringVar, BooleanVar
from PIL import Image, ImageTk
from datasource.dto.BiljkeDto import BiljkeDto

class TkBiljke:

    def __init__(self):
        self.id = None
        self.name = StringVar()
        self.temperature = StringVar()
        self.humidity = StringVar()
        self.ph = StringVar()
        self.light = StringVar()
        self.salinity = StringVar()
        self.image = None
        self.tkImageBiljke: ImageTk = None

    def fillFromDto(self, biljkeDto: BiljkeDto):
        self.id = biljkeDto.id
        self.name.set(biljkeDto.name)
        self.temperature.set(biljkeDto.temperature)
        self.humidity.set(biljkeDto.humidity)
        self.ph.set(biljkeDto.ph)
        self.light.set(biljkeDto.light)
        self.salinity.set(biljkeDto.salinity)

    def clear(self):
        self.id = None
        self.name.set("")
        self.temperature.set("")
        self.humidity.set("")
        self.ph.set("")
        self.light.set("")
        self.salinity.set("")


    def loadImage(self, url):
        self.image = Image.open(url)
        self.tkImageBiljke = ImageTk.PhotoImage(self.image)

