import os
import random

saldo = int(990)



# while (saldo >= int(1000)):
#     cupom = input("Seu saldo chegou a R$1000\nE você liberou um cupom surpresa\nDigite 'cupomsurpresa' para liberar.\n")
            
#     if cupom == 'cupomsurpresa':
#         saldo = saldo + 1000
#         print('PARABÉNS\nVocê acaba de liberar um cupom de R$1000\nValor já creditado em seu saldo')

#         break
#     else:
#         print('Cupom inválido.')
#     continue

while True:
    print('=' * 50)
    print('''
██████╗     ██╗   ██╗    ██████╗      █████╗     ███╗   ██╗    ██╗  ██╗
██╔══██╗    ╚██╗ ██╔╝    ██╔══██╗    ██╔══██╗    ████╗  ██║    ██║ ██╔╝
██████╔╝     ╚████╔╝     ██████╔╝    ███████║    ██╔██╗ ██║    █████╔╝ 
██╔═══╝       ╚██╔╝      ██╔══██╗    ██╔══██║    ██║╚██╗██║    ██╔═██╗ 
██║            ██║       ██████╔╝    ██║  ██║    ██║ ╚████║    ██║  ██╗
╚═╝            ╚═╝       ╚═════╝     ╚═╝  ╚═╝    ╚═╝  ╚═══╝    ╚═╝  ╚═╝
 ''')

    print('=' * 50)
    print('             Bem-vindo ao PyBank\n          Escolha uma das opções abaixo: ')
    print('       [v]er saldo - [s]acar saldo - [g]ame')
    print('=' * 50)
    escolha = input('Opção desejada: ')

    os.system('cls')

    try:
        if escolha == 'v':
            print('=' * 50)
            print(f'            Seu saldo atual é de R${saldo}')

        elif escolha == 's':
            valor_retirado = input('Qual valor deseja sacar: R$')
            valor_retirado = int(valor_retirado)

            if valor_retirado > saldo:       
                print('Você não pode sacar mais que seu saldo atual.')

            elif valor_retirado <= saldo:
                saldo = saldo - int(valor_retirado)
                print(f'Você retirou R${valor_retirado}, e seu saldo atual é de R${saldo}')

    except ValueError:
         os.system('cls')
         print('Somente números permitidos.')

    if escolha == 'g':
        print("Bem-vindo ao jogo 'Adivinhe o Número'!")
        print("Você tem 5 chances para ganhar um prêmio de R$100.")
        print("O valor para participar é de R$20.")
        taxa = input("\nDeseja continuar? (Digite [s] para SIM ou [n] para NÃO): ")


        if saldo <= int(19):
            os.system('cls')
            print('Saldo insuficiente.')
            continue
        elif taxa == 's':
            saldo = saldo - 20
            os.system('cls')
        elif taxa == 'n':
            os.system('cls')
            continue
        else:
            os.system('cls')
            print('Essa opção não existe.')
            continue       


        print('''
              
 ██▓███▓██   ██▓ ▄████ ▄▄▄      ███▄ ▄███▓█████ 
▓██░  ██▒██  ██▒██▒ ▀█▒████▄   ▓██▒▀█▀ ██▓█   ▀ 
▓██░ ██▓▒▒██ ██▒██░▄▄▄▒██  ▀█▄ ▓██    ▓██▒███   
▒██▄█▓▒ ▒░ ▐██▓░▓█  ██░██▄▄▄▄██▒██    ▒██▒▓█  ▄ 
▒██▒ ░  ░░ ██▒▓░▒▓███▀▒▓█   ▓██▒██▒   ░██░▒████▒
▒▓▒░ ░  ░ ██▒▒▒ ░▒   ▒ ▒▒   ▓▒█░ ▒░   ░  ░░ ▒░ ░
░▒ ░    ▓██ ░▒░  ░   ░  ▒   ▒▒ ░  ░      ░░ ░  ░
░░      ▒ ▒ ░░ ░ ░   ░  ░   ▒  ░      ░     ░   
        ░ ░          ░      ░  ░      ░     ░  ░
        ░ ░                                     
  ''')

    
        chances = 5
        num_aleatorio = random.randrange(0, 100)
        num_alea_fixo = num_aleatorio
        entre_maior = num_alea_fixo + int(random.randrange(0, 10))
        entre_menor = num_alea_fixo - int(random.randrange(0, 10))

    while (escolha == 'g'):
 
        entre_maior_fixo = entre_maior
        entre_menor_fixo = entre_menor


        num_escolhido = input('Escolha um número de 0 a 100: ')
        print(f'Número de chances: {chances}')

        os.system('cls')
        try:
            if num_alea_fixo == int(num_escolhido):
                saldo = saldo + 100
                print("""
 █████╗    ██████╗  ███████   ██████╗   ████████╗   ██████╗   ██╗   ██╗  ██╗
██╔══██╗  ██╔════╝  ██╔════╝  ██╔══██╗  ╚══██╔══╝  ██╔═══██╗  ██║   ██║  ██║
███████║  ██║       █████╗    ██████╔╝     ██║     ██║   ██║  ██║   ██║  ██║
██╔══██║  ██║       ██╔══╝    ██╔══██╗     ██║     ██║   ██║  ██║   ██║  ╚═╝
██║  ██║  ╚██████╗  ███████╗  ██║  ██║     ██║     ╚██████╔╝  ╚██████╔╝  ██╗
╚═╝  ╚═╝   ╚═════╝  ╚══════╝  ╚═╝  ╚═╝     ╚═╝      ╚═════╝    ╚═════╝   ╚═╝                                                                                        
""")
                print('Parabéns, você acaba de ganhar R$100!')
                qualquer_coisa = input('Digite algo para sair: ')  
                os.system('cls')
                break

        except ValueError:
            os.system('cls')
            print('Letras e outros caracteres não são permitidos.')
            continue
        except Exception:
            os.system('cls')
            print('Erro desconhecido.')
            continue

        if num_alea_fixo != num_escolhido:
                chances = chances - 1

        if chances > 0:
                print('----------------------------')
                print('       POXA VOCÊ ERROU!     ')
                print('----------------------------')

                print(f'Número de chances: {chances}')
                # print(num_alea_fixo)
                print(f'DICA: o número está entre {entre_menor} e {entre_maior}.')

                continue

        elif chances <= 0:
                print('Suas chances esgotaram :( ')
                qualquer_coisa = input('Digite algo para sair: ')
                os.system('cls')
                break      



