from colorama import *
def fatorial(n):
    f = 1
    for c in range(1, n+1):
        f *= c
    return f


def dobro(n):
    return n * 2


def triplo(n):
    return n * 3


def leiaInt(msg):
    from colorama import Fore,  init
    init(autoreset=True)
    while True:
        try:
            n = input(msg)
            return  int(n)
        except ValueError:
            print(Fore.RED + 'ERRO! Digite um número inteiro válido.')
        except KeyboardInterrupt:
            print(Fore.RED + 'O usuário preferiu não informar esse valor')
            break



def leiaFloat(msg):
    from colorama import Fore,  init
    init(autoreset=True)
    while True:
        try:
            n = input(msg).strip().replace(',', '.')
            return float(n)
        except ValueError:
            print(Fore.RED + 'ERRO! Digite um número float válido.')
        except KeyboardInterrupt:
            print(Fore.RED + 'O usuário preferiu não informar esse valor')
            break

