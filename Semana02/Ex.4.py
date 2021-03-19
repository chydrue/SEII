
#######################################################################################################################
#LISTAS
#######################################################################################################################

cursos = ['história', 'matemática', 'física', 'ciência da computação']
cursos_2 = ['arte', 'educação']
print(cursos)

cursos.append('mecatrônica')
print(cursos)

cursos.extend(cursos_2)
print(cursos)

cursos.insert(2, 'mecânica')
print(cursos)

popped = cursos.pop()
print(popped)

cursos.sort()
print(cursos)

cursos.reverse()
print(cursos)

sorted_cursos = sorted(cursos)
print(sorted_cursos)

for curso in cursos:
    print(curso)

for index, curso in enumerate(cursos):
    print(index, curso)

curso_str = ' - '.join(cursos)
print(curso_str)

#######################################################################################################################
#TUPLAS
#######################################################################################################################

tupla_1 = ('história', 'matemática', 'física', 'etc')
tupla_2 = tupla_1

print(tupla_1)
print(tupla_2)

tupla_1[0] = 'arte'

print(tupla_1)
print(tupla_2)

#######################################################################################################################
#SETS
#######################################################################################################################

cursos3 = set('etc', 'etc', 'etc', 'etc')
print(cursos3)