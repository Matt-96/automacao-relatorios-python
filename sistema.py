from arquivo import gerar_docx
from interface import *
menu_de_opcoes = ['Cadastrar Conteúdo (T1 - T4)', 'Visualizar Relatorios', 'Gerar Documento (.docx)', 'Sair do Sistema']
menuOpc = ['Turma 1', 'Turma 2', 'Turma 3', 'Turma 4']
# Guarda as turmas, e a lista de cada turma guarda os conteúdos trabalhados.
aulas = {'T1': [],
         'T2': [],
         'T3': [],
         'T4': []}
while True:
    opc = menuPrincipal(menu_de_opcoes)
    if opc == 1:
        cabecalho('CADASTRAR CONTEÚDO T1 - T4')
        print('Selecione a turma para cadastrar o conteúdo: ')


        turma = menu(menuOpc)

        while True:
            conteudo = str(input('Informe os conteúdos trabalhados: '))
            aulas[f'T{turma}'].append(conteudo)

            resp = validar()
            if resp in 'N':
                break

    elif opc == 2:
        cabecalho('VISUALIZAR RELATÓRIOS')

        resumo(aulas)

    elif opc == 3:
        cabecalho('GERAR DOCUMENTO(.docx)')
        gerar_docx(aulas)
        # Apaga o conteúdo anterior para abrir11
        # espaço para novos relatórios
        aulas = {'T1': [],
                 'T2': [],
                 'T3': [],
                 'T4': []}


    elif opc == 4:
        print('Saindo do sistema... Até logo!')
        break

    else:
        print('Opção inválida! Tente novamente')