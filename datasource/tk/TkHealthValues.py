from tkinter import StringVar, BooleanVar

class TkHealthValues:

    def __init__(self):
        self.temperature = StringVar()
        self.humidity = StringVar()
        self.ph = StringVar()
        self.salinity = StringVar()
        self.light = StringVar()
        self.simulated = BooleanVar()
        self.simulated.set(False)