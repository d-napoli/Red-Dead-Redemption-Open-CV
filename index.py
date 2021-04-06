from PIL import ImageGrab
import numpy as np
import cv2
import time
import keys as k

keys = k.Keys()

def pathing(minimap):
    limite_inferior = np.array([100, 130, 100])
    limite_superior = np.array([150, 255, 255])

    hsv = cv2.cvtColor(minimap, cv2.COLOR_RGB2HSV)
    mascara = cv2.inRange(hsv, limite_inferior, limite_superior)

    matches = np.argwhere(mascara == 255) # array com os índices que batem o filtro da máscara
    
    caminho_encontrado = np.mean(matches[:,1]) # pega os valores do índice Y da variável matches
    centro_tela = minimap.shape[1] / 2 # pega o centro da tela, de acordo com o tamanho do mini mapa

    diferenca_centro = centro_tela - caminho_encontrado # a diferença do caminho atual até o centro da tela
    print(diferenca_centro)

    keys.directMouse(-1 * int(diferenca_centro * 1.6), 0)

    cv2.imshow("cv2screen", mascara)
    cv2.waitKey(5)

for i in range(5): # timeout antes de a execução começar
    print(i)
    time.sleep(1)

keys.directKey("w")

for i in range(40000):
    image_frame = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
    image_np = np.array(image_frame)
    tela = cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB)

    miniminimap = tela[710:780, 140:230]

    pathing(miniminimap)

    if(i % 10 == 0):
        keys.directKey("LSHIFT")

    if(i % 11 == 0):
        keys.directKey("LSHIFT", keys.key_release)

    # tela = cv2.resize(tela, (960, 540))
    # cv2.imshow("cv2tela", miniminimap)
    # cv2.waitKey(5)
keys.directKey("w", keys.key_release)
cv2.destroyAllWindows()