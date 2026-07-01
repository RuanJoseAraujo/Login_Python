import database

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
        print('Erro! Digite uma opção válida.')
    else:
        return num


print(menu())
while True:
    try:
        answer = int(input('Digite uma opção: '))
        answerCheck(answer)
    except:
        print('Erro! Digite uma opção válida')