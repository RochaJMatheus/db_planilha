class Utils:

    def __init__(self):
        pass

    def convertClassToJson(self, objt: object):
        """
        Converte um objeto python com atributos para um objeto dict\n
        Obs: Classe que será convertida deve seguir o padrão de atributos privados
        :param obj: Objeto ex Class , list[Class]
        :return: Dict
        """
        if type(objt) is list:
            _jsonArr = []
            for obj in objt:
                _jsonObj = obj.__dict__
                for key in list(_jsonObj):
                    _jsonObj[key.replace(obj.__class__.__name__, '').replace("_", '')] = _jsonObj.pop(key)
                _jsonArr.append(_jsonObj)
            return _jsonArr
        else:
            _jsonObj = objt.__dict__
            for key in list(_jsonObj):
                _jsonObj[key.replace(objt.__class__.__name__, '').replace("_", "")] = _jsonObj.pop(key)
            return _jsonObj
