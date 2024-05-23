from chessPictures import *
from interpreter2 import draw2

#pintar el tablero  
blackSquare=square.negative()
fila8=square.join(blackSquare).horizontalRepeat(4)
fila7=blackSquare.join(square).horizontalRepeat(4)
draw2(fila8.under(fila7).verticalRepeat(4))

#pintar las piezas
draw2(rock)