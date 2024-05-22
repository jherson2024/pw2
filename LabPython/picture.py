from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    return Picture([row[::-1] for row in self.img])

  def horizontalMirror(self):
    return Picture(self.img[::-1])

  def negative(self):
    return Picture([''.join(self.invColor(char) for char in row) for row in self.img])

  def join(self, p):
    return Picture([self.img[i] + p.img[i] for i in range(len(self.img))])

  def up(self, p):
    return Picture(p.img + self.img)

  def under(self, p):
    return Picture(self.img + p.img)
  
  def horizontalRepeat(self, n):
    return Picture([row * n for row in self.img])

  def verticalRepeat(self, n):
    return Picture(self.img * n)

  def rotate(self):
    rotated = [list(row) for row in zip(*self.img)][::-1]
    return Picture(rotated)