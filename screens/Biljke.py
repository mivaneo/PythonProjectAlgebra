import tkinter as tk
from tkinter import ttk, LabelFrame, Frame, StringVar
from PIL import ImageTk, Image
from datasource.dto.BiljkeDto import BiljkeDto
from datasource.tk.TkBiljke import TkBiljke
from datasource.tk.TkHealthValues import TkHealthValues
from service.BiljkeService import BiljkeService

class BiljkeScreen(LabelFrame):

    def __init__(self, parent, healthValues: TkHealthValues, tkBiljke: TkBiljke, service: BiljkeService):
        super().__init__(master=parent)
        self.grid(pady=5, padx=5)
        self.healthValues = healthValues
        self.tkBiljke = tkBiljke
        self.tkBiljke.loadImage(r"images/rajcica_grappolo.png")
        self.tkBiljke.loadImage(r"images/rajcica_roma.png")
        self.tkBiljke.loadImage(r"images/bosiljak.png")
        self.tkBiljke.loadImage(r"images/jalapeno.png")
        self.tkBiljke.loadImage(r"images/krastavac.png")
        self.tkBiljke.loadImage(r"images/menta.png")
        self.tkBiljke.loadImage(r"images/mrkva.png")
        self.tkBiljke.loadImage(r"images/ruzmarin.png")
        self.tkBiljke.loadImage(r"images/crvena_jagoda.png")
        self.tkBiljke.loadImage(r"images/bijela_jagoda.png")
        self.tkBiljke.loadImage(r"images/no_image.png")
        self.service = service
        self.createDetaljiBiljke()
        self.tkImageBiljke: ImageTk = None
        self._loadImages()



    def setComponent(self, component, row, column, sticky=None):
        if not sticky:
            component.grid(row=row, column=column, pady=5, padx=5)
        else:
            component.grid(row=row, column=column, pady=5, padx=5, sticky=sticky)


    def createDetaljiBiljke(self):
        biljke = ttk.LabelFrame(self, text="Biljke")
        biljke.grid(row=0, column=0, pady=5, padx=5)
        lblNazivBiljke = ttk.Label(biljke, text="Naziv biljke:")
        lblNazivBiljke.grid(row=0, column=1, pady=5, padx=5)
        lblTemperaturaBiljke = ttk.Label(biljke, text="Temperatura(Celzijus):")
        lblTemperaturaBiljke.grid(row=1, column=1, pady=5, padx=5)
        lblVlaznostBiljke = ttk.Label(biljke, text="Vlaznost(%):")
        lblVlaznostBiljke.grid(row=2, column=1, pady=5, padx=5)
        lblPhBiljke = ttk.Label(biljke, text="PH(kiselost):")
        lblPhBiljke.grid(row=3, column=1, pady=5, padx=5)
        lblSvjetlostBiljke = ttk.Label(biljke, text="Svjetlost(suncanih sati):")
        lblSvjetlostBiljke.grid(row=4, column=1, pady=5, padx=5)
        lblSalinitetBiljke = ttk.Label(biljke, text="Salinitet(decisimens/metar):")
        lblSalinitetBiljke.grid(row=5, column=1, pady=5, padx=5)

        btnOcisti = ttk.Button(biljke, text="Ocisti", command=self.btnCancelClicked)
        btnOcisti.grid(row=7, column=0, pady=5, padx=5)
        btnAzuriraj = ttk.Button(biljke, text="Azuriraj biljku", command=self.btnAzurirajClicked)
        btnAzuriraj.grid(row=7, column=3, pady=5, padx=5)
        btnObrisi = ttk.Button(biljke, text="Obrisi biljku", command=self.btnDeleteClicked)
        btnObrisi.grid(row=7, column=4, pady=5, padx=5)
        btnDodaj = ttk.Button(biljke, text="Dodaj biljku", command=self.btnDodajClicked)
        btnDodaj.grid(row=7, column=2, pady=5, padx=5)

        self.biljke = tk.Listbox(biljke)
        self.biljke.grid(row=0, column=0, pady=5, padx=5, rowspan=5)
        self.biljke.bind("<Double-1>", self.selectBiljkefromList)

        self.fetchAndSetBiljkeList()


        name = ttk.Entry(biljke, textvariable=self.tkBiljke.name)
        name.grid(row=0, column=2, padx=5, pady=5, sticky=tk.EW, columnspan=2)

        temperature = ttk.Entry(biljke, textvariable=self.tkBiljke.temperature)
        temperature.grid(row=1, column=2, padx=5, pady=5, sticky=tk.EW, columnspan=2)

        humidity = ttk.Entry(biljke, textvariable=self.tkBiljke.humidity)
        humidity.grid(row=2, column=2, padx=5, pady=5, sticky=tk.EW, columnspan=2)

        ph = ttk.Entry(biljke, textvariable=self.tkBiljke.ph)
        ph.grid(row=3, column=2, padx=4, pady=5, sticky=tk.EW, columnspan=2)

        light = ttk.Entry(biljke, textvariable=self.tkBiljke.light)
        light.grid(row=4, column=2, padx=4, pady=5, sticky=tk.EW, columnspan=2)

        salinity = ttk.Entry(biljke, textvariable=self.tkBiljke.salinity)
        salinity.grid(row=5, column=2, padx=4, pady=5, sticky=tk.EW, columnspan=2)

        foto = ttk.Label(biljke, image=self.tkBiljke.tkImageBiljke)
        foto.grid(row=0, column=4, padx=5, pady=5, rowspan=6)



    def selectBiljkefromList(self, event):
        selectedIndex = event.widget.curselection()
        biljkeDto: BiljkeDto = self.biljkeList[selectedIndex[0]]
        print(biljkeDto)
        self.tkBiljke.fillFromDto(biljkeDto)
        if biljkeDto.id == 1:
            image = Image.open("./images/rajcica_grappolo.png")
            self.tkBiljke.tkImageBiljke = ImageTk.PhotoImage(image)
        elif biljkeDto.id == 2:
            jalapeno = self.tkBiljke.loadImage(r"images/jalapeno.png")
            self.tkBiljke.tkImageBiljke = jalapeno
        elif biljkeDto.id == 3:
            menta = self.tkBiljke.loadImage(r"images/menta.png")
            self.tkBiljke.tkImageBiljke = menta
        elif biljkeDto.id == 4:
            bosiljak = self.tkBiljke.loadImage(r"images/bosiljak.png")
            self.tkBiljke.tkImageBiljke = bosiljak
        elif biljkeDto.id == 5:
            crvena_jagoda = self.tkBiljke.loadImage(r"images/crvena_jagoda.png")
            self.tkBiljke.tkImageBiljke = crvena_jagoda
        elif biljkeDto.id == 6:
            ruzmarin = self.tkBiljke.loadImage(r"images/ruzmarin.png")
            self.tkBiljke.tkImageBiljke = ruzmarin
        elif biljkeDto.id == 7:
            bijela_jagoda = self.tkBiljke.loadImage(r"images/bijela_jagoda.png")
            self.tkBiljke.tkImageBiljke = bijela_jagoda
        elif biljkeDto.id == 8:
            krastavac = self.tkBiljke.loadImage(r"images/krastavac.png")
            self.tkBiljke.tkImageBiljke = krastavac
        elif biljkeDto.id == 9:
            rajcica_roma = self.tkBiljke.loadImage(r"images/rajcica_roma.png")
            self.tkBiljke.tkImageBiljke = rajcica_roma
        elif biljkeDto.id == 10:
            mrkva = self.tkBiljke.loadImage(r"images/mrkva.png")
            self.tkBiljke.tkImageBiljke = mrkva
        else:
            ostalo = self.tkBiljke.loadImage(r"images/no_image.png")
            self.tkBiljke.tkImageBiljke = ostalo



    def fetchAndSetBiljkeList(self):
        self.biljkeList = self.service.dohvatiSveBiljke()
        simplifiedBiljkeList = []
        for biljke in self.biljkeList:
            b: BiljkeDto = biljke
            simplifiedBiljkeList.append(b.getInfo())
        self.tkBiljkeList = StringVar(value=simplifiedBiljkeList)
        self.biljke.config(listvariable=self.tkBiljkeList)

    def btnAzurirajClicked(self):
        biljkeDto = BiljkeDto.createFromTkModel(self.tkBiljke)
        self.service.azurirajBiljku(biljkeDto)
        self.fetchAndSetBiljkeList()

    def btnDodajClicked(self):
        biljkeDto = BiljkeDto.createFromTkModel(self.tkBiljke)
        self.service.dodajBiljku(biljkeDto)
        self.fetchAndSetBiljkeList()

    def btnCancelClicked(self):
        self.clearTkBiljke()
        ostalo = self.tkBiljke.loadImage(r"images/no_image.png")
        self.tkBiljke.tkImageBiljke = ostalo

    def btnDeleteClicked(self):
        self.service.obrisiBiljku(self.tkBiljke.id)
        self.clearTkBiljke()
        self.fetchAndSetBiljkeList()

    def clearTkBiljke(self):
        self.tkBiljke.clear()

    def loadImage(self, url):
        self.image = Image.open(url)
        self.tkImageBiljke = ImageTk.PhotoImage(self.image)

    def _loadImages(self):
        imgRajcicaGrappolo = Image.open("./images/rajcica_grappolo.png")
        imgJalapeno = Image.open("./images/jalapeno.png")
        imgMenta = Image.open("./images/menta.png")
        imgBosiljak = Image.open("./images/bosiljak.png")
        imgCrvenaJagoda = Image.open("./images/crvena_jagoda.png")
        imgRuzmarin = Image.open("./images/ruzmarin.png")
        imgBijelaJagoda = Image.open("./images/bijela_jagoda.png")
        imgKrastavac = Image.open("./images/krastavac.png")
        imgRajcicaRoma = Image.open("./images/rajcica_roma.png")
        imgMrkva = Image.open("./images/mrkva.png")
        imgNoImage = Image.open("./images/no_image.png")



