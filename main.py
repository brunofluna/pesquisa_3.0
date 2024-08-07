# lista de cidades para pesquisar 
cidades = ['Brasília', 'Taguatinga', 'Planaltina', 'Ceilândia', 'Samambaia', 'Riacho fundo', 'Candangolândia', 'Núcleo bandeirante', 'Gama', 'Santa maria', 'Sobradinho', 'Planaltina', 'Recanto das emas', 'Guará', 'Valparaiso', 'Novo gama', 'Céu azul', 'Lago azul', 'Formosa', 'Sol nascente', 'Estrutural', 'Águas claras', 'Arniqueira', 'Areal', 'Sol nascente', 'Dvo', 'São Sebastião', 'Dvo']

# cidade a ser pesquisada
cidade_pesquisada = input('Cidade a ser pesquisada: ').capitalize()
# conta a quantidade de ocorrências da palavra
cont = cidades.count(cidade_pesquisada)
if cont == 1:
    print(f'\n{cidade_pesquisada} foi encontrada 1 vez\n')
else:
# exibe o resultado
    print(f'\n{cidade_pesquisada} foi encontrada {cont} vezes na lista.\n')