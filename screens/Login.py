import tkinter as tk
from tkinter import Frame
from tkinter import ttk
from datasource.tk.TkHealthValues import TkHealthValues
from datasource.tk.TkBiljke import TkBiljke
from datasource.tk.TkUser import TkUser
from datasource.tk.TkPosude import TkPosude
from datasource.dto.BiljkeDto import BiljkeDto
from datasource.dto.UserDto import UserDto
from service.BiljkeService import BiljkeService
from service.UserService import UserService
from service.PosudeService import PosudeService
from screens.Pocetna import PocetnaScreen
from screens.Biljke import BiljkeScreen
from screens.Profil import ProfilScreen
from screens.Posude import PosudeScreen
from time import sleep as delay
from PIL import Image, ImageTk

class PrviProzor(Frame):

    def __init__(self, mainWindow, service: BiljkeService, userService: UserService, posudeService: PosudeService):
        super().__init__(master=mainWindow)
        self.grid()
        self['relief'] = tk.RAISED
        self['borderwidth'] = 5
        self.toggleProzor2 = False
        self.toggleVisibility = False
        self.healthValues = TkHealthValues()
        self.tkBiljke = TkBiljke()
        self.userDto = UserDto()
        self.tkUser = TkUser()
        self.tkPosude = TkPosude()
        self.service = service
        self.userService = userService
        self.posudeService = posudeService
        self.kreirajPrvuGrupuWidgeta()


    def kreirajPrvuGrupuWidgeta(self):
        imgShow = Image.open("./images/show.png")
        imgHide = Image.open("./images/hide.png")

        self.prozor1 = tk.LabelFrame(self, text="Prijava")
        self.prozor1.grid(row=0, column=0, pady=5, padx=5)

        self.lblUsername = ttk.Label(self.prozor1, text="Username:")
        self.lblUsername.grid(row=0, column=0, padx=5, pady=5)

        self.username = tk.StringVar()
        self.eUsername = ttk.Entry(self.prozor1, textvariable=self.username)
        self.eUsername.grid(row=0, column=1, padx=5, pady=5)

        self.lblPassword = ttk.Label(self.prozor1, text="Password:")
        self.lblPassword.grid(row=1, column=0, pady=5, padx=5)

        self.password = tk.StringVar()
        self.ePassword = ttk.Entry(self.prozor1, textvariable=self.password, show="*")
        self.ePassword.grid(row=1, column=1, padx=5, pady=5)


        self.tkImgShow = ImageTk.PhotoImage(imgShow)
        self.tkImgHide = ImageTk.PhotoImage(imgHide)
        self.btnUkljuciVidljivost = ttk.Button(self.prozor1, image=self.tkImgHide, command=self.promjeniVidljivost)
        self.btnUkljuciVidljivost.grid(row=1, column=2)

        btnLogin = ttk.Button(self.prozor1, text="Prijava", command=self.login)
        btnLogin.grid(row=2, column=1, pady=5, padx=5)

        self.upozorenje = tk.StringVar()
        self.lblUpozorenje = ttk.Label(self.prozor1, textvariable=self.upozorenje)
        self.lblUpozorenje.grid(row=3, column=0, padx=5, pady=5, columnspan=2)

    def promjeniVidljivost(self):
        if not self.toggleVisibility:
            self.ePassword.config(show="")
            self.btnUkljuciVidljivost.config(image=self.tkImgShow)
            self.toggleVisibility = True
        else:
            self.ePassword.config(show="*")
            self.btnUkljuciVidljivost.config(image=self.tkImgHide)
            self.toggleVisibility = False

    def login(self):
        userDto: UserDto = self.userService.getUserByUsername(self.username.get())
        if userDto is not None:
            if self.username.get() == userDto.username and self.password.get() == userDto.password:
                self.kreirajDruguGrupuWidgeta()
                self.prozor1.grid_remove()
            else:
                self.upozorenje.set("Username ili password ne odgovaraju!")


    def kreirajDruguGrupuWidgeta(self):
        self.floraPanel = ttk.LabelFrame(self, text="PyFloraPosude")
        self.floraPanel.grid(row=0, column=1, padx=5, pady=5)

        self.tabs = ttk.Notebook(self.floraPanel)
        self.tabs.grid(row=0, column=0, pady=5, padx=5)

        self.tabPocetna = ttk.Frame(self.tabs)
        self.tabBiljke = ttk.Frame(self.tabs)
        self.tabPosude = ttk.Frame(self.tabs)
        self.tabProfil = ttk.Frame(self.tabs)

        self.tabs.add(self.tabPocetna, text="Pregled")
        self.tabs.add(self.tabBiljke, text="Biljke")
        self.tabs.add(self.tabPosude, text="Posude")
        self.tabs.add(self.tabProfil, text="Profil")

        self.pocetnaScreen = PocetnaScreen(self.tabPocetna, self.healthValues, self.tkPosude, self.service, self.posudeService)
        self.biljkeScreen = BiljkeScreen(self.tabBiljke, self.healthValues, self.tkBiljke, self.service)
        self.profilScreen = ProfilScreen(self.tabProfil, self.userService, self.tkUser)
        self.PosudeScreen = PosudeScreen(self.tabPosude, self.healthValues, self.tkBiljke, self.service, self.posudeService, self.tkPosude)




