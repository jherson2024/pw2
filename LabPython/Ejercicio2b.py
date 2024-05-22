from chessPictures import *
from interpreter import draw

knightBlack=knight.negative()
draw(knight.join(knightBlack).under(knightBlack.verticalMirror().join(knight.verticalMirror())))