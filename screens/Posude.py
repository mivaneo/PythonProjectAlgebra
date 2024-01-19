import tkinter as tk
from tkinter import ttk, LabelFrame, Frame, StringVar
from PIL import ImageTk, Image
from datasource.dto.BiljkeDto import BiljkeDto
from datasource.dto.PosudeDto import PosudeDto
from datasource.tk.TkBiljke import TkBiljke
from datasource.tk.TkPosude import TkPosude
from datasource.tk.TkHealthValues import TkHealthValues
from service.BiljkeService import BiljkeService
from service.PosudeService import PosudeService

class PosudeScreen(LabelFrame):

    def __init__(self, parent, healthValues: TkHealthValues, tkBiljke: TkBiljke, service: BiljkeService, posudeService: PosudeService, tkPosude: TkPosude):
        super().__init__(master=parent)
        self.grid(pady=5, padx=5)
        self.healthValues = healthValues
        self.tkBiljke = tkBiljke
        self.tkPosude = tkPosude
        self.service = service
        self.posudeService = posudeService
        self.createDetaljiPosude()


    def setComponent(self, component, row, column, sticky=None):
        if not sticky:
            component.grid(row=row, column=column, pady=5, padx=5)
        else:
            component.grid(row=row, column=column, pady=5, padx=5, sticky=sticky)


    def createDetaljiPosude(self):
        posude = ttk.LabelFrame(self, text="Posude")
        posude.grid(row=0, column=0, pady=5, padx=5)
        lblNazivPosude = ttk.Label(posude, text="Naziv posude:")
        lblNazivPosude.grid(row=0, column=1, pady=5, padx=5)
        lblIzaberiBiljkuUPosudu = ttk.Label(posude, text="Izaberi biljku:")
        lblIzaberiBiljkuUPosudu.grid(row=0, column=3, pady=5, padx=5)
        lblTemperaturaBiljke = ttk.Label(posude, text="Temperatura(Celzijus):")
        lblTemperaturaBiljke.grid(row=3, column=0, pady=5, padx=5)
        lblVlaznostBiljke = ttk.Label(posude, text="Vlaznost(%):")
        lblVlaznostBiljke.grid(row=4, column=0, pady=5, padx=5)
        lblPhBiljke = ttk.Label(posude, text="PH(kiselost):")
        lblPhBiljke.grid(row=5, column=0, pady=5, padx=5)
        lblSvjetlostBiljke = ttk.Label(posude, text="Svjetlost(suncanih sati):")
        lblSvjetlostBiljke.grid(row=6, column=0, pady=5, padx=5)
        lblSalinitetBiljke = ttk.Label(posude, text="Salinitet(decisimens/metar):")
        lblSalinitetBiljke.grid(row=7, column=0, pady=5, padx=5)

        btnOcisti = ttk.Button(posude, text="Ocisti", command=self.btnCancelClicked)
        btnOcisti.grid(row=8, column=3, pady=5, padx=5)
        btnAzuriraj = ttk.Button(posude, text="Spremi promjene", command=self.btnAzurirajClicked)
        btnAzuriraj.grid(row=8, column=2, pady=5, padx=5)
        btnObrisi = ttk.Button(posude, text="Izbrisi posudu", command=self.btnDeleteClicked)
        btnObrisi.grid(row=1, column=3, pady=5, padx=5)
        btnDodaj = ttk.Button(posude, text="Dodaj novu posudu", command=self.btnDodajClicked)
        btnDodaj.grid(row=1, column=2, pady=5, padx=5)

        self.posude = tk.Listbox(posude)
        self.posude.grid(row=0, column=0, pady=5, padx=5)
        self.posude.bind("<Double-1>", self.selectPosudefromList)

        self.fetchAndSetPosudeList()

        name = ttk.Entry(posude, textvariable=self.tkPosude.name)
        name.grid(row=0, column=2, padx=5, pady=5)
        
        posadenaBiljka = ttk.Combobox(posude, textvariable=self.tkPosude.biljka)
        posadenaBiljka.grid(row=0, column=4, padx=5, pady=5)
        posadenaBiljka.state = posadenaBiljka.state(["readonly"])
        values = self.service.dohvatiSveBiljkeName()
        posadenaBiljka['values'] = values

        temperature = ttk.Entry(posude, textvariable=self.tkPosude.temperature)
        temperature.grid(row=3, column=1, padx=5, pady=5)

        humidity = ttk.Entry(posude, textvariable=self.tkPosude.humidity)
        humidity.grid(row=4, column=1, padx=5, pady=5)

        ph = ttk.Entry(posude, textvariable=self.tkPosude.ph)
        ph.grid(row=5, column=1, padx=5, pady=5)

        light = ttk.Entry(posude, textvariable=self.tkPosude.light)
        light.grid(row=6, column=1, padx=5, pady=5)

        salinity = ttk.Entry(posude, textvariable=self.tkPosude.salinity)
        salinity.grid(row=7, column=1, padx=5, pady=5)

        lblStatus = ttk.Label(posude, text="Status")
        lblStatus.grid(row=2, column=2, pady=5, padx=5, columnspan=2)

        self.statusTemperature = tk.StringVar()
        self.lblstatusTemperature = ttk.Label(posude, textvariable=self.statusTemperature)
        self.lblstatusTemperature.grid(row=3, column=2, padx=5, pady=5, columnspan=2)

        self.statusHumidity = tk.StringVar()
        self.lblstatusHumidity = ttk.Label(posude, textvariable=self.statusHumidity)
        self.lblstatusHumidity.grid(row=4, column=2, padx=5, pady=5, columnspan=2)

        self.statusPh = tk.StringVar()
        self.lblstatusPh = ttk.Label(posude, textvariable=self.statusPh)
        self.lblstatusPh.grid(row=5, column=2, padx=5, pady=5, columnspan=2)

        self.statusLight = tk.StringVar()
        self.lblstatusLight = ttk.Label(posude, textvariable=self.statusLight)
        self.lblstatusLight.grid(row=6, column=2, padx=5, pady=5, columnspan=2)

        self.statusSalinity = tk.StringVar()
        self.lblstatusSalinity = ttk.Label(posude, textvariable=self.statusSalinity)
        self.lblstatusSalinity.grid(row=7, column=2, padx=5, pady=5, columnspan=2)

    def tempStatus(self):
        biljka = self.tkPosude.biljka.get()
        posudeDtoTemperature = self.posudeService.getBiljkaTemperatureFromPosuda(biljka)
        biljkeDtoTemperature = self.service.getBiljkaNameTemperature(biljka)
        print("biljka:", biljka)
        print("posudeDtoTemperature:", posudeDtoTemperature)
        print("biljkeDtoTemperature:", biljkeDtoTemperature)

        if posudeDtoTemperature is not None and biljkeDtoTemperature is not None:
            temp_diff = int(float(posudeDtoTemperature) - float(biljkeDtoTemperature))

            if temp_diff > 3:
                self.statusTemperature.set("Potrebno je SMANJITI temperaturu!")
            elif temp_diff < -3:
                self.statusTemperature.set("Potrebno je POVECATI temperaturu!")
            else:
                self.statusTemperature.set("Temperatura je OK!")
        else:
            if posudeDtoTemperature is None:
                self.statusTemperature.set("Nema podataka o temperaturi u posudi.")
            else:
                self.statusTemperature.set("Nema podataka o temperaturi biljke.")

    def humidityStatus(self):
        biljka = self.tkPosude.biljka.get()
        posudeDtoHumidity = self.posudeService.getBiljkaHumidityFromPosuda(biljka)
        biljkeDtoHumidity = self.service.getBiljkaNameHumidity(biljka)
        print("biljka:", biljka)
        print("posudeDtoHumidity:", posudeDtoHumidity)
        print("biljkeDtoHumidity:", biljkeDtoHumidity)

        if posudeDtoHumidity is not None and biljkeDtoHumidity is not None:
            humidity_diff = int(float(posudeDtoHumidity) - float(biljkeDtoHumidity))

            if humidity_diff > 5:
                self.statusHumidity.set("Potrebno je SMANJITI vlaznost!")
            elif humidity_diff < -5:
                self.statusHumidity.set("Potrebno je POVECATI vlaznost!")
            else:
                self.statusHumidity.set("Vlaznost je OK!")
        else:
            if posudeDtoHumidity is None:
                self.statusHumidity.set("Nema podataka o vlaznosti u posudi.")
            else:
                self.statusHumidity.set("Nema podataka o vlaznosti biljke.")

    def phStatus(self):
        biljka = self.tkPosude.biljka.get()
        posudeDtoPh = self.posudeService.getBiljkaPhFromPosuda(biljka)
        biljkeDtoPh = self.service.getBiljkaNamePh(biljka)
        print("biljka:", biljka)
        print("posudeDtoPh:", posudeDtoPh)
        print("biljkeDtoPh:", biljkeDtoPh)

        if posudeDtoPh is not None and biljkeDtoPh is not None:
            ph_diff = int(float(posudeDtoPh) - float(biljkeDtoPh))

            if ph_diff > 1:
                self.statusPh.set("Potrebno je SMANJITI ph!")
            elif ph_diff < -1:
                self.statusPh.set("Potrebno je POVECATI ph!")
            else:
                self.statusPh.set("Ph je OK!")
        else:
            if posudeDtoPh is None:
                self.statusPh.set("Nema podataka o ph u posudi.")
            else:
                self.statusPh.set("Nema podataka o ph biljke.")

    def lightStatus(self):
        biljka = self.tkPosude.biljka.get()
        posudeDtoLight = self.posudeService.getBiljkaLightFromPosuda(biljka)
        biljkeDtoLight = self.service.getBiljkaNameLight(biljka)
        print("biljka:", biljka)
        print("posudeDtoLight:", posudeDtoLight)
        print("biljkeDtoLight:", biljkeDtoLight)

        if posudeDtoLight is not None and biljkeDtoLight is not None:
            light_diff = int(float(posudeDtoLight) - float(biljkeDtoLight))

            if light_diff > 1:
                self.statusLight.set("Potrebno je SMANJITI svjetlost!")
            elif light_diff < -1:
                self.statusLight.set("Potrebno je POJACATI svjetlost!")
            else:
                self.statusLight.set("Svjetlost je OK!")
        else:
            if posudeDtoLight is None:
                self.statusLight.set("Nema podataka o svjetlosti u posudi.")
            else:
                self.statusLight.set("Nema podataka o svjetlosti biljke.")

    def salinityStatus(self):
        biljka = self.tkPosude.biljka.get()
        posudeDtoSalinity = self.posudeService.getBiljkaSalinityFromPosuda(biljka)
        biljkeDtoSalinity = self.service.getBiljkaNameSalinity(biljka)
        print("biljka:", biljka)
        print("posudeDtoSalinity:", posudeDtoSalinity)
        print("biljkeDtoSalinity:", biljkeDtoSalinity)

        if posudeDtoSalinity is not None and biljkeDtoSalinity is not None:
            salinity_diff = int(float(posudeDtoSalinity) - float(biljkeDtoSalinity))

            if salinity_diff > 1:
                self.statusSalinity.set("Potrebno je SMANJITI salinitet!")
            elif salinity_diff < -1:
                self.statusSalinity.set("Potrebno je POJACATI salinitet!")
            else:
                self.statusSalinity.set("Salinitet je OK!")
        else:
            if posudeDtoSalinity is None:
                self.statusSalinity.set("Nema podataka o salinitetu u posudi.")
            else:
                self.statusSalinity.set("Nema podataka o salinitetu biljke.")

    def selectBiljkefromList(self, event):
        selectedIndex = event.widget.curselection()
        biljkeDto: BiljkeDto = self.biljkeList[selectedIndex[0]]
        print(biljkeDto)
        self.tkBiljke.fillFromDto(biljkeDto)


    def fetchAndSetBiljkeList(self):
        self.biljkeList = self.service.dohvatiSveBiljke()
        simplifiedBiljkeList = []
        for biljke in self.biljkeList:
            b: BiljkeDto = biljke
            simplifiedBiljkeList.append(b.getInfo())
        self.tkBiljkeList = StringVar(value=simplifiedBiljkeList)
        self.biljke.config(listvariable=self.tkBiljkeList)

    def fetchAndSetPosudeList(self):
        self.posudeList = self.posudeService.dohvatiSvePosude()
        simplifiedPosudeList = []
        for posude in self.posudeList:
            p: PosudeDto = posude
            simplifiedPosudeList.append(p.getInfo())
        self.tkPosudeList = StringVar(value=simplifiedPosudeList)
        self.posude.config(listvariable=self.tkPosudeList)


    def selectPosudefromList(self, event):
        selectedIndex = event.widget.curselection()
        posudeDto: PosudeDto = self.posudeList[selectedIndex[0]]
        print(posudeDto)
        self.tkPosude.fillFromDto(posudeDto)
        self.tempStatus()
        self.humidityStatus()
        self.phStatus()
        self.lightStatus()
        self.salinityStatus()

    def btnAzurirajClicked(self):
        posudeDto = PosudeDto.createFromTkModel(self.tkPosude)
        self.posudeService.azurirajPosudu(posudeDto)
        self.fetchAndSetPosudeList()

    def btnDodajClicked(self):
        posudeDto = PosudeDto.createFromTkModel(self.tkPosude)
        self.posudeService.dodajPosudu(posudeDto)
        self.fetchAndSetPosudeList()

    def btnCancelClicked(self):
        self.clearTkPosude()
        self.statusTemperature.set("")
        self.statusHumidity.set("")
        self.statusPh.set("")
        self.statusLight.set("")
        self.statusSalinity.set("")
        self.fetchAndSetPosudeList()

    def btnDeleteClicked(self):
        self.posudeService.obrisiPosudu(self.tkPosude.id)
        self.clearTkPosude()
        self.fetchAndSetPosudeList()

    def clearTkPosude(self):
        self.tkPosude.clear()






