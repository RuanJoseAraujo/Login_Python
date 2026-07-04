import sqlite3 
from time import sleep


def createDataBase():
    global cursor, banco
    banco = sqlite3.connect('login.db')
    cursor = banco.cursor()
    try:
        cursor.execute("CREATE TABLE users (id integer primary key, name text, birthdate text, email text)")
    except:
        return ''

def showUsers():
    print('-=' * 20)
    for c in (cursor.execute("select * from users")):
        print(c,end='\n')
    print('-=' * 20)

def getName():
        global name
        try:
            while True:
                name = str(input("Digite o nome: ")).strip()
                noSpaceName = name.replace(' ', '')
                if name.isnumeric() == True:
                    print('Erro! Digite um nome válido')
                elif noSpaceName.isalpha() == False:
                    print('Erro! Digite um nome válido')
                else:
                    break
        except (KeyboardInterrupt):
            print('Erro! Não foi passado nenhum valor')

def getBirthDate():
        global day, month, year
        try:
            print('Digite sua data de nascimento: ')
            while True:
                try:
                    day = int(input("Dia: "))
                    if day >= 32 or day <= 0:
                        print("Digite o dia corretamente.")
                    else:
                        break
                except:
                    print('Erro! Digite o dia corretamente.')
        except:
            print('Erro! Digite o dia corretamente.')

        try:
            thirty = [4, 6, 9, 11]
            while True:
                try:
                    month = int(input("Mês: "))
                    if month > 12 or month < 1:
                        print("Digite o mês corretamente")
                    elif day > 28 and month == 2:
                        print('Erro! Esse mês não possui mais de 28 dias')
                    elif day == 31 and month in thirty:
                        print('Erro! Esse mês não possui 31 dias')
                    else:
                        break           
                except:
                    print('Erro! Digite o mês corretamente')            
        except:
            print('Erro! Digite o mês corretamente')
            
        try:
            global birthDate
            while True:
                try:
                    year = int(input("Ano: "))
                    year = str(year)
                    if len(year) != 4:
                        print("Digite o ano corretamente.") 
                    else:
                        birthDate = (f'{year}-{month}-{day}')
                        break
                except:
                    print('Erro! Digite o ano corretamente.')
        except:
            print('Erro! Digite o ano corretamente.') 

def getEmail():
        global email
        try:
            while True:
                email = str(input('Digite seu e-mail: '))
                countA = email.count('@')
                countDotCom = email.count('.com')
                whereA = email.find('@')
                size = len(email)
                whereDotCom = email.find('.com')
                math = size - whereDotCom
                if countA == 1 and countDotCom == 1 and whereA != 0 and math == 4:
                    break
                else:
                    print('Erro! Digite um email válido')
        except:
            print('Erro! Digite um e-mail válido')

def registerUser():
    print('-=' * 20)
    getName()
    getBirthDate()
    getEmail()

    while True:
        try:
            print('-=' * 20)
            print(f'Dados:\nNome: {name}\nData de nascimento: {day}/{month}/{year}\nE-mail: {email}')
            print('-=' * 20)
            answer = str(input('Deseja inserir esses dados? [S/N]: '))
            if answer[0] in 'Nn':
                editing = int(input('Qual elemento você deseja editar?\n1 - Nome\n2 - Data de nascimento\n3 - E-mail\n4 - Nenhum\nOpção: '))
                if editing == 1:
                    getName()
                elif editing == 2:
                    getBirthDate()
                elif editing == 3:
                    getEmail()
                elif answer[0] == 4:
                    break 
            elif answer[0] in 'Ss':
                cursor.execute("INSERT INTO users (id ,name, birthdate, email) VALUES ( NULL, '"+name+"', '"+birthDate+"', '"+email+"')")
                banco.commit()
                for c in range(0,3):
                    print('.',end=' ', flush=True)
                    sleep(.5)
                print('Cadastro realizado!')
                break       
        except Exception as error:
            print(error.__cause__)
            print(error.__class__)

def editUser():
    try:
        showUsers()
        edit = int(input("Qual registro você deseja editar? "))
        validation = cursor.execute("SELECT * FROM users WHERE id = "+str(edit)+"")
        if len(validation.fetchall()) == 1:
            show = cursor.execute("SELECT * FROM users WHERE id = "+str(edit)+"")
            print(show.fetchall())
            try:
                makeSure = str(input('Deseja editar esse registro? [S/N] ')).upper().strip()
                if makeSure[0] in 'S':
                    getName()
                    getBirthDate()
                    getEmail() 
                    print('-=' * 20)
                    print(f'Dados:\nNome: {name}\nData de nascimento: {day}/{month}/{year}\nE-mail: {email}')
                    print('-=' * 20)
                    makeSure = str(input('Deseja realizar esse registro? [S/N] ')).upper().strip()
                    if makeSure[0] in 'S':
                        cursor.execute("UPDATE users SET name = '"+str(name)+"', birthdate = '"+str(birthDate)+"', email = '"+str(email)+"' WHERE id = "+str(edit)+"") 
                        banco.commit()
                        for c in range(0,3):
                            print('.',end=' ', flush=True)
                            sleep(.5)
                        print('Registro editado!')
            except (KeyboardInterrupt):
                print('Erro! Digite alguma opção')
            except:
                print('Erro! Opção inválida')    
        else:
            print('Erro! Opção inválida')
    except Exception as error:
        print(error.__class__)

def deleteUser():
    showUsers()
    try:
        answer = int(input('Qual registro você deseja deletar? '))
        validation = cursor.execute("SELECT * FROM users WHERE id = "+str(answer)+"")
        if len(validation.fetchall()) == 1:
            show = cursor.execute("SELECT * FROM users WHERE id = "+str(answer)+"")
            print(show.fetchall())
            makeSuke = str(input('Deseja exluir esse registro? [S/N] ')).upper().strip()
            if makeSuke[0] in 'S':
                cursor.execute("DELETE FROM users WHERE id = "+str(answer)+"")
                banco.commit()
                for c in range(0,3):
                    print('.',end=' ', flush=True)
                    sleep(.5)
                print('Usuário deletado!')
    except KeyboardInterrupt:
        print('Erro! Nenhum valor inserido')
    except:
        print('Erro! Opção inválida')