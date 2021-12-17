"""
Enunciado
Super desafio! Faça um sistema de cadastro de clientes. Modele cada cliente como uma lista de três elementos: nome, CPF e e-mail.

a. Faça uma função que peça o nome, o CPF e o e-mail da pessoa e retorne uma lista contendo esses elementos nessa ordem.

b. Os clientes cadastrados devem ser armazenados em uma lista (uma lista de listas, já que cada cliente será uma lista tal como 
produzido no item a).

c. Faça uma função que recebe a lista do item b) e um CPF e, se esse cliente estiver na lista de cadastro, sua função deve devolver 
a lista de dados desse cliente; caso contrário, sua função deve imprimir “não encontrado”.

d. Enquanto não for digitado 0, o seu programa deve continuar rodando. Se digitado 1, seu programa deve cadastrar um novo cliente; 
se digitado 2, seu programa deve pedir um CPF e procurá-lo na lista de clientes (item c); se digitado 3, seu programa deve imprimir 
todos os clientes cadastrados.
"""

def registerClient():
    name = input('Insert the name: ')
    cpf = int(input('Insert the ID: '))
    email = input('Insert the e-mail: ')

    print(f'Client {name} registered with ID {cpf} and E-mail {email}.')
    
    return [name, cpf, email]

def checkId(clientList, cpf):
    
    for client in clientList:
        if cpf in client:
            return client
    print(f'Client with ID {cpf} not found.')
    return []

def clientInfo(client):
    print(f'Name: {client[0]}\nID:{client[1]}\nE-mail:{client[2]}')

clientList = []


choice = int(input('\n\u001b[36mMenu\u001b[37m\n1 - Register client\n2 - Search client\n3 - Display clients\n0 - Exit\n'))
while choice != 0:

    if choice == 1:
        print('\u001b[36m Registering new client: \u001b[37m')
        clientList.append(registerClient())

    elif choice == 2:
        print(clientList)
        if not clientList:
            print('Register list is empty.')
        else:
            print('\u001b[36m Searching client: \u001b[37m')
            cpf = int(input('Type ID number: '))
            client = checkId(clientList, cpf)
            clientInfo(client)
            

    elif choice == 3:
        if not clientList:
            print('Register list is empty.')
        else:
            print('\u001b[36m Displaying clients: \u001b[37m')
            for client in clientList:
                clientInfo(client)
        
    else:
        print('\u001b[36m Invalid input, type again: \u001b[37m')

    choice = int(input('Menu\n1 - Register client\n2 - Search client\n3 - Display clients\n0 - Exit\n'))