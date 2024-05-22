from chessPictures import *
from interpreter import draw

def piezaColocada(pieza,casilla):
    newImg=[]
    color=casilla.img[0][0]
    for row in pieza.img:
        newImg.append(row.replace(" ",color))
    return Picture(newImg)

black_rock=rock.negative()
black_bishop=rock.negative()
black_knight=rock.negative()
black_queen=rock.negative()
black_king=rock.negative()
black_pawn=rock.negative()

draw(piezaColocada(rock,square))