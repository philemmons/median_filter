'''
Title: Median Filter
Abstract: "Write a median filter program using Python and Pillow to create a
new image from the 9 images."
Phillip T.Emmons
CST 205 Monday/Wednesday 10-12pm
9-9-2016

The help sheet with the multiple variable assignment was very useful"
'''
import time
from PIL import Image
from statistics import median

startTime =time.clock()

#instance variables, all list
redPixList = []
greenPixList = []
bluePixList = []
inputFile = []

#This will get the image for the size ands the width.
initialPhoto =  Image.open( "1.png")
width, height = initialPhoto.size
#Creates a solid color image for the pixels to be added to during loops below.
canvasImage = Image.new("RGB", (width, height), color= 255)
canvasImage.save('newImage.png') 
print("Canvas ready.")


#Adds all 10 images to a list from the folder location.
for numImage in range( 1,10 ):
    inputFile.append( Image.open( str( numImage ) + '.png' ) )

print("Images loaded.")

#This will go through all 9 images, adding the pixel color binary number  to separate lists.

# The loops will iterate row by column.
for xWidth in range( 0, width ):
    for yHeight in range( 0, height):
        for flipBook in range( 0, len(inputFile) ):
            redPix, greenPix, bluePix =  inputFile[ flipBook ].getpixel( (  xWidth, yHeight ) )  
            redPixList.append( redPix )
            greenPixList.append( greenPix )
            bluePixList.append( bluePix )
#Each list will be sorted and the median value selected, and it will be added to its color result variable.
        resultRed = median( sorted( redPixList ) ) 
        resultGreen = median( sorted( greenPixList ) )
        resultBlue = median( sorted( bluePixList ) )

#Writes new pixel to image location.
        canvasImage.putpixel( ( xWidth, yHeight ), ( resultRed, resultGreen, resultBlue ) )
#Reset the color list by splicing  for the next pixel 
        redPixList[:] = []
        greenPixList[:] = []
        bluePixList[:] = []
        
#This will be the output image.       
canvasImage.save('newImage.png')
print("All finished")
print("time: "+ str(time.clock()-startTime))