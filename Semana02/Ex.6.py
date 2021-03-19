linguagem = 'Cobol'

if linguagem == 'Python':
    print('Linguagem é: ' + linguagem)
elif linguagem == 'Java':
    print('Linguagem é:' + linguagem)
else:
    print('A linguagem é desconhecida')


user = 'Admin'
logged_in = True

if user == "Admin" or logged_in:
    print('Página do administrador')
else:
    print('Bad Creds')


if not logged_in:
    print('Please Log In')
else:
    print('Bem vindo!')

