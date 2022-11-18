
# Importar librerías
import os
import imageio

# Ubicación donde se encuentran sus imagenes
path = '/home/mario/Escritorio/crear_GIF/imagenes/'
archivos = sorted(os.listdir(path))
img_array = []

#Leer todos los archivos formato imagen desde path
for x in range(0, len(archivos)):
    nomArchivo = archivos[x]
    dirArchivo = path + str(nomArchivo)
    print(dirArchivo)
   
   #imprimir en terminal
    leer_imagenes = imageio.imread(dirArchivo)    
    img_array.append(leer_imagenes)
    #guardar el GIF
    imageio.mimwrite('archivoCreado.gif', img_array, 'GIF', duration=0.1)
