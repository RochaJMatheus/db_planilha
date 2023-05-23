class ExErros(Exception):

    def __init__(self, trackingCode, trackingMessage, detalhes):
        """

        :param trackingCode: Código de rastreio especifico para um microsserviço
        :param trackingMessage: Mensagem para rastreio de erros
        :param detalhes: Detalhes sobre o erro
        """
        self.__trackingCode = trackingCode
        self.__trackingMessage = trackingMessage = trackingMessage
        self.__detalhes = detalhes

    def exibir_erro(self):
        return "Tracking: {tracking} \n" \
               "Message: {message} \n" \
               "Detalhes: {detalhes}".format(tracking=self.__trackingCode, message=self.__trackingMessage,
                                             detalhes=self.__detalhes)

    @property
    def trackingCode(self):
        return self.__trackingCode

    @trackingCode.setter
    def trackingCode(self, value):
        self.__trackingCode = value

    @property
    def trackingMessage(self):
        return self.__trackingMessage

    @trackingMessage.setter
    def trackingMessage(self, value):
        self.__trackingMessage = value

    @property
    def detalhes(self):
        return self.__detalhes

    @detalhes.setter
    def detalhes(self, value):
        self.__detalhes = value
