from colorama import init, Fore, Style
from numeros import leiaInt
from docx import  Document

init(autoreset=True)
def linha():
    print('-' * 50)


def cabecalho(msg):
    linha()
    print(f'{msg:^50}')
    linha()


def menuPrincipal(lista):
    cabecalho('SISTEMA DE RELATÓRIOS')
    c = 1
    for item in lista:
        print(Fore.YELLOW + f'{c}', '-',Fore.BLUE + f'{item}')
        c+=1
    linha()
    opc = leiaInt(Fore.GREEN + 'Sua opção:')
    return opc

def validar(msg='Deseja continuar? [S / N]'):
    while True:
        resp = str(input(msg)).strip().upper()[0]
        if resp in 'SN':
            return resp
        print(Fore.RED + 'ERRO! Digite apenas S ou N!')

def menu(lista):
    cabecalho('ESCOLHA UMA OPÇÃO')
    c = 1
    for item in lista:
        print(f'{c}', '-', f'{item}')
        c+=1
    linha()
    while True:
        opc = leiaInt(Fore.GREEN + 'Sua opção:')
        if opc > len(lista) or opc < 1:
            print('Por favor, selecione uma opção válida.')
        else:
            return opc


def resumo(dados):
    cabecalho('RESUMO GERAL DAS TURMAS')

    # Cabeçalho da Tabela
    print(f'{"TURMA":<10} | {"CONTEÚDOS TRABALHADOS"}')
    linha()
    # aqui, turma é a chave, lista o valor.
    for turma, lista in dados.items():
        # Tratando a exibição da lista (Lógica do "e" final)
        if not lista:
            txt_conteudo = "Nenhum conteúdo"
        elif len(lista) == 1:
            txt_conteudo = lista[0]
        else:
            txt_conteudo = ", ".join(lista[:-1]) + " e " + lista[-1]

        # Exibindo a linha da tabela com alinhamento
        print(f'{turma:<10} | {txt_conteudo}')

    linha()



