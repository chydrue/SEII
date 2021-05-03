numeros = [1, 2, 3, 4, 5]

# for numeros in numeros:
#     if numeros == 3:
#         print('Achei!')
#         continue
#     print(numeros)


for numero in numeros:
    for letra in "abc":
        print(numero, letra)

for i in range(10):
    print(i)

x = 0

while x < 10:
    if x == 5:
        print('voila')
    print(x)
    x += 1
