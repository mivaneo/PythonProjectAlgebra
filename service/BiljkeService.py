from utils.DBUtils import DBUtils
from datasource.dto.BiljkeDto import BiljkeDto


class BiljkeService:

    TABLE_NAME = "biljke"

    def __init__(self, sqlConnection):
        self.connection = sqlConnection
        self.kreirajTablicu()
        self._upisiBiljke()


    def kreirajTablicu(self):
        query = f"""
            CREATE TABLE IF NOT EXISTS
            {self.TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(30) NOT NULL UNIQUE,
                temperature VARCHAR(10) NOT NULL,
                humidity VARCHAR(10) NOT NULL,
                ph VARCHAR(10) NOT NULL,
                light VARCHAR(10) NOT NULL,
                salinity VARCHAR(10) NOT NULL
            );
        """
        DBUtils.izvrsiIZapisi(self.connection, query)


    def _upisiBiljke(self):
        self.upisiBiljku("Rajcica Grappolo", "15", "55", "5", "8", "1")
        self.upisiBiljku("Jalapeno paprika", "18", "50", "5", "10", "2")
        self.upisiBiljku("Menta", "15", "45", "4", "7", "1")
        self.upisiBiljku("Bosiljak", "16", "50", "5", "8", "1")
        self.upisiBiljku("Crvena jagoda", "20", "60", "4", "10", "2")
        self.upisiBiljku("Ruzmarin", "13", "52", "4", "7", "1")
        self.upisiBiljku("Bijela jagoda", "22", "57", "4", "9", "1")
        self.upisiBiljku("Krastavac", "15", "50", "5", "7", "2")
        self.upisiBiljku("Rajcica Roma", "16", "58", "5", "8", "1")
        self.upisiBiljku("Mrkva", "14", "50", "4", "7", "1")

    def dohvatiSveBiljke(self):
        query = f"SELECT * FROM {self.TABLE_NAME};"
        rezultat = DBUtils.dohvatiPodatke(self.connection, query)
        biljkeList = []
        if rezultat is not None:
            for biljke in rezultat:
                biljkeDto: BiljkeDto = BiljkeDto.createFromResult(biljke)
                print(biljkeDto)
                biljkeList.append(biljkeDto)
            return biljkeList
        else:
            return None


    def dohvatiSveBiljkeName(self):
        query = f"SELECT name FROM {self.TABLE_NAME};"
        rezultat = DBUtils.dohvatiPodatke(self.connection, query)
        biljkeList = []
        if rezultat is not None:
            for biljke in rezultat:
                biljkeDto: BiljkeDto = BiljkeDto.createFromResultName(biljke)
               # print(biljkeDto)
                biljkeList.append(biljkeDto.name)
            return biljkeList
        else:
            return None


    def getBiljkaNameTemperature(self, biljka):
        query = f"SELECT temperature FROM {self.TABLE_NAME} WHERE name = ?"
        result = DBUtils.izvrsiIDohvati(self.connection, query, (biljka,))

        if result is not None and len(result) > 0 and result[0] is not None:
            temperature_tuple = result[0]
            temperature = temperature_tuple[0]
            return int(temperature)
        else:
            return None

    def getBiljkaNameHumidity(self, biljka):
        query = f"SELECT humidity FROM {self.TABLE_NAME} WHERE name = ?"
        result = DBUtils.izvrsiIDohvati(self.connection, query, (biljka,))

        if result is not None and len(result) > 0 and result[0] is not None:
            humidity_tuple = result[0]
            humidity = humidity_tuple[0]
            return int(humidity)
        else:
            return None

    def getBiljkaNamePh(self, biljka):
        query = f"SELECT ph FROM {self.TABLE_NAME} WHERE name = ?"
        result = DBUtils.izvrsiIDohvati(self.connection, query, (biljka,))

        if result is not None and len(result) > 0 and result[0] is not None:
            ph_tuple = result[0]
            ph = ph_tuple[0]
            return int(ph)
        else:
            return None

    def getBiljkaNameLight(self, biljka):
        query = f"SELECT light FROM {self.TABLE_NAME} WHERE name = ?"
        result = DBUtils.izvrsiIDohvati(self.connection, query, (biljka,))

        if result is not None and len(result) > 0 and result[0] is not None:
            light_tuple = result[0]
            light = light_tuple[0]
            return int(light)
        else:
            return None

    def getBiljkaNameSalinity(self, biljka):
        query = f"SELECT salinity FROM {self.TABLE_NAME} WHERE name = ?"
        result = DBUtils.izvrsiIDohvati(self.connection, query, (biljka,))

        if result is not None and len(result) > 0 and result[0] is not None:
            salinity_tuple = result[0]
            salinity = salinity_tuple[0]
            return int(salinity)
        else:
            return None



    def upisiBiljku(self, name, temperature, humidity, ph, light, salinity):
        query = f"""
            INSERT INTO {self.TABLE_NAME} (name, temperature, humidity, ph, light, salinity)
            VALUES ('{name}', '{temperature}', '{humidity}', '{ph}', '{light}', '{salinity}');
        """
        DBUtils.izvrsiIZapisi(self.connection, query)

    def dodajBiljku(self, dto: BiljkeDto):
        query = f"""
            INSERT INTO {self.TABLE_NAME} (name, temperature, humidity, ph, light, salinity)
            VALUES ('{dto.name}', '{dto.temperature}', '{dto.humidity}', '{dto.ph}', '{dto.light}', '{dto.salinity}');
        """
        DBUtils.izvrsiIZapisi(self.connection, query)


    def azurirajBiljku(self, dto: BiljkeDto):
        query = f"""
            UPDATE {self.TABLE_NAME} 
            SET name='{dto.name}',temperature='{dto.temperature}',humidity='{dto.humidity}',ph='{dto.ph}',light='{dto.light}',salinity='{dto.salinity}'
            WHERE id={dto.id};
        """
        DBUtils.izvrsiIZapisi(self.connection, query)


    def obrisiBiljku(self, id):
        query = f"DELETE FROM {self.TABLE_NAME} where id={id};"
        DBUtils.izvrsiIZapisi(self.connection, query)


