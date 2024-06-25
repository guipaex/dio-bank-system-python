balance = 0
withdraw_limit = 500
extract = ""
daily_withdraws = 0
DAILY_LIMIT = 3
options = [0, 1, 2, 3]

signed = True

menu = '''===== MENU =====
|- [1] Depositar
|- [2] Sacar
|- [3] Extrato
|
|- [0] Sair
'''


while signed:

    print( f'''============= PyBank =============
    Seu saldo atual é de R$ {balance:.2f}
    '''
    )

    print(menu)

    selection = int(input('Escolha uma opção: '))

    if selection not in options:
        print('Operação inválida! Digite um valor entre 0 e 3.')

    if selection == 0:
        print('Finalizando o PyBank...')
        signed = False
        break

    if selection == 1:
        valor = float(input('Quanto deseja depositar? '))
        if valor > 0:
            balance += valor
            extract += f"+ DEPÓSITO: R$ {valor:.2f}\n"
            print(f'Você depositou R$ {valor:.2f}.\n')
        else:
            print('O valor informado é inválido.')
            break

    elif selection == 2:
        if daily_withdraws >= DAILY_LIMIT:
            print('Limite de saques diários excedido.')
            break
        else:
            value = float(input('Quanto deseja sacar? '))
            if value > 0 and value <= withdraw_limit and value <= balance:
                    balance -= value
                    daily_withdraws +=1
                    extract += f"- SAQUE: R$ {value:.2f}\n"
                    print(f'Você sacou R$ {value:.2f}.\nSeu saldo atual é de R$ {balance:.2f}.')
            
            elif value <= 0:
                print(f'Valor inválido. Digite um valor entre 0 e R$ {withdraw_limit}.')
            elif value > withdraw_limit:
                print(f'O Valor excede o limite de saque. Digite um valor entre 0 e R${withdraw_limit}.')
            elif value > balance:
                print(f'Saldo insuficiente. Digite um valor entre 0 e R$ {balance}.')

    elif selection == 3:
        print(f'''
============= Extrato =============
{'\nNão foram realizadas movimentações ainda. ' if not extract else extract}
''')
        print('==================================')