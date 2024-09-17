from models.classes.Endereco import Endereco
from models.abstracts.Pessoa import Pessoa

class Juridico(Pessoa):
    def __init__(self, nome, telefone, email,cnpj:str , inscricao_estadual:str  , endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.cnpj = cnpj
        self.inscricao_estadual=inscricao_estadual

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\no cnpj é :{self.cnpj}"
            f"\n a inscrição estadual é:{self.inscricao_estadual}"
            )





