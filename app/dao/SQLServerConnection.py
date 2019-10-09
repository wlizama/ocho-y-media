import pyodbc
import configparser
from ..utils.Constants import INI_SOURCE

class SQLServerConnection:
    def __init__(self):
        self.__config = configparser.ConfigParser()
        self.__config.read(INI_SOURCE)
        self.__con = self.__connect()

    def __connect(self):
        return pyodbc.connect(f"""\
            DRIVER={self.__config.get("BD_CONNECTION.SQL_Server", "driver_name")};\
            SERVER={self.__config.get("BD_CONNECTION.SQL_Server", "bdip")};\
            UID={self.__config.get("BD_CONNECTION.SQL_Server", "user")};\
            PWD={self.__config.get("BD_CONNECTION.SQL_Server", "password")};\
            DATABASE={self.__config.get("BD_CONNECTION.SQL_Server", "database")};\
            """)


    def __get_cursor(self):
        return self.__con.cursor()


    def execute_insert(self, table, cols, vals):
        str_cols = ",".join(cols)
        str_vals_ident = "?"
        str_vals = str_vals_ident * len(cols)
        str_vals = ",".join(str_vals)

        cursor = self.__get_cursor()

        cursor.execute(f"""\
        INSERT INTO {table} ({str_cols}) values ({str_vals});
        """, vals)
        cursor.execute("select @@IDENTITY;")

        returnId = cursor.fetchval()

        self.__con.commit()
        self.__con.close()

        return returnId


    def execute_list(self, table, cols="", cond=""):
        str_cols = "*" if len(cols.strip()) == 0 else cols
        str_cond = "" if len(cond.strip()) == 0 else f" WHERE {cond}"

        cursor = self.__get_cursor()
        cursor.execute(f"SELECT {str_cols} from {table}{str_cond};")
        return cursor.fetchall()