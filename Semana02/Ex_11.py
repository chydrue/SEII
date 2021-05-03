



with open('teste.txt', 'r') as f:

    size_to_read = 100
    f_contents = f.read(size_to_read)

    print(f_contents, end ='')


   # for line in f:
   #     print(line, end='')

    # print(f.name)
    # f_contents = f.readline()
    # print(f_contents)


# print(f.closed)


# f = open('teste.txt','r')
#
# print(f.mode)
#
# f.close()
