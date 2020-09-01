



class Pagamento:
    def __init__(self,nome,cnpj,dono,telefone):
        self.estabelecimento = {nome:self.nome,cnpj:self.cnpj,dono:self.dono,telefone:self.telefone}
        return self.estabelecimento

    def payment_(self):
        #return self.estabelecimento
        pass


pag = Pagamento(nome='Paulo Ribeiro',cnpj='10',dono='Pedro',telefone='100200101')
