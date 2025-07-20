
'''
depedendo da versão do python o arquivo precisa ser iniciado com um aquivo 
.init
olhar a frescura do pep 8
pypi.org tem as bibliotecas disponíveis de terceiros
'''



'''

O que é um módulo: São todos os tipos de arquivos criados para organizar e facilitar a manutenção dos códigos. 
Um módulo é um arquivo Python contendo funções, classes e variáveis.

boa prática: sempre colocar os imports no topo do código.

'''
# Formas de importar módulos:
# import nome_do_modulo  #| para importar o modulo completo

# from nome_do_modulo import nome_da_função #| para importar uma função específica

# from nome_do_modulo import (func1, func2) #| mesma coisa da anterior mas segundo pep8 é uma boa pratica fazer dessa forma e até espaçando entre elas

# from nome_do_modulo import * #| é igual ao primeiro caso mas a diferença vem com a chamada da função ao invés de precisar do nome_do_modulo.nome_da_função() você só usaria o nome_da_função()

# from pacote.nome_do_modulo import nome_da_função #| nesse caso o "pacote" seria uma pasta externa ao código e não mais apenas um arquivo, logo pegariamos o nome_da_pasta.nome_do_modulo_dentro_da_pasta.nome_da_função

# import nome_do_modulo as apelido #| é usado quando o nome do import está muito grande ai o apelido se torna o nome do módulo e ai ultilizamos ele para chamar a função:
'''
ex:
normal: from nome_do_modulo.nome_da_função()
apelido: import nome_do_modulo as apelido
chamada: apelido.nome_da_função()
'''




