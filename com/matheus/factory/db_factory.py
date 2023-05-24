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
            DbFactory.__INSTANCE = self
        except ExErros as ex:
            raise ExErros(trackingCode="X.X.X", trackingMessage="Erro ao conectar com o banco de dados",
                          detalhes=str(ex))

    @staticmethod
    def valid_connection():
        return DbFactory.get_instance().__connection.is_connected()

    @staticmethod
    def get_instance():
        return DbFactory.__INSTANCE

    @staticmethod
    def getConnection():
        return DbFactory.get_instance().__connection

    @staticmethod
    def closeConnection():
        if DbFactory.get_instance().__connection is not None:
            return
        else:
            DbFactory.get_instance().close()
            return
