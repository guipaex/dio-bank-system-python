menus = {
    'Menu Principal': [
        { 'key': 1, 'option': 'Entrar'},
        { 'key': 2,'option': 'Cadastrar'},
        { 'key': 0,'option': 'Encerrar Sistema'},
    ],
    'Menu de Usuário': [
        { 'key': 1, 'option': 'Selecionar conta'},
        { 'key': 2,'option': 'Criar uma nova conta'},
        { 'key': 0,'option': 'Encerrar Sessão'},
    ],
    'Menu da Conta': [
        { 'key': 1, 'option': 'Sacar'},
        { 'key': 2,'option': 'Depositar'},
        { 'key': 3,'option': 'Ver Extrato'},
        { 'key': 9,'option': 'Trocar de Conta'},
        { 'key': 0,'option': 'Encerrar Sessão'},
    ]
}

def main():
    print( f'''\n=============== PyBank ===============\n''')
    while True:
        print( f'''\n=============== Menu Principal ===============\n''')
        displayMenu(menus['Menu Principal'])
        option = int(input('Digite o número da opção: '))

        if option == 1:
            logIn()
        elif option == 2:
            createUser()
        elif option == 0:
            print('Encerrando o sistema...\n')
            break
        else:
            print("Opção inválida. Tente novamente.")

def displayMenu(menu):
            for item in menu:
                if item['key'] == 0:
                    print(f'\n[{item['key']}] {item['option']}\n')
                else:
                    print(f'[{item['key']}] {item['option']}')

def logIn():
    cpf = input('Digite seu CPF: ')
    for user in users:
        if user['cpf'] == cpf:
            currentUser = user
        else:
            print('CPF não cadastrado. Deseja realizar o cadastro?.')
            action = int(input(f'[1] Cadastrar CPF! \n[2] Tentar novamente.'))
            if action == 1:
                break
            else:
                logIn()

    if len(currentUser['accounts']) > 1:
        print('Selecione uma conta para operar:\n')
        for account in currentUser['accounts']:
            print(f'[{account['n']}] Conta {account['n']}  - Saldo: R$ {account['balance']:.2f}')           
        selectedAccount = int(input('\nDigite o número da conta: '))
        print(f'Conta {selectedAccount} selecionada.')
    else:
        selectedAccount = currentUser['accounts'][0]

    sectionData = {
        'name': currentUser['name'],
        'account': currentUser['accounts'][selectedAccount - 1]
    }

    accountMenu(sectionData)

def handleErrors(params, target):
    if target == 'menuOptions':
        if params[0] not in params[1]:
            print(f'\n::::::::: Operação inválida! :::::::::\nDigite um valor entre {min(params[1])} e {max(params[1])}.')

def accountMenu(accountData):
    DAILY_WHITDRAW_LIMIT = 3
    withdraws = 0
    currentAccount = accountData['account']
    while True:
        print( f'''\n=============== Menu da Conta ===============\n''')
        print(f'Olá, {accountData["name"]}! Seu saldo atual é de R$ {currentAccount["balance"]:.2f}\n')
        displayMenu(menus['Menu da Conta'])
        option = int(input('Qual operação deseja realizar? '))

        if option == 1:
            if withdraws < DAILY_WHITDRAW_LIMIT:
                withdraw(int(input('Digite o valor do saque: ')), currentAccount)
                withdraws += 1
            else:
                print('Limite de saques diários atingido. Por favor, tente novamente mais tarde.')
        elif option == 2:
            deposit(currentAccount, int(input('Digite o valor do depósito: ')))
        elif option == 3:
            statement(currentAccount)
        elif option == 9 or option == 0:
            break

#Função de Depósito (Positional Only)
def deposit(account, value):
    if value > 0:
        account['balance'] += value
        account['extract'].append(f"+ DEPÓSITO: R$ {value:.2f}")
        print(f'Depósito realizado com sucesso!. Seu novo saldo é de R$ {account["balance"]:.2f}.')
    else:
        print('O valor informado é inválido.')
    
    return account['balance'], account['extract']

# Função de Saque (Keyword Only)
def withdraw(value, account):
    MAX_WITHDRAW = 500
    if value < 0:
        print(f'Valor de saque inválido!. Por favor digite um valor acima de R$ 0.00.')
    else:
        if value <= account['balance']:
            if value <= MAX_WITHDRAW:
                account['balance'] -= value
                account['extract'].append(f"- SAQUE: R$ {value:.2f}")
                print(f'Saque realizado com sucesso!. Seu novo saldo é de R$ {account["balance"]:.2f}.')
            else :
                print(f'Limite de saque excedido!. Por favor digite um valor menor ou igual a R$ {MAX_WITHDRAW:.2f}.')
        else:
            print(f'Saldo insuficiente!. Seu saldo é de R$ {account["balance"]:.2f}.')

# Função de Extrato (Positional'Saldo' and Keyword'Extrato')
def statement(account):
    print(f'\n ======= EXTRATO ======\n')
    for transaction in account['extract']:
        print(f'{transaction}')
    print(f'\n ======= SALDO FINAL R$ {account["balance"]:.2f} ======\n')


# Função de Cadastro de Usuário (nome, cpf, data de nascimento e endereço)
def createUser():
    cpf = input('Digite seu CPF: ')
    for user in users:
        if user['cpf'] == cpf:
            print('CPF ja existente. Por favor digite outro.')
            return createUser()
    name = input('Digite seu nome: ')
    birthdate = input('Digite sua data de nascimento: ')
    address = input('Digite seu endereço: ')

# Função de cadastrar Conta Bancária (cpf)
# agency = '0001'
# accounts = sum(len(user['accounts']) for user in users)
# accountNumber = accounts + 1

# Função de listar Contas Bancária (cpf)

###############################################################################

users = [
    {
        'name':'John Doe',
        'birthdate':'01/01/2000',
        "cpf":"123",
        'address':'Rua Fulano, 123 - Tiramissu - Belo Horizonte/MG',
        'accounts':[
            {
                'agency':'0001',
                'n':1,
                'satus': 'active',
                'balance':0,
                'extract':[]
            },
             {
                'agency':'0001',
                'n':2,
                'satus': 'active',
                'balance':50,
                'extract':[]
            }
        ]
    }
]

main()