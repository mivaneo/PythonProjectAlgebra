import sqlite3


class DBUtils:

    @staticmethod
    def izvrsiIZapisi(sqlConnection, upit):
        try:
            cursor = sqlConnection.cursor()
            cursor.execute(upit)
            sqlConnection.commit()
            cursor.close()
            return True
        except sqlite3.Error as sqlError:
            print(sqlError)
        except Exception as e:
            print(e)

        return False

    @staticmethod
    def dohvatiPodatke(sqlConnection, upit, one=False):
        try:
            cursor: sqlite3.Cursor = sqlConnection.cursor()
            cursor.execute(upit)
            rezultat = None
            if one:
                rezultat = cursor.fetchone()
            else:
                rezultat = cursor.fetchall()
            cursor.close()
            return rezultat
        except sqlite3.Error as sqlError:
            print(sqlError)
        except Exception as e:
            print(e)

    @staticmethod
    def izvrsiIDohvati(sqlConnection, upit, parameters=None, one=False):
        try:
            cursor = sqlConnection.cursor()
            if parameters:
                cursor.execute(upit, parameters)
            else:
                cursor.execute(upit)

            result = None
            if one:
                result = cursor.fetchone()
            else:
                result = cursor.fetchall()

            cursor.close()
            sqlConnection.commit()
            return result
        except sqlite3.Error as sqlError:
            print(sqlError)
        except Exception as e:
            print(e)

        return None


