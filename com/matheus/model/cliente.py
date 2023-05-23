class Cliente:

    def __init__(self, **kwargs):
        self.__id = kwargs.get('id')
        self.__nome = kwargs.get('nome')
        self.__sobrenome = kwargs.get('sobrenome')
        self.__data_nascimento = kwargs.get('data_nascimento')
        self.__cpf = kwargs.get('cpf')
        self.__email = kwargs.get('email')
        self.__rg = kwargs.get('rg')

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def sobrenome(self):
        return self.__sobrenome

    @sobrenome.setter
    def sobrenome(self, value):
        self.__sobrenome = value

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, value):
        self.__data_nascimento = value

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, value):
        self.__cpf = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def rg(self):
        return self.__rg

    @rg.setter
    def rg(self, value):
        self.__rg = value
