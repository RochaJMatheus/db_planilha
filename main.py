# This is a sample Python script.
from com.matheus.bo.cliente_bo import ClienteBo
from com.matheus.exceptions.ex_errors import ExErros
from com.matheus.factory.db_factory import DbFactory

if __name__ == '__main__':
    try:
        DbFactory()
        # verificar conexão com o banco de dados
        isConnected = DbFactory.get_instance().valid_connection
        if isConnected:
            bo = ClienteBo()
            bo.get_planilha()
        else:
            print("erro conexão não foi aberta")

    except ExErros as ex:
        print(ex.exibir_erro())
    finally:
        DbFactory.get_instance().closeConnection()
        print("Conexão fechada")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
