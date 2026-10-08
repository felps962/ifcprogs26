class veiculo:
    def __init__(self, placa:str , ano:int):
        self.placa = placa
        self.ano = ano


class moto(veiculo):
    def __init__(self, placa, ano):
        super().__init__(placa, ano)

class caminhao(veiculo):
    def __init__(self, placa, ano, peso_kg: int):
        super().__init__(placa, ano)
        self.peso_kg - peso_kg
    