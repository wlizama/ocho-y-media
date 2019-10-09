import pyodbc
import configparser
from ..utils.Constants import INI_SOURCE

class SQLServerConnection:
    def __init__(self):
        self.__config = configparser.ConfigParser()
        self.__config.read(INI_SOURCE)


    def connect(self):
        return pyodbc.connect(f"""\
            DRIVER={self.__config.get("BD_CONNECTION.SQL_Server", "driver_name")};\
            SERVER={self.__config.get("BD_CONNECTION.SQL_Server", "bdip")};\
            UID={self.__config.get("BD_CONNECTION.SQL_Server", "user")};\
            PWD={self.__config.get("BD_CONNECTION.SQL_Server", "password")};\
            DATABASE={self.__config.get("BD_CONNECTION.SQL_Server", "database")};\
            """)


    def get_cursor(self):
        return self.connect().cursor()