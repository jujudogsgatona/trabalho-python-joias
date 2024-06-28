class Joias:
    def __init__(self, cor, material, tipo, quilates, preco, pedra_preciosa):
        self.__cor = cor,
        self.__material = material,
        self.__tipo = tipo,
        self.__quilates = quilates,
        self.__preco = preco,
        self.__pedra_preciosa = pedra_preciosa 

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        self.__preco = valor

    @property
    def pedra_preciosa (self):
        return self.__pedra_preciosa 

    @pedra_preciosa.setter
    def pedra_preciosa (self, valor):
        self.__pedra_preciosa = valor