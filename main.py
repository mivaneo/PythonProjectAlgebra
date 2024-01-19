import tkinter as tk
from tkinter import ttk, Tk
import sqlite3
from service.UserService import UserService
from screens.Login import PrviProzor
from service.BiljkeService import BiljkeService
from service.PosudeService import PosudeService


class App(Tk):

    def __init__(self, service: BiljkeService, userService: UserService, posudeService: PosudeService):
        super().__init__()
        self.title("PyFloraPosude")
        self.geometry("770x770")
        self.userService = userService
        self.service = service
        self.posudeService = posudeService
        self.kreirajPrviProzor()

    def kreirajPrviProzor(self):
        PrviProzor(self, self.service, self.userService, self.posudeService)

def initDB():
    DB = "biljke.db"
    conn = sqlite3.connect(DB)
    return conn

def initDBUser():
    DB = "user.db"
    conn = sqlite3.connect(DB)
    return conn

def initDBPosude():
    DB = "posude.db"
    conn = sqlite3.connect(DB)
    return conn

if __name__ == '__main__':
    sqlConnection = initDB()
    service = BiljkeService(sqlConnection)
    sqlConnectionUser = initDBUser()
    userService = UserService(sqlConnectionUser)
    sqlConnectionPosude = initDBPosude()
    posudeService = PosudeService(sqlConnectionPosude)
    app = App(service, userService, posudeService)
    app.mainloop()

