from threading import Thread
from mqtt.MqttClient import MqttClient
from time import sleep as delay
import tkinter as tk
from datetime import datetime as dt
from datasource.dto.PosudeDto import PosudeDto
from datasource.tk.TkPosude import TkPosude


class MqttMessageReaderService(Thread):

    def __init__(self, mqtt: MqttClient, messageReceiver: tk.Text, tkModel: TkPosude):
        super().__init__()
        self.mqtt = mqtt
        self.tkRpi = tkModel
        self.messageBox = messageReceiver

    def run(self):
        while True:
            try:
                message = self.mqtt.getFromQueue()
                if message != None:
                    print(message)
                    self.writeMessageToBox(message)
                    topic, msg = message.split(";")
                    if topic == "iot/MIposuda":
                        print(msg)
                        posudeDto = PosudeDto()
                        posudeDto.serialize(msg, ignoreProperties=True)
                        print(posudeDto.dumpModel())
                        self.tkRpi.temperature.set(round(posudeDto.temperature, 2))
                        self.tkRpi.humidity.set(round(posudeDto.humidity, 2))
                        self.tkRpi.ph.set(round(posudeDto.ph, 2))
                        self.tkRpi.light.set(round(posudeDto.light, 2))
                        self.tkRpi.salinity.set(round(posudeDto.salinity, 2))

                else:
                    print("Nothing to read!")
            except:
                print("Nothing to read!")
            delay(1)

    def writeMessageToBox(self, text):
        topic, msg = text.split(";")
        self.messageBox.config(state=tk.NORMAL)
        output = f"[{dt.now()}]-[{topic}]: {msg}"
        self.messageBox.insert(tk.END, output + "\n")
        self.messageBox.config(state=tk.DISABLED)
        self.messageBox.see(tk.END)