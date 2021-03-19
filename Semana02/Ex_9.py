print('Imported my_module')

test = 'Test String'

def find_index(to_search, target):
    "Encontra o index de um valor em uma sequência"
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1


