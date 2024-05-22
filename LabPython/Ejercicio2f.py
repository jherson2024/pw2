from chessPictures import *
from interpreter import draw

def piezaColocada(pieza,casilla):
    newImg=[]
    color=casilla.img[0][0]
    for row in pieza.img:
        newImg.append(row.replace(" ",color))
    return Picture(newImg)

draw(piezaColocada(rock,square))