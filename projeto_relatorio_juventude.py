from arquivo import gerar_relatorioJ
from interface import *

menuOpc = ['Cadastrar Conteúdo', 'Visualizar conteúdo', 'Gerar relatório', 'Sair']
aula = {'T5':[]}
while True:
    opc = menuPrincipal(menuOpc)
    if opc == 1:
        cabecalho('Cadastrar Conteúdo')
        while True:
            ensinamentos = str(input('Informe os conteúdos trabalhados: '))
            aula[f'T5'].append(ensinamentos)
            resp = validar()
            if resp in 'N':
                break
    elif opc == 2:
        cabecalho('VISUALIZAR RELATÓRIO')

        resumo(aula)

    elif opc == 3:
        cabecalho('Gerar Relatório')

        gerar_relatorioJ(aula)
        # Limpa o dicionario para um novo relatório
        aula = {'T5': []}

    elif opc == 4:
        print('Saindo do sistema... Até logo!')
        break
    else:
        print('Opção inválida! Tente novamente')