import time
# import threading
import concurrent.futures                       #Para utilizar o thread pool.


start = time.perf_counter()

def fazer_algo(segundos):                       #Função que irá esperar por determinado tempo;
    print(f'Dormir {segundos} segundo(s)...')   #Será utilizada para medir a diferença na eficiência ao se usar threads.
    time.sleep(segundos)
    return 'Chega de dormir...'


# fazer_algo()                                   //Chamando a função várias vezes sem utilizar threads.
# fazer_algo()
# fazer_algo()


#with concurrent.futures.ThreadPoolExecutor() as executor:               #Implementando Thread Pool.
#     sex = [5, 4, 3, 2, 1]
#     results = [executor.submit(fazer_algo, sec) for sec in sex]
#
#     for f in concurrent.futures.as_completed(results):
#         print(f.result())

with concurrent.futures.ThreadPoolExecutor() as executor:             #Implementando threads usando o método 'map()'.
    sex = [5, 4, 3, 2, 1]
    results = executor.map(fazer_algo, sex)

    for result in results:
        print(result)

#
# threads = []                                    #Lista vazia de threads que será utilizada no loop de join.
#
# for _ in range(10):                             #Loop que irá iniciar diversas threads simultâneas.
#     t = threading.Thread(target=fazer_algo, args=[1.5])
#     t.start()
#     threads.append(t)
#
# for thread in threads:                          #Loop de join, irá esperar todas as threads terminarem para prosseguir.
#     thread.join()
#

finish = time.perf_counter()

print(f'Terminou em {round(finish-start, 4)} seconds(s)')
