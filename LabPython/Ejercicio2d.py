from chessPictures import *
from interpreter import draw

blackSquare=square.negative()
draw(square.join(blackSquare).horizontalRepeat(4))
