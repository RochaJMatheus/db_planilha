import datetime
import json
import sys
import traceback

from com.matheus.factory.db_factory import DbFactory
from com.matheus.model.cliente import Cliente


class ClienteDAO:
    def __init__(self):
        pass

    def get_all_users(self):
        """
        Busca todos os usuáros na base de dados
        :return:
        """
        # Connection
        conn = DbFactory.get_instance().getConnection()
        cursor = conn.cursor(dictionary=True)
        try:
            cursor.execute("Select * from cliente")
            result = cursor.fetchall()
            print(result)
            if not result:
                return None
            # Iterar dados cliente
            arr_cli = []
            for cli in result:
                cli['data_nascimento'] = datetime.datetime.strftime(cli['data_nascimento'], '%d/%m/%Y') if cli[
                    'data_nascimento'] else ''
                tupla = ()
                for j, k in cli.items():
                    tupla = tupla + (k,)
                arr_cli.append(tupla)
            headers = [i[0] for i in cursor.description]
            return arr_cli, headers
        except Exception as ex:
            traceback.print_exception(type(ex), ex, ex.__traceback__, file=sys.stderr)
            raise Exception(ex)
