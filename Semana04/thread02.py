import time
import multiprocessing
import concurrent.futures
start = time.perf_counter()

def faz_algo(segundos):
    print(f'Dormir {segundos} segundo...')
    time.sleep(segundos)
    return 'Chega de dormir...'



#De forma análoga ao uso das threads nós iremos criar cada processo e executar o join.
#Porém os processos executam de forma completamente paralela, iniciando ao mesmo tempo.

# p1 = multiprocessing.Process(target=faz_algo)
# p2 = multiprocessing.Process(target=faz_algo)
#
# p1.start()
# p2.start()
#
# p1.join()
# p2.join()



#Agora utilizaremos o loop para criar diversos processos

# processes = []     #Lista vazia de processos, será incrementada no loop principal e utilizada para o laço de join.
#
# for _ in range(10):
#     p = multiprocessing.Process(target=faz_algo, args=[1.5])
#     p.start()
#     processes.append(p)
#
# for process in processes:
#     process.join()


#Utilizaremos agora um Process Pool Executor, que implementa a iteração de processos de forma automatizada.

#O método submit() roda a função e retorna um "future object".
#Um future object encapsula as informações de saída para podermos analisá-las.



# with concurrent.futures.ProcessPoolExecutor() as executor:
#     results = [executor.submit(faz_algo, 1) for _ in range(10)]      #Utilizamos uma list comprehension para o loop.
#
#     for f in concurrent.futures.as_completed(results):
#         print(f.result())



#Vamos utilizar agora uma lista para criar os processos

# with concurrent.futures.ProcessPoolExecutor() as executor:
#     secs = [5, 4, 3, 2, 1]
#     results = [executor.submit(faz_algo, secs) for sec in secs]
#
#     for f in concurrent.futures.as_completed(results):
#         print(f.result())
#
# #Nota-se que os resultados são gerados de forma aleatória, pois os processos são criados paralelamente.


with concurrent.futures.ProcessPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]
    results = executor.map(faz_algo, secs)

    for result in results:
        print(result)

#Quando usamos submit() são criados Future Objects, mas quando utilizamos map() são utilizados apenas os resultados.


finish = time.perf_counter()

print(f'Terminou em {round(finish-start, 2)} segundos(s)')