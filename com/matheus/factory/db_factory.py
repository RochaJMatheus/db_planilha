import mysql
import mysql.connector
from com.matheus.exceptions.ex_errors import ExErros


class DbFactory:
    __INSTANCE = None

    def __init__(self):
        # Inicializar  a conexão com o banco de dados
        try:
            self.__connection = mysql.connector.connect(user='root',
                                                        password='gRKCi10S5swq3^40iWKL7w*55YMJU0oPT!d^gYKTxj1%&qnH5U',
                                                        host='127.0.0.1',
                                                        database='db_dados')
            self.__INSTANCE = self
        except ExErros as ex:
            raise ExErros(trackingCode="X.X.X", trackingMessage="Erro ao conectar com o banco de dados",
                          detalhes=str(ex))

    def get_instance(self):
        return self.__INSTANCE

    @staticmethod
    def getConnection(self):
        return self.__connection

    @staticmethod
    def closeConnection(self):
        if self.__connection is not None:
            return
        else:
            self.__connection.close()
            return
