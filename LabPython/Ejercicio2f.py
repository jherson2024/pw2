from chessPictures import *
from interpreter import draw

blackSquare=square.negative()
fila8=square.join(blackSquare).horizontalRepeat(4)
fila7=blackSquare.join(square).horizontalRepeat(4)
draw(fila8.under(fila7).verticalRepeat(2))
