# Midterm Project - Team 10
# 11 November 2018
# This program is an instagram filter that takes an image, resizes it if 
# necessary, and applies a red, white, and blue hue, as well as a beach scene

# This function has the user select an image and returns it
def getPic():
  return makePicture(pickAFile())

# This function takes the first vertical third of an image and makes applies
# a red hue
def redThird(pic):
  width = getWidth(pic)
  height = getHeight(pic)
  for x in range(0, width/3):
    for y in range(0, height):
      p = getPixel(pic,x,y)
      r = getRed(p)
      setRed(p, r*3)
  return pic

# This function takes the second vertical third of an image and makes applies
# a white hue
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

# This function takes the last vertical third of an image and makes applies
# a blue hue
def blueThird(pic):
  width = getWidth(pic)
  height = getHeight(pic)
  for x in range((2 * width)/3, width):
    for y in range(0, height):
      p = getPixel(pic,x,y)
      b = getBlue(p)
      setBlue(p, b*3)
  return pic

# This function converts an image to black and white
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

# This function is the main function for the second filter
def drawBeach(pic, width, height):
  pic = addSun(pic, 500, 500)
  pic = drawSand(pic, width, height)
  pic = drawSign(pic, 500, 500)
  pic = drawSeagull(pic, 200, 200)
  pic = drawSeagull(pic, 200, 200)
  pic = drawSeagull(pic, 200, 200)
  return pic

# This function adds the sun to the specified location
def addSun(pic, x, y):
  return pic

# This function draws sand on the bottom of the image
def drawSand(pic, width, height):
  sand = makeColor(229, 199, 160)

  # apply sand base
  sandLayer(pic, height - 25, height, sand, width, height)

  # apply sprinkling of sand
  sandLayer(pic, height - 12, height - 25, sand, width, height, 1, 3)
  sandLayer(pic, height - 26, height - 28, sand, width, height, 2, 2)
  sandLayer(pic, height - 22, height - 25, sand, width, height, 3, 4)

  # apply grit
  sandLayer(pic, height - 2, height, black, width, height, 0, 20)
  sandLayer(pic, height - 5, height - 3, black, width, height, 2, 15)
  sandLayer(pic, height - 18, height - 16, black, width, height, 4, 10)

  # adds grit to the sand
  applyGrit(pic, width, height)
  return pic

# applies a layer of sand with the given parameters
def sandLayer(pic, minHeight, maxHeight, color=black, width=500, height=500, \
  xOffset=0, xStep=1):
  for x in range(xOffset, width, xStep):
    for y in range(minHeight, maxHeight):
      setColor(getPixel(pic, x, y), color)
  return pic

# distributes grit onto the sand
def applyGrit(pic, width, height):
  for x in range(0, width):
    for y in range(height - 23, height):
      if x % 8 == 0 and y % 4 == 0:
        setColor(getPixel(pic, x, y), black)
  return pic

# Draws a seagull at the given x, y coordinate
def drawSeagull(pic, x, y):
  return pic

# Draws the sign on for the beach scene
def drawSign(pic, x, y):
  return pic

# Retrieves the dimensions of the image
def getDimensions(pic):
  width = getWidth(pic)
  height = getHeight(pic)
  return width, height

# This is the main function for the midterm project
def main():
  pic = getPic()
  picSize = testPicSize(pic)
  width, height = getDimensions(pic)

  # Tests the image to see if it is big enough
  if not picSize:
    return None

  # Resize the image
  pic = resizePic(pic)

  # Apply first filter - make image red, white and blue
  pic = redWhiteBlue(pic)

  # Apply second filter - add beach scene
  pic = drawBeach(pic, width, height)
  explore(pic)

  return pic