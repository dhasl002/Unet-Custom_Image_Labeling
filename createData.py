import numpy as np
import cv2
import random

width = 368
height = 208
offset = 40

def placeImageRandomly(imageToPlace, offset, groundTruth, finalImage):
    randX = random.randint(offset-imageToPlace.shape[0],height-offset)
    randY = random.randint(offset-imageToPlace.shape[1],width-offset)
    for i in range(0, imageToPlace.shape[0]):
        for j in range(0, imageToPlace.shape[1]):
            if(i+randX < height and j+randY < width and i+randX > 0 and j+randY > 0):
                if float(imageToPlace[i][j][0]/256) < .99 or float(imageToPlace[i][j][0]/256) < .99 or float(imageToPlace[i][j][0]/256) < .99:
                    finalImage[i+randX][j+randY][0] = float(imageToPlace[i][j][0]/256)
                    finalImage[i+randX][j+randY][1] = float(imageToPlace[i][j][1]/256)
                    finalImage[i+randX][j+randY][2] = float(imageToPlace[i][j][2]/256)
                    if (float(imageToPlace[i][j][0]/256) < .99 or float(imageToPlace[i][j][0]/256) <.99 or float(imageToPlace[i][j][0]/256) <.99):
                        groundTruth[i+randX][j+randY][0] = 1
                        groundTruth[i+randX][j+randY][1] = 0
                        groundTruth[i+randX][j+randY][2] = 0

for imageNum in range(0,50000):
    #load images
    bananasImg = cv2.imread('croppedImages/bananas/1.png', 1)
    bananasArray = np.asarray( bananasImg, dtype="float64" )
    horseImg = cv2.imread('croppedImages/horse/1.png', 1)
    horseArray = np.asarray( horseImg, dtype="float64" )
    carImg = cv2.imread('croppedImages/car/' + str(random.randint(1,4)) + '.png', 1)
    carArray = np.asarray( carImg, dtype="float64" )

    #Create white image of size heightxwidth
    img = np.zeros([height,width,3])
    groundTruth = np.zeros([height,width,3])
    for i in range(0,height):
        for j in range(0, width):
            img[i][j][0] = 1
            img[i][j][1] = 1
            img[i][j][2] = 1
            groundTruth[i][j][0] = 0
            groundTruth[i][j][1] = 0
            groundTruth[i][j][2] = 0

    #give 50% chance of having object in image, ensure that image is not empty
    executeLoop = True
    while executeLoop:
        randBanana = random.randint(0,1)
        randHorse = random.randint(0,1)
        randCar = random.randint(0,1)
        if randBanana != 0 or randHorse != 0 or randCar != 0:
             executeLoop = False

    if randBanana == 1:
        randX = random.randint(offset-bananasArray.shape[0],height-offset)
        randY = random.randint(offset-bananasArray.shape[1],width-offset)
        for i in range(0, bananasArray.shape[0]):
            for j in range(0, bananasArray.shape[1]):
                if(i+randX < height and j+randY < width and i+randX > 0 and j+randY > 0):
                    if float(bananasArray[i][j][0]/256) < .99 or float(bananasArray[i][j][0]/256) < .99 or float(bananasArray[i][j][0]/256) < .99:
                        img[i+randX][j+randY][0] = float(bananasArray[i][j][0]/256)
                        img[i+randX][j+randY][1] = float(bananasArray[i][j][1]/256)
                        img[i+randX][j+randY][2] = float(bananasArray[i][j][2]/256)
                        if (float(bananasArray[i][j][0]/256) < .99 or float(bananasArray[i][j][0]/256) <.99 or float(bananasArray[i][j][0]/256) <.99):
                            groundTruth[i+randX][j+randY][0] += 1
                            groundTruth[i+randX][j+randY][1] += 0
                            groundTruth[i+randX][j+randY][2] += 0

    if randCar == 1:
        randX = random.randint(offset-carArray.shape[0],height-offset)
        randY = random.randint(offset-carArray.shape[1],width-offset)
        for i in range(0, carArray.shape[0]):
            for j in range(0, carArray.shape[1]):
                if(i+randX < height and j+randY < width and i+randX > 0 and j+randY > 0):
                    if float(carArray[i][j][0]/256) < .99 or float(carArray[i][j][0]/256) < .99 or float(carArray[i][j][0]/256) < .99:
                        img[i+randX][j+randY][0] = float(carArray[i][j][0]/256)
                        img[i+randX][j+randY][1] = float(carArray[i][j][1]/256)
                        img[i+randX][j+randY][2] = float(carArray[i][j][2]/256)
                        if (float(carArray[i][j][0]/256) < .99 or float(carArray[i][j][0]/256) <.99 or float(carArray[i][j][0]/256) <.99):
                            groundTruth[i+randX][j+randY][0] += 0
                            groundTruth[i+randX][j+randY][1] += 1
                            groundTruth[i+randX][j+randY][2] += 0

    if randHorse == 1:
        randX = random.randint(offset-horseArray.shape[0],height-offset)
        randY = random.randint(offset-horseArray.shape[1],width-offset)
        for i in range(0, horseArray.shape[0]):
            for j in range(0, horseArray.shape[1]):
                if(i+randX < height and j+randY < width and i+randX > 0 and j+randY > 0):
                    if float(horseArray[i][j][0]/256) < .99 or float(horseArray[i][j][0]/256) < .99 or float(horseArray[i][j][0]/256) < .99:
                        img[i+randX][j+randY][0] = float(horseArray[i][j][0]/256)
                        img[i+randX][j+randY][1] = float(horseArray[i][j][1]/256)
                        img[i+randX][j+randY][2] = float(horseArray[i][j][2]/256)
                        if (float(horseArray[i][j][0]/256) < .99 or float(horseArray[i][j][0]/256) <.99 or float(horseArray[i][j][0]/256) <.99):
                            groundTruth[i+randX][j+randY][0] += 0
                            groundTruth[i+randX][j+randY][1] += 0
                            groundTruth[i+randX][j+randY][2] += 1

    for i in range(0,height):
        for j in range(0, width):
            img[i][j][0] = img[i][j][0]*256
            img[i][j][1] = img[i][j][1]*256
            img[i][j][2] = img[i][j][2]*256
            if(groundTruth[i][j][0] == 0 and groundTruth[i][j][1] == 0 and groundTruth[i][j][2] == 0):
                groundTruth[i][j][0] = 1
                groundTruth[i][j][1] = 1
                groundTruth[i][j][2] = 1
            groundTruth[i][j][0] = groundTruth[i][j][0]*256
            groundTruth[i][j][1] = groundTruth[i][j][1]*256
            groundTruth[i][j][2] = groundTruth[i][j][2]*256

    cv2.imwrite('trainingData/trainingImages/' + str(imageNum) + '.png', img)
    cv2.imwrite('trainingData/groundTruth/' + str(imageNum) + '.png', groundTruth)





