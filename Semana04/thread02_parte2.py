import time
import concurrent.futures
from PIL import Image, ImageFilter

#O script irá processar as imagens baixadas no programa thread01_parte2


#Imagens a serem processadas:

img_names = [
    'photo-1516117172878-fd2c41f4a759.jpg',
    'photo-1532009324734-20a7a5813719.jpg',
    'photo-1524429656589-6633a470097c.jpg',
    'photo-1530224264768-7ff8c1789d79.jpg',
    'photo-1564135624576-c5c88640f235.jpg',
    'photo-1541698444083-023c97d3f4b6.jpg',
    'photo-1522364723953-452d3431c267.jpg',
    'photo-1513938709626-033611b8cc03.jpg',
    'photo-1507143550189-fed454f93097.jpg',
    'photo-1493976040374-85c8e12f0c0e.jpg',
    'photo-1504198453319-5ce911bafcde.jpg',
    'photo-1530122037265-a5f1f91d3b99.jpg',
    'photo-1516972810927-80185027ca84.jpg',
    'photo-1550439062-609e1531270e.jpg',
    'photo-1549692520-acc6669e2f0c.jpg'
]

#Início do contador:
t1 = time.perf_counter()


#Nós iremos redimensionar as imagens para o seguinte tamanho:
size = (1200, 1200)



#Definição da função de processamento:

def process_image(img_name):
    img = Image.open(img_name)                              #Abre determinada imagem
    img = img.filter(ImageFilter.GaussianBlur(15))          #Aplica um filtro de Desfoque Gaussiano na imagem
    img.thumbnail(size)                                     #Cria uma miniatura com o tamanho desejado
    img.save(f'processed/{img_name}')                       #Salva a imagem em um diretório para as imagens processadas
    print(f'{img_name} foi processada...')

#Será criado um Process Pool Executor que irá utilizar o método map() para criar um processo para cada imagem
#Desta forma o procedimento se tornará paralelo e muito mais eficiente.

with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(process_image, img_names)


t2 = time.perf_counter()

print(f'Finished in {t2-t1} seconds')