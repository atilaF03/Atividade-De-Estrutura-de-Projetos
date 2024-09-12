import os

class Endereco:
    def __init__(self, logradouro, numero, cep , complemento , cidade) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.cep = cep
        self.complemento = complemento
        self.cidade = cidade

    def __str__(self) -> str:
        return (f"\n Logradouro:{self.logradouro}"
                f"\n numero:{self.numero}"
                f"\n cep:{self.cep}"
                f"\n complemento:{self.complemento}"
                f"\n cidade:{self.cidade}"
                )
    

