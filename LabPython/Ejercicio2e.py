from chessPictures import *
from interpreter import draw

blackSquare=square.negative()
draw(blackSquare.join(square).horizontalRepeat(4))
