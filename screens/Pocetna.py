import tkinter as tk
from tkinter import ttk, LabelFrame, StringVar
from PIL import ImageTk, Image
from datasource.tk.TkHealthValues import TkHealthValues
from datasource.tk.TkPosude import TkPosude
from service.BiljkeService import BiljkeService
from service.PosudeService import PosudeService
from datasource.dto.PosudeDto import PosudeDto


class PocetnaScreen(LabelFrame):

    def __init__(self, parent, healthValues: TkHealthValues, tkPosude: TkPosude, service: BiljkeService, posudeService: PosudeService):
        super().__init__(master=parent)
        self.grid(pady=5, padx=5)
        self.healthValues = healthValues
        self.tkPosude = tkPosude
        self.service = service
        self.posudeService = posudeService
        self._loadImages()
        self.createDetaljiPosude()


    def setComponent(self, component, row, column, sticky=None):
        if not sticky:
            component.grid(row=row, column=column, pady=5, padx=5)
        else:
            component.grid(row=row, column=column, pady=5, padx=5, sticky=sticky)

    def createDetaljiPosude(self):
        pocetna = ttk.LabelFrame(self, text="Pregled")
        pocetna.grid(row=0, column=0, pady=5, padx=5)
        lblNazivPosude = ttk.Label(pocetna, text="Naziv posude:")
        lblNazivPosude.grid(row=1, column=0, pady=5, padx=5, sticky=tk.EW)
        lblIzaberiBiljkuUPosudu = ttk.Label(pocetna, text="Biljka:")
        lblIzaberiBiljkuUPosudu.grid(row=2, column=0, pady=5, padx=5, sticky=tk.EW)
        lblTemperaturaBiljke = ttk.Label(pocetna, text="Temperatura(Celzijus):")
        lblTemperaturaBiljke.grid(row=3, column=0, pady=5, padx=5, sticky=tk.EW)
        lblVlaznostBiljke = ttk.Label(pocetna, text="Vlaznost(%):")
        lblVlaznostBiljke.grid(row=4, column=0, pady=5, padx=5, sticky=tk.EW)
        lblPhBiljke = ttk.Label(pocetna, text="PH(kiselost):")
        lblPhBiljke.grid(row=5, column=0, pady=5, padx=5, sticky=tk.EW)
        lblSvjetlostBiljke = ttk.Label(pocetna, text="Svjetlost(suncanih sati):")
        lblSvjetlostBiljke.grid(row=6, column=0, pady=5, padx=5, sticky=tk.EW)
        lblSalinitetBiljke = ttk.Label(pocetna, text="Salinitet(decisimens/metar):")
        lblSalinitetBiljke.grid(row=7, column=0, pady=5, padx=5, sticky=tk.EW)

        self.posude = tk.Listbox(pocetna)
        self.posude.grid(row=0, column=1, pady=5, padx=5, sticky=tk.EW)
        self.posude.bind("<Double-1>", self.selectPosudefromList)

        self.fetchAndSetPosudeList()

        name = ttk.Label(pocetna, textvariable=self.tkPosude.name)
        name.grid(row=1, column=1, padx=5, pady=5, sticky=tk.EW)

        posadenaBiljka = ttk.Label(pocetna, textvariable=self.tkPosude.biljka)
        posadenaBiljka.grid(row=2, column=1, padx=5, pady=5, sticky=tk.EW)

        temperature = ttk.Label(pocetna, textvariable=self.tkPosude.temperature)
        temperature.grid(row=3, column=1, padx=5, pady=5, sticky=tk.EW)

        humidity = ttk.Label(pocetna, textvariable=self.tkPosude.humidity)
        humidity.grid(row=4, column=1, padx=5, pady=5, sticky=tk.EW)

        ph = ttk.Label(pocetna, textvariable=self.tkPosude.ph)
        ph.grid(row=5, column=1, padx=5, pady=5, sticky=tk.EW)

        light = ttk.Label(pocetna, textvariable=self.tkPosude.light)
        light.grid(row=6, column=1, padx=5, pady=5, sticky=tk.EW)

        salinity = ttk.Label(pocetna, textvariable=self.tkPosude.salinity)
        salinity.grid(row=7, column=1, padx=5, pady=5, sticky=tk.EW)

        lblStatus = ttk.Label(pocetna, text="Status")
        lblStatus.grid(row=2, column=2, pady=5, padx=5, columnspan=2, sticky=tk.EW)

        self.statusTemperature = tk.StringVar()
        self.lblstatusTemperature = ttk.Label(pocetna, textvariable=self.statusTemperature)
        self.lblstatusTemperature.grid(row=3, column=2, padx=5, pady=5, columnspan=2, sticky=tk.EW)

        self.statusHumidity = tk.StringVar()
        self.lblstatusHumidity = ttk.Label(pocetna, textvariable=self.statusHumidity)
        self.lblstatusHumidity.grid(row=4, column=2, padx=5, pady=5, columnspan=2, sticky=tk.EW)

        self.statusPh = tk.StringVar()
        self.lblstatusPh = ttk.Label(pocetna, textvariable=self.statusPh)
        self.lblstatusPh.grid(row=5, column=2, padx=5, pady=5, columnspan=2, sticky=tk.EW)

        self.statusLight = tk.StringVar()
        self.lblstatusLight = ttk.Label(pocetna, textvariable=self.statusLight)
        self.lblstatusLight.grid(row=6, column=2, padx=5, pady=5, columnspan=2, sticky=tk.EW)

        self.statusSalinity = tk.StringVar()
        self.lblstatusSalinity = ttk.Label(pocetna, textvariable=self.statusSalinity)
        self.lblstatusSalinity.grid(row=7, column=2, padx=5, pady=5, columnspan=2, sticky=tk.EW)

        lblTemperature = ttk.Label(pocetna, image=self.tkImgTemp)
        lblTemperature.grid(row=9, column=0, pady=5, padx=5)
        # lblTemperatureValue = ttk.Label(pocetna, textvariable=self.healthValues.temperature)
        # lblTemperatureValue.grid(row=9, column=0, pady=5, padx=5)

        lblHumidity = ttk.Label(pocetna, image=self.tkImgHumidity)
        lblHumidity.grid(row=10, column=0, pady=5, padx=5)
        # lblHumidityValue = ttk.Label(pocetna, textvariable=self.healthValues.humidity)
        # lblHumidityValue.grid(row=10, column=0, pady=5, padx=5)

        lblPh = ttk.Label(pocetna, image=self.tkImgPh)
        lblPh.grid(row=11, column=0, pady=5, padx=5)
        # lblPhValue = ttk.Label(pocetna, textvariable=self.healthValues.ph)
        # lblPhValue.grid(row=11, column=0, pady=5, padx=5)

        lblSalinity = ttk.Label(pocetna, image=self.tkImgSalinity)
        lblSalinity.grid(row=13, column=0, pady=5, padx=5)
        # lblSalinityValue = ttk.Label(pocetna, textvariable=self.healthValues.salinity)
        # lblSalinityValue.grid(row=13, column=0, pady=5, padx=5)

        lblLight = ttk.Label(pocetna, image=self.tkImgLight)
        lblLight.grid(row=12, column=0, padx=5, pady=5)
        # lblLightValue = ttk.Label(pocetna, textvariable=self.healthValues.light)
        # lblLightValue.grid(row=12, column=0, pady=5, padx=5)

        lblSimPh = ttk.Label(pocetna, text="Spremi nove vrijednosti")
        lblSimPh.grid(row=8, column=0, padx=5, pady=5, sticky=tk.EW)
        btnSync = ttk.Button(pocetna, text="Simulate", command=self.azurirajPosudu)
        btnSync.grid(row=8, column=1, pady=5, padx=5)

        self.scaleTemperature = ttk.Scale(pocetna, from_=0, to=50, variable=self.tkPosude.temperature, command=self.accept_whole_number_only_temp)
        self.scaleTemperature.grid(row=9, column=1, pady=5, padx=5, sticky=tk.EW)
        lblSimTemp = ttk.Label(pocetna, textvariable=self.tkPosude.temperature)
        lblSimTemp.grid(row=9, column=2, padx=5, pady=5, sticky=tk.EW)

        self.scaleHumidity = ttk.Scale(pocetna, from_=0, to=100, variable=self.tkPosude.humidity, command=self.accept_whole_number_only_humidity)
        self.scaleHumidity.grid(row=10, column=1, pady=5, padx=5, sticky=tk.EW)
        lblSimHumidity = ttk.Label(pocetna, textvariable=self.tkPosude.humidity)
        lblSimHumidity.grid(row=10, column=2, padx=5, pady=5, sticky=tk.EW)

        self.scalePh = ttk.Scale(pocetna, from_=0, to=10, variable=self.tkPosude.ph, command=self.accept_whole_number_only_ph)
        self.scalePh.grid(row=11, column=1, pady=5, padx=5, sticky=tk.EW)
        lblSimPh = ttk.Label(pocetna, textvariable=self.tkPosude.ph)
        lblSimPh.grid(row=11, column=2, padx=5, pady=5, sticky=tk.EW)

        self.scaleSalinity = ttk.Scale(pocetna, from_=0, to=10, variable=self.tkPosude.salinity, command=self.accept_whole_number_only_salinity)
        self.scaleSalinity.grid(row=13, column=1, pady=5, padx=5, sticky=tk.EW)
        lblSimSalinity = ttk.Label(pocetna, textvariable=self.tkPosude.salinity)
        lblSimSalinity.grid(row=13, column=2, padx=5, pady=5, sticky=tk.EW)

        self.scaleLight = ttk.Scale(pocetna, from_=0, to=24, variable=self.tkPosude.light, command=self.accept_whole_number_only_light)
        self.scaleLight.grid(row=12, column=1, padx=5, pady=5, sticky=tk.EW)
        lblSimLight = ttk.Label(pocetna, textvariable=self.tkPosude.light)
        lblSimLight.grid(row=12, column=2, padx=5, pady=5, sticky=tk.EW)

        btnOcisti = ttk.Button(pocetna, text="Ocisti", command=self.btnCancelClicked)
        btnOcisti.grid(row=0, column=3, pady=5, padx=5)

        btnOsvjezi = ttk.Button(pocetna, text="Osvjezi listu", command=self.btnOsvjezi)
        btnOsvjezi.grid(row=0, column=2, pady=5, padx=5)

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
        self.fetchAndSetPosudeList()

    def _loadImages(self):
        imgTemperature = Image.open("./images/thermometer.png")
        imgHumidity = Image.open("./images/humidity.png")
        imgPh = Image.open("./images/ph.png")
        imgSalinity = Image.open("./images/salinity.png")
        imgLight = Image.open("./images/light_on.png")

        self.tkImgTemp = ImageTk.PhotoImage(imgTemperature)
        self.tkImgHumidity = ImageTk.PhotoImage(imgHumidity)
        self.tkImgPh = ImageTk.PhotoImage(imgPh)
        self.tkImgSalinity = ImageTk.PhotoImage(imgSalinity)
        self.tkImgLight = ImageTk.PhotoImage(imgLight)

    def btnCancelClicked(self):
        self.clearTkPosude()
        self.statusTemperature.set("")
        self.statusHumidity.set("")
        self.statusPh.set("")
        self.statusLight.set("")
        self.statusSalinity.set("")
        self.fetchAndSetPosudeList()

    def clearTkPosude(self):
        self.tkPosude.clear()

    def btnOsvjezi(self):
        self.fetchAndSetPosudeList()

    def azurirajPosudu(self):
        posudeDto = PosudeDto.createFromTkModel(self.tkPosude)
        self.posudeService.azurirajPosudu(posudeDto)
        self.fetchAndSetPosudeList()

    def accept_whole_number_only_temp(self, e=None):
        value = self.scaleTemperature.get()
        rounded_value = int(value)
        if rounded_value != value:
            self.scaleTemperature.set(rounded_value)
        self.tkPosude.temperature.set(rounded_value)

    def accept_whole_number_only_humidity(self, e=None):
        value = self.scaleHumidity.get()
        rounded_value = int(value)
        if rounded_value != value:
            self.scaleHumidity.set(rounded_value)
        self.tkPosude.humidity.set(rounded_value)

    def accept_whole_number_only_ph(self, e=None):
        value = self.scalePh.get()
        rounded_value = int(value)
        if rounded_value != value:
            self.scalePh.set(rounded_value)
        self.tkPosude.ph.set(rounded_value)

    def accept_whole_number_only_salinity(self, e=None):
        value = self.scaleSalinity.get()
        rounded_value = int(value)
        if rounded_value != value:
            self.scaleSalinity.set(rounded_value)
        self.tkPosude.salinity.set(rounded_value)

    def accept_whole_number_only_light(self, e=None):
        value = self.scaleLight.get()
        rounded_value = int(value)
        if rounded_value != value:
            self.scaleLight.set(rounded_value)
        self.tkPosude.light.set(rounded_value)