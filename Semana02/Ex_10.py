import os

# print(os.getcwd())
#
# os.chdir('E:\ckmf\Livraiada\Bibliografia ufu\Sistemas Digitais')
#
# print(os.getcwd())
# print(os.listdir())
#
# os.removedirs('teste/subpasta')
# os.makedirs('teste/subpasta')
#
# os.rename('Sistemas Embarcados II - Apresentação.pdf', 'Sistemas Embarcados 2 - Apresentação.pdf')
# print(os.stat('Sistemas Embarcados 2 - Apresentação.pdf'))
#
for dirpath, dirnames, filenames in os.walk('E:\ckmf\Livraiada\Bibliografia ufu\Sistemas Digitais'):
    print(dirpath)
    print(dirnames)
    print(filenames)
    print()

