from com.matheus.factory.db_factory import DbFactory


class ClienteDAO:
    def __init__(self):
        pass

    def get_all_users(self):
        """
        Busca todos os usuáros na base de dados
        :return:
        """
        # Connection
        conn = DbFactory().get_instance().getConnection()
        cursor = conn.cursor(dictionary=True)
