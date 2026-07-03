import sqlite3 

banco = sqlite3.connect('login.db')

cursor = banco.cursor()

# cursor.execute("CREATE TABLE users (id integer, name text, birthdate text, email text)")

def showUsers():
    cursor.execute("select * from users")
    print(cursor.fetchall())

def registerUser():
    
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
                day = int(input("Dia: "))
                if day >= 32 or day <= 0:
                    print("Digite o dia corretamente.")
                else:
                    break
        except:
            print('Erro! Digite a data corretamente.')

        try:
            thirtyOne = [4, 6, 9, 11]
            while True:
                month = int(input("Mês: "))
                if month > 12 or month < 1:
                    print("Digite o mês corretamente")
                if day > 28 and month == 2:
                    print('Erro! Esse mês não possui mais de 28 dias')
                elif month in thirtyOne:
                    print('Erro! Esse mês não possui 31 dias')
                else:
                    break                       
        except:
            print('Erro! Digite o mês corretamente')
            
        try:
            while True:
                year = int(input("Ano: "))
                year = str(year)
                if len(year) > 4 or len(year) < 3:
                    print("Digite o ano corretamente.") 
                else:
                    break
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
    
    getName()
    getBirthDate()
    getEmail()
    print('-=' * 20)
    print(f'Dados:\nNome: {name}\nData de nascimento: {day}/{month}/{year}\nE-mail: {email}')
    print('-=' * 20)
    try:
        answer = str(input('Deseja inserir esses dados? [S/N]: '))
        if answer[0] in 'Nn':
            print('Qual elemento você deseja editar?\n1 - Nome\n2 - Dia\n3 - Mês\n4 - Ano\n5 - E-mail\n6 - Nenhum')
    except:
        print('testando')






registerUser()