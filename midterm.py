#Practice for Midterm

def getPic():
  return makePicture(pickAFile())

def redThird(pic):
  width = getWidth(pic)
  height = getHeight(pic)
  for x in range(0, width/3):
    for y in range(0, height):
      p = getPixel(pic,x,y)
      r = getRed(p)
      setRed(p, r*3)
  return pic

def whiteThird(pic):
  width = getWidth(pic)
  height = getHeight(pic)
  for x in range((width + 1)/3, (2 * width)/3):
    for y in range(0, height):
      p = getPixel(pic,x,y)
      r = getRed(p)
      g = getGreen(p)
      b = getBlue(p)
      newColor = makeColor(r + 50, g + 50, b + 50)
      setColor(p, newColor)
  return pic

def blueThird(pic):
  width = getWidth(pic)
  height = getHeight(pic)
  for x in range((2 * width)/3, width):
    for y in range(0, height):
      p = getPixel(pic,x,y)
      b = getBlue(p)
      setBlue(p, b*3)
  return pic


def redWhiteBlue(pic):
  
  #Resize Function needed here
  
  
  #Red filter, First Third
  redThird(pic)
  #White filter, Second Third
  whiteThird(pic)
  #Blue filter, Last Third
  blueThird(pic)
  repaint(pic)
  return pic
