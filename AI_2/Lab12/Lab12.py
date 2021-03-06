##Jake Shankman
##AI 2 Period 2
### Lab11 Edge Detection
## 2/2/12

from math import atan2
from math import degrees
from random import random

angles = [0, 45, 90, 135, 180, 225, 270, 315]
printlist = []
#INput kills
def newIndex(x, y, z, theta):
  
  while theta<0:
    theta+=360
  while theta>=360:
    theta-=360
  
  if theta == angles[0]:
    return (y * z + x + 1)
  elif theta == angles[1]:
    return ((y-1)*z + x + 1)
  elif theta == angles[2]:
    return ((y - 1)*z + x)
  elif theta == angles[3]:
    return ((y-1)*z + x - 1)
  elif theta == angles[4]:
    return (y*z + x - 1)
  elif theta == angles[5]:
    return ((y + 1)*z + x - 1)
  elif theta == angles[6]:
    return ((y+ 1)*z + x)
  elif theta == angles[7]:
    return ((y + 1)*z + x + 1)
    
    
#floodfill calls itself, keep if above low threshold
def floodfill(image, index, x, y, z, h, printlist):
  if x ==0 or x == z - 1 or y == 0 or y == h - 1:
    return printlist
  else:
    GX = Gx(image, index, x, y, z)
    GY = Gy(image, index, x, y, z)
    G = abs(GX) + abs(GY)
    if G > 125:
      printlist[index] = 0
      theta = degrees(atan2(GY, GX))
      theta = theta/45
      theta = round(theta + 0.5) * 45
      
      indexUp = newIndex(x, y, w, theta)
      GXI = Gx(s, indexUp, x, y, w)
      GYI = Gy(s, indexUp, x, y, w)
      GI = abs(GXI) + abs(GYI) 
      
      indexDown = newIndex(x, y, w, theta + 180)
      GXD = Gx(s, indexDown, x, y, w)
      GYD = Gy(s, indexDown, x, y, w)
      GD = abs(GXD) + abs(GYD)
      
      if G > GI:
	printlist = floodfill(s, newIndex(x, y, w, theta + 90), x, y, w, h, printlist)
	if G > GD:
	  printlist = floodfill(s, newIndex(x, y, w, theta - 90), x, y, w, h, printlist)
    else:
      printlist[index] = 255
    return printlist

def smooth(image,index, x , y, z):
  ##Make Gaussian Smoothing (multiply value by values below)
  ##1  2  1
  ##2  4  2
  ##1  2  1
  ## Average and divide by 16
  indexl = (y*z + x - 1)
  indexr = (y*z + x + 1)
  indexu = ((y - 1)*z + x)
  indexd = ((y+ 1)*z + x)
  
  indexlu = ((y-1)*z + x - 1)
  indexru = ((y-1)*z + x + 1)
  indexld = ((y + 1)*z + x - 1)
  indexrd = ((y + 1)*z + x + 1)
  
  point = int(image[index])
  pvalue = point * 4
  
  pvalue = pvalue + (int(image[indexl]) * 2)
  pvalue = pvalue + (int(image[indexr]) * 2)
  pvalue = pvalue + (int(image[indexu]) * 2)
  pvalue = pvalue + (int(image[indexd]) * 2)
  
  pvalue = pvalue + int(image[indexlu])
  pvalue = pvalue + int(image[indexld])
  pvalue = pvalue + int(image[indexru])
  pvalue = pvalue + int(image[indexrd])
  
  pvalue = pvalue / 16
  print pvalue

def Gx(image, index, x, y, z):
  indexl = (y*z + x - 1)
  indexr = (y*z + x + 1)
  
  indexlu = ((y-1)*z + x - 1)
  indexru = ((y-1)*z + x + 1)
  indexld = ((y + 1)*z + x - 1)
  indexrd = ((y + 1)*z + x + 1)
  
  pvalue = 0
  
  pvalue = pvalue + (int(image[indexl]) * -2)
  pvalue = pvalue + (int(image[indexr]) * 2)
  
  pvalue = pvalue + (int(image[indexlu]) * - 1)
  pvalue = pvalue + (int(image[indexld]) *-1)
  pvalue = pvalue + int(image[indexru]) 
  pvalue = pvalue + int(image[indexrd])
 
  return pvalue
  
  
def Gy(image, index, x, y, z):
  indexu = ((y - 1)*z + x)
  indexd = ((y+ 1)*z + x)
  
  indexlu = ((y-1)*z + x - 1)
  indexru = ((y-1)*z + x + 1)
  indexld = ((y + 1)*z + x - 1)
  indexrd = ((y + 1)*z + x + 1)
  
  pvalue = 0
  

  pvalue = pvalue + (int(image[indexu]) * 2)
  pvalue = pvalue + (int(image[indexd]) * -2)
  
  pvalue = pvalue + int(image[indexlu])
  pvalue = pvalue + (int(image[indexld]) * - 1)
  pvalue = pvalue + int(image[indexru])
  pvalue = pvalue + (int(image[indexrd]) * - 1)
  
  return pvalue
  
task = raw_input()





if task == 'Grayscale':
  s = open('circle.ppm','r').read().split()
  print 'P2'
  print s[1]
  print s[2]
  print '255'
  i = 4
  while i < len(s):
    red = int(s[i])
    green = int(s[i + 1])
    blue = int(s[i + 2])
    
    gray = 0.3*red + .59*green + .11*blue
    gray = int(gray + 0.5)
    print gray
    
    i = i + 3

elif task == 'Smooth':
  s = open('circle.pgm', 'r').read().split()
  print 'P2'
  print s[1]
  print s[2]
  print '255'
  w = int(s[1])
  h = int(s[2])
  s = s[4:]
  j = 0
  while j < h:
    i = 0
    while i < w:
      x = i
      y = j
      index = int((y*w) + x)
      if x ==0 or x == w - 1 or y == 0 or y == h - 1:
	print s[index]
      else:
	smooth(s, index, x, y, w)
      i = i + 1
    j = j + 1

elif task == 'Edge':
  s = open('circle2.pgm', 'r').read().split()
  print 'P2'
  print s[1]
  print s[2]
  print '255'
  w = int(s[1])
  h = int(s[2])
  s = s[4:]
  printlist = s[:]
  for item in printlist:
    item = -100
  j = 0
  while j < h:
    i = 0
    while i < w:
      x = i
      y = j
      index = int((y*w) + x)
      if x ==0 or x == w - 1 or y == 0 or y == h - 1:
	 printlist[index] = 255
      else:
	GX = Gx(s, index, x, y, w)
	GY = Gy(s, index, x, y, w)
	G = abs(GX) + abs(GY)
	if G > 175:
	  printlist[index] = 0
	  #Figure out the recursion, LOW for G = 25, HIGH = 75
	  #135  90  45
	  #180  -   0
	  #225 270 315
	
	  theta = degrees(atan2(GY, GX))
	  theta = theta/45
	  theta = round(theta + 0.5) * 45
	  #create top and bottom in form of indexes, convert, then calculate G, recurr
	  #Recur +- 90, floodfill
	  indexUp = newIndex(x, y, w, theta)
	  GXI = Gx(s, indexUp, x, y, w)
	  GYI = Gy(s, indexUp, x, y, w)
	  GI = abs(GXI) + abs(GYI)
	  
	  indexDown = newIndex(x, y, w, theta + 180)
	  GXD = Gx(s, indexDown, x, y, w)
	  GYD = Gy(s, indexDown, x, y, w)
	  GD = abs(GXD) + abs(GYD)
	  
	  if G > GI:
	    printlist = floodfill(s, newIndex(x, y, w, theta + 90), x, y, w, h, printlist)
	    if G > GD:
	      printlist = floodfill(s, newIndex(x, y, w, theta - 90), x, y, w, h, printlist)
	else:
	  printlist[index] = 255
	
      i = i + 1
    j = j + 1
   
    
  for item in printlist:
    if item < 0:
      item = 255
    print item
