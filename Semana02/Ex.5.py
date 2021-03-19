estudante = {'Nome': 'João', 'Idade': 25, 'Cursos': ['matemática', 'história']}

print(estudante.get('Nome'))

estudante['telefone'] = '9999-9999'

print(estudante.get('telefone'))

for chave, valor in estudante.items():
    print(chave, valor)