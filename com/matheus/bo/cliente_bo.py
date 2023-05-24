from com.matheus.dao.cliente_dao import ClienteDAO
from com.matheus.exceptions.ex_errors import ExErros

import csv

from com.matheus.utils.utils import Utils


class ClienteBo:

    def __init__(self):
        pass

    def get_planilha(self):
        """
        Efetua conversao dos dados do banco de dados para uma planilha
        :return:
        """
        try:
            cli_dao = ClienteDAO()
            # Buscar dados do cliente
            dados_cli, header = cli_dao.get_all_users()
            if dados_cli is None:
                return {"trackingCode": "X.X.X.21",
                        "trackingMessage": "Não existem dados do cliente cadastrados na base de dados"}
            criar_planilha(dados_cli, header)
        except Exception as ex:
            raise ExErros(trackingCode="01", trackingMessage="erro Interno", detalhes=str(ex))


def criar_planilha(dados, header):
    """
    Criar a planilha com os dados do cliente
    :param dados:  Dados do cliente
    :param header: campos do banco de dados / Servirá de header para a planilha
    :return:
    """
    nome_planilha = "dados.csv"
    with open(nome_planilha, 'w', newline="") as csvfile:
        dados_cli = csv.writer(csvfile)
        dados_cli.writerow(header)
        for cli in dados:
            dados_cli.writerow(cli)
