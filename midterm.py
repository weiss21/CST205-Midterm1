# Midterm Project - Team 10
# 11 November 2018
# This program is an instagram filter that takes an image, resizes it if 
# necessary, and applies a red, white, and blue hue, as well as a beach scene

#global variables
offset = 400

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
  minimum_size = 801
  height = getHeight(pic)
  width = getWidth(pic)
  if width <= minimum_size:
    return False
  elif height < minimum_size:
    return False
  return True

# This function resizes the picture
def resizePic(pic, width, height):
  # declare variables
  midX = width / 2
  midY = height / 2
  indexX = 0
  indexY = 0
  canvas = makeEmptyPicture(offset * 2, offset * 2, black)
  
  # resize image
  for x in range(midX - offset, midX + offset):
    for y in range(midY - offset, midY + offset):
      pixel = getPixel(pic, x, y)
      color = getColor(pixel)
      p = getPixel(canvas, indexX, indexY)
      setColor(p, color)
      indexY += 1
    indexY = 0
    indexX += 1
  return canvas

# This function is the main function for the second filter
def drawBeach(pic, width, height):
  pic = addSun(pic, 550, 25)
  pic = drawSand(pic)
  pic = drawSign(pic, 500, 500)
  pic = drawSeagull(pic, 80, 100)
  pic = drawSeagull(pic, 280, 150)
  pic = drawSeagull(pic, 90, 200)
  return pic

# This function adds the sun to the specified location
def addSun(pic, x, y):
  addOvalFilled(pic, x, y, 200, 200, orange)
  return pic

# This function draws sand on the bottom of the image
def drawSand(pic):
  width = getWidth(pic)
  height = getHeight(pic)
  # make colors
  sand = makeColor(229, 199, 160)
  sprinkles = makeColor(219, 158, 107)

  # apply sand base
  sandLayer(pic, height - 100, height, sand, width, height)

  # apply sprinkling of sand
  sandLayer(pic, height - 90, height, sprinkles, width, height, 8, 11)

  # adds grit to the sand
  applyGrit(pic, width, height, 95)
  return pic

# applies a layer of sand with the given parameters
def sandLayer(pic, minHeight, maxHeight, color, width, height, xStep=1, yStep=1):
  for x in range(0, width, xStep):
    for y in range(minHeight, maxHeight, yStep):
      setColor(getPixel(pic, x, y), color)
  return pic

# distributes grit onto the sand
def applyGrit(pic, width, height, deltaY):
  for x in range(2, width):
    for y in range(height - deltaY, height):
      if x % 60 == 0 and y % 14 == 0:
        setColor(getPixel(pic, x, y), black)
  return pic

# Draws a seagull at the given x, y coordinate
def drawSeagull(pic, x, y):
  addArc(pic, x, y, 100, 200, 60, 90, black)
  addArc(pic, x + 50, y, 100, 200, 30, 90, black)

  return pic

# Draws the sign on for the beach scene
def drawSign(pic, x, y):
  brown = makeColor(165,42,42)
  addRectFilled(pic, x, y, 250, 80, brown)
  addText(pic, x + 30, y + 45)  
  #Post for sign below
  addRectFilled(pic, x + 125 , y + 65, 25, 175, brown)
  return pic

# Adds text to the sign
def addText(pic, x, y):
  message = 'Welcome to CSUMB!!!'
  font = makeStyle(sansSerif, bold, 18)
  addTextWithStyle(pic, x, y, message, font, white)

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
    print 'Supplied image too small. Needs to be 800x800'
    return None

  # Resize the image
  pic = resizePic(pic, width, height)

  # Apply first filter - make image red, white and blue
  pic = redWhiteBlue(pic)

  # Apply second filter - add beach scene
  pic = drawBeach(pic, width, height)

  return pic