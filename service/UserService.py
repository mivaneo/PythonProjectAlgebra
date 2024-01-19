from utils.DBUtils import DBUtils
from datasource.dto.UserDto import UserDto


class UserService:

    TABLE_NAME = "user"

    def __init__(self, sqlConnection):
        self.connection = sqlConnection
        self.kreirajTablicu()
        self._upisiUsera()



    def kreirajTablicu(self):
        query = f"""
            CREATE TABLE IF NOT EXISTS
            {self.TABLE_NAME} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR(30) UNIQUE NOT NULL,
                password VARCHAR(30) NOT NULL
            );
        """
        DBUtils.izvrsiIZapisi(self.connection, query)


    def upisiUsera(self, username, password):
        query = f"""
            INSERT INTO {self.TABLE_NAME} (username, password)
            VALUES ('{username}', '{password}');
        """
        DBUtils.izvrsiIZapisi(self.connection, query)

    def _upisiUsera(self):
        self.upisiUsera("admin", "admin123")

    def dohvatiSveUsere(self):
        query = f"SELECT * FROM {self.TABLE_NAME};"
        rezultat = DBUtils.dohvatiPodatke(self.connection, query)
        userList = []
        if rezultat is not None:
            for user in rezultat:
                userDto: UserDto = UserDto.createFromResult(user)
                print(userDto)
                userList.append(userDto)
            return userList
        else:
            return None

    def azurirajUsera(self, dto: UserDto):
        query = f"""
            UPDATE {self.TABLE_NAME} 
            SET username='{dto.username}',password='{dto.password}'
            WHERE id={dto.id};
        """
        DBUtils.izvrsiIZapisi(self.connection, query)

    def obrisiUsera(self, id):
        query = f"DELETE FROM {self.TABLE_NAME} where id={id};"
        DBUtils.izvrsiIZapisi(self.connection, query)

    def dodajUsera(self, dto: UserDto):
        query = f"""
            INSERT INTO {self.TABLE_NAME} (username, password)
            VALUES ('{dto.username}', '{dto.password}');
        """
        DBUtils.izvrsiIZapisi(self.connection, query)

    def getUserByUsername(self, username):
        query = f"SELECT * FROM {self.TABLE_NAME} where username='{username}';"
        result = DBUtils.dohvatiPodatke(self.connection, query, one=True)
        if result is not None:
            userDto: UserDto = UserDto.createFromResult(result)
            print(userDto)
            return userDto
        else:
            return None