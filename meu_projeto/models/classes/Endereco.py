import os
from models.enum.Unidade_federativa import Unidade_federativa
class Endereco:
    def __init__(self, logradouro:str , numero:str , cep:str , complemento:str , cidade:str, uf:Unidade_federativa) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.cep = cep
        self.complemento = complemento
        self.cidade = cidade
        self.uf= uf
    def __str__(self) -> str:
        return (f"\n Logradouro:{self.logradouro}"
                f"\n numero:{self.numero}"
                f"\n cep:{self.cep}"
                f"\n complemento:{self.complemento}"
                f"\n cidade:{self.cidade}"
                f"\n Unidade Federativa{self.uf.sigla}"
                )
    

