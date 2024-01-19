from utils.DBUtils import DBUtils
from datasource.dto.PosudeDto import PosudeDto


class PosudeService:

    TABLE_NAME = "posude"

    def __init__(self, sqlConnection):
        self.connection = sqlConnection
        self.kreirajTablicu()
        self._upisiPosude()


    def kreirajTablicu(self):
        query = f"""
            CREATE TABLE IF NOT EXISTS
            {self.TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(40) NOT NULL UNIQUE,
                biljka VARCHAR(30) NULL,
                temperature VARCHAR(10) NULL,
                humidity VARCHAR(10) NULL,
                ph VARCHAR(10) NULL,
                light VARCHAR(10) NULL,
                salinity VARCHAR(10) NULL
            );
        """
        DBUtils.izvrsiIZapisi(self.connection, query)


    def _upisiPosude(self):
        self.upisiPosudu("Plava posuda", "Menta", "15", "45", "4", "7","1")


    def dohvatiSvePosude(self):
        query = f"SELECT * FROM {self.TABLE_NAME};"
        rezultat = DBUtils.dohvatiPodatke(self.connection, query)
        posudeList = []
        if rezultat is not None:
            for posude in rezultat:
                posudeDto: PosudeDto = PosudeDto.createFromResult(posude)
                print(posudeDto)
                posudeList.append(posudeDto)
            return posudeList
        else:
            return None


    def upisiPosudu(self, name, biljka, temperature, humidity, ph, light, salinity):
        query = f"""
            INSERT INTO {self.TABLE_NAME} (name, biljka, temperature, humidity, ph, light, salinity)
            VALUES ('{name}', '{biljka}', '{temperature}', '{humidity}', '{ph}', '{light}', '{salinity}');
        """
        DBUtils.izvrsiIZapisi(self.connection, query)


    def dodajPosudu(self, dto: PosudeDto):
        query = f"""
            INSERT INTO {self.TABLE_NAME} (name, biljka, temperature, humidity, ph, light, salinity)
            VALUES ('{dto.name}','{dto.biljka}', '{dto.temperature}', '{dto.humidity}', '{dto.ph}', '{dto.light}', '{dto.salinity}');
        """
        DBUtils.izvrsiIZapisi(self.connection, query)

    def azurirajPosudu(self, dto: PosudeDto):
        query = f"""
            UPDATE {self.TABLE_NAME} 
            SET name='{dto.name}',biljka='{dto.biljka}',temperature='{dto.temperature}',humidity='{dto.humidity}',ph='{dto.ph}',light='{dto.light}',salinity='{dto.salinity}'
            WHERE id={dto.id};
        """
        DBUtils.izvrsiIZapisi(self.connection, query)


    def obrisiPosudu(self, id):
        query = f"DELETE FROM {self.TABLE_NAME} where id={id};"
        DBUtils.izvrsiIZapisi(self.connection, query)


    def getBiljkaTemperatureFromPosuda(self, biljka):
        query = f"SELECT temperature FROM {self.TABLE_NAME} WHERE biljka = ?"
        result = DBUtils.izvrsiIDohvati(self.connection, query, (biljka,))

        if result is not None and len(result) > 0 and result[0] is not None:
            temperature_tuple = result[0]
            temperature = temperature_tuple[0]

            if temperature is not None:
                try:
                    return int(temperature)
                except ValueError:
                    pass

        return None

    def getBiljkaHumidityFromPosuda(self, biljka):
        query = f"SELECT humidity FROM {self.TABLE_NAME} WHERE biljka = ?"
        result = DBUtils.izvrsiIDohvati(self.connection, query, (biljka,))

        if result is not None and len(result) > 0 and result[0] is not None:
            humidity_tuple = result[0]
            humidity = humidity_tuple[0]

            if humidity is not None:
                try:
                    return int(humidity)
                except ValueError:
                    pass

        return None

    def getBiljkaPhFromPosuda(self, biljka):
        query = f"SELECT ph FROM {self.TABLE_NAME} WHERE biljka = ?"
        result = DBUtils.izvrsiIDohvati(self.connection, query, (biljka,))

        if result is not None and len(result) > 0 and result[0] is not None:
            ph_tuple = result[0]
            ph = ph_tuple[0]

            if ph is not None:
                try:
                    return int(ph)
                except ValueError:
                    pass

        return None

    def getBiljkaLightFromPosuda(self, biljka):
        query = f"SELECT light FROM {self.TABLE_NAME} WHERE biljka = ?"
        result = DBUtils.izvrsiIDohvati(self.connection, query, (biljka,))

        if result is not None and len(result) > 0 and result[0] is not None:
            light_tuple = result[0]
            light = light_tuple[0]

            if light is not None:
                try:
                    return int(light)
                except ValueError:
                    pass

        return None

    def getBiljkaSalinityFromPosuda(self, biljka):
        query = f"SELECT salinity FROM {self.TABLE_NAME} WHERE biljka = ?"
        result = DBUtils.izvrsiIDohvati(self.connection, query, (biljka,))

        if result is not None and len(result) > 0 and result[0] is not None:
            salinity_tuple = result[0]
            salinity = salinity_tuple[0]

            if salinity is not None:
                try:
                    return int(salinity)
                except ValueError:
                    pass

        return None