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

#BlackandWhite
def betterBnW(pic):
  pixels = getPixels(pic)
  
  for p in pixels:
    b = getBlue(p)
    g = getGreen(p)
    r = getRed(p)
    avg = ((b*0.114) + (g*0.587) + (r*0.299))  
    setRed(p, avg)
    setGreen(p, avg)
    setBlue(p, avg)
  return pic

# This function turns an image red white and blue
def redWhiteBlue(pic):
  
  betterBnW(pic)
  #Red filter, First Third
  redThird(pic)
  #White filter, Second Third
  whiteThird(pic)
  #Blue filter, Last Third
  blueThird(pic)
  repaint(pic)
  return pic

# This function determines whether the image is big enough for the filter.
def testPicSize(pic):
  minimum_size = 500
  height = getHeight(pic)
  width = getWidth(pic)
  if width <= minimum_size:
    return False
  elif height < minimum_size:
    return False
  return True

# This function resizes the picture
def resizePic(pic):
  return pic

def drawBeach(pic):
  pic = addSun(pic, 500, 500)
  return pic

# This function adds the sun to the specified location
def addSun(pic, x, y):
  return pic

# This function draws sand on the bottom of the image
def drawSand(pic, height, width):
  return pic

def drawSign(pic, x, y):
  return pic

# This is the main function for the midterm project
def main():
  pic = getPic()
  picSize = testPicSize(pic)

  # Tests the image to see if it is big enough
  if not picSize:
    return None

  # Resize the image
  pic = resizePic(pic)

  # Apply first filter - make image red, white and blue
  pic = redWhiteBlue(pic)

  return pic