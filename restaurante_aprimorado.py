from datetime import date
class Cliente:
    def __init__(self,nome:str,data_nascimento:date,cpf:str):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Prato:
    def __init__(self,nome:str,ingredientes:list[str],modo_preparo:str,preco:float ):
        self.nome = nome
        self.ingredientes = ingredientes
        self.modo_preparo = modo_preparo
        self.preco = preco

class ItemPedido:
    def __init__(self,prato:Prato, valor_prato:float,quantidade:int):
        self.prato = prato
        self.valor_prato = valor_prato
        self.quantidade = quantidade

class Pedido:
    def __init__(self, cliente: Cliente):
        self.cliente = cliente
        self.itens = []

    def adicionar_item(self, item: ItemPedido):
        self.itens.append(item)

    def valor_total(self):
        return sum(item.prato.preco * item.quantidade for item in self.itens)
