from chessPictures import *
from interpreter import draw

def piezaColocada(pieza,casilla):
    newImg=[]
    color=casilla.img[0][0]
    for row in pieza.img:
        newImg.append(row.replace(" ",color))
    return Picture(newImg)

black_rock=rock.negative()
black_bishop=bishop.negative()
black_knight=knight.negative()
black_queen=queen.negative()
black_king=king.negative()
black_pawn=pawn.negative()
black_square=square.negative()

#octava fila
fila8=piezaColocada(black_rock,square).join(piezaColocada(black_knight,black_square)).join(piezaColocada(black_bishop,square)).join(piezaColocada(black_queen,black_square)).join(piezaColocada(black_king,square)).join(piezaColocada(black_bishop,black_square)).join(piezaColocada(black_knight,square)).join(piezaColocada(black_rock,black_square))
fila7=piezaColocada(black_pawn,black_square).join(piezaColocada(black_pawn,square)).horizontalRepeat(4)
fila6=square.join(black_square).horizontalRepeat(4)
fila5=fila6.verticalMirror()
fila4=fila6
fila3=fila5
fila2=fila7.negative()
fila1=fila8.negative()
draw(fila8.under(fila7).under(fila6).under(fila5).under(fila4).under(fila3).under(fila2).under(fila1))