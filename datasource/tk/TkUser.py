from tkinter import StringVar, BooleanVar
from datasource.dto.UserDto import UserDto

class TkUser:

    def __init__(self):
        self.id = None
        self.username = StringVar()
        self.password = StringVar()

    def fillFromDto(self, userDto: UserDto):
        self.id = userDto.id
        self.username.set(userDto.username)
        self.password.set(userDto.password)

    def clear(self):
        self.id = None
        self.username.set("")
        self.password.set("")
