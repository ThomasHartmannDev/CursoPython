# from Pacote1 import modulo1
# from Pacote2 import modulo1
# Temos impotações de modulos com mesmo nome e isso gera um conflito porem exist
# um jeito de se resolver isso.

from Pacote1 import modulo1 as modulo1_soma
from Pacote2 import modulo1 as modulo1_sub
# nos demos "apelidos" para os modulos assim chamamos eles apartir do apelido agora.

print(f'Soma 2 + 5 = {modulo1_soma.soma(2,5)}')
print(f'Subtração 3 - 5 = {modulo1_sub.sub(3,6)}')