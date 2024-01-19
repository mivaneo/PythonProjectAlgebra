import tkinter as tk
from tkinter import ttk, LabelFrame, Frame, StringVar
from datasource.dto.UserDto import UserDto
from datasource.tk.TkUser import TkUser
from service.UserService import UserService

class ProfilScreen(LabelFrame):

    def __init__(self, parent, service: UserService, tkUser: TkUser):
        super().__init__(master=parent)
        self.grid(pady=5, padx=5)
        self.service = service
        self.tkUser = tkUser
        self.createDetaljiUser()

    def setComponent(self, component, row, column, sticky=None):
        if not sticky:
            component.grid(row=row, column=column, pady=5, padx=5)
        else:
            component.grid(row=row, column=column, pady=5, padx=5, sticky=sticky)


    def createDetaljiUser(self):
        profil = ttk.LabelFrame(self, text="Profil")
        profil.grid(row=0, column=0, pady=5, padx=5)
        lblUsername = ttk.Label(profil, text="Username:")
        lblUsername.grid(row=0, column=1, pady=5, padx=5, sticky=tk.E)
        lblPassword = ttk.Label(profil, text="Password:")
        lblPassword.grid(row=1, column=1, pady=5, padx=5, sticky=tk.E)


        btnOcisti = ttk.Button(profil, text="Ocisti", command=self.btnCancelClicked)
        btnOcisti.grid(row=2, column=2, pady=5, padx=5)
        btnAzuriraj = ttk.Button(profil, text="Azuriraj usera", command=self.btnAzurirajClicked)
        btnAzuriraj.grid(row=3, column=1, pady=5, padx=5)
        btnObrisi = ttk.Button(profil, text="Obrisi usera", command=self.btnDeleteClicked)
        btnObrisi.grid(row=3, column=0, pady=5, padx=5)
        btnDodaj = ttk.Button(profil, text="Dodaj usera", command=self.btnDodajClicked)
        btnDodaj.grid(row=3, column=2, pady=5, padx=5)

        self.user = tk.Listbox(profil)
        self.user.grid(row=0, column=0, pady=5, padx=5, rowspan=3)
        self.user.bind("<Double-1>", self.selectUserfromList)

        self.fetchAndSetUserList()


        username = ttk.Entry(profil, textvariable=self.tkUser.username)
        username.grid(row=0, column=2, padx=5, pady=5, sticky=tk.EW, columnspan=2)

        password = ttk.Entry(profil, textvariable=self.tkUser.password)
        password.grid(row=1, column=2, padx=5, pady=5, sticky=tk.EW, columnspan=2)



    def selectUserfromList(self, event):
        selectedIndex = event.widget.curselection()
        userDto: UserDto = self.userList[selectedIndex[0]]
        print(userDto)
        self.tkUser.fillFromDto(userDto)



    def fetchAndSetUserList(self):
        self.userList = self.service.dohvatiSveUsere()
        simplifiedUserList = []
        for user in self.userList:
            u: UserDto = user
            simplifiedUserList.append(u.getInfo())
        self.tkUserList = StringVar(value=simplifiedUserList)
        self.user.config(listvariable=self.tkUserList)

    def btnAzurirajClicked(self):
        userDto = UserDto.createFromTkModel(self.tkUser)
        self.service.azurirajUsera(userDto)
        self.fetchAndSetUserList()

    def btnDodajClicked(self):
        userDto = UserDto.createFromTkModel(self.tkUser)
        self.service.dodajUsera(userDto)
        self.fetchAndSetUserList()


    def btnDeleteClicked(self):
        self.service.obrisiUsera(self.tkUser.id)
        self.clearTkUser()
        self.fetchAndSetUserList()

    def clearTkUser(self):
        self.tkUser.clear()

    def btnCancelClicked(self):
        self.clearTkUser()