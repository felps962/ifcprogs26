from datetime import date
class cliente:
    def __init__(self,nome:str,data_nascimento:date,cpf:str):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class prato:
    def __init__(self,nome:str,valor_prato:float,quantidade:int):
        self.nome = nome
        self.valor_prato = valor_prato
        self.quantidade = quantidade
        
class pedido(cliente,prato):
    def __init__(self, nome, data_nascimento, cpf,data_pedido:date,percentual_descconto:float,valor_final:float,pratos:list[prato]):
        super().__init__(nome, data_nascimento, cpf)
        self.data_pedido = data_pedido
        self.percentual_desconto = percentual_descconto
        self.valor_final = valor_final
        self.pratos = pratos