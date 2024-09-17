import os 
from models.classes.Juridico import Juridico
from models.classes.Endereco import Endereco
from models.enum.Unidade_federativa import Unidade_federativa

os.system("cls|| clear")

endereco = Endereco("rua do Fim","14","40015,655","ao lado da green house","salvador",Unidade_federativa.BAHIA)
juridico= Juridico("Atila silva", "71 99999-9999","atila@145","1234315245","sfaeq",endereco)


print(juridico)