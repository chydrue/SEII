# def hello_func(saudação):
#     return '{}, Professor.'.format(saudação)
#
# print(hello_func('Bom dia'))
#
#
#
#
# cursos = ['matemática', 'arte']
# info ={'nome': 'Cleiton', 'idade':31}
#
#
# def estudante_info(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
# estudante_info(*cursos, **info)


dias_do_mês = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(ano):

    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 ==0)

def dias_no_mês(ano, mês):

    if not 1 <= mês <= 12:
        return 'Mês inválido.'

    if mês == 2 and is_leap(ano):
        return 29

    return dias_do_mês[mês]

print(dias_no_mês(2020, 2))