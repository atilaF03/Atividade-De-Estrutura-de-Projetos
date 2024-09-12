from abc import ABC,abstractmethod
from meu_projeto.classes.Endereco import Endereco

class pessoa(ABC):
    def __init__(self,nome,telefone,email, endereco: Endereco) -> None:
        self.nome= nome
        self.telefone= telefone
        self.email= email
      
        self.endereco = endereco

    def __str__(self) -> str:
        return(f"\no nome é:{self.nome}"
               f"\ntelefone :{self.telefone}"
               f"\nemail:{self.email}"
               f"\nendereço:{self.endereco}"
               )
     