import database
from time import sleep

def menu():
    """
    -> make the menu
    """
    
    print('-=' * 10)
    print(f'{"Menu":^20}')
    print('-=' * 10)
    print('1 - Listar usuários')
    print('2 - Cadastrar usuário')
    print('3 - Editar usuário')
    print('4 - Deletar usuário')
    return '5 - Sair do sistema'

def answerCheck(num):
    if num <= 0 or num > 5:
        print('Erro! Digite uma opção válida')
    else:
        return num

try:
    database.createDataBase()
finally:
    while True:
        print(menu())
        try:
            answer = int(input('Digite uma opção: '))
            answerCheck(answer)
            sleep(1)
            if answer == 1:
                database.showUsers()
                sleep(1)
            if answer == 2:
                database.registerUser()
                sleep(1)
            if answer == 3:
                database.editUser()
                sleep(1)
            if answer == 4:
                database.deleteUser()
                sleep(1)
            if answer == 5:
                print('Até a próxima!')
                break
        except:
            print('Erro! Digite uma opção válida')