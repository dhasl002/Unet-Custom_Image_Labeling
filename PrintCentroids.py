import numpy as np
import cv2

height = 208
width = 368

#loop over predictions, check color and calculate centroid statistics
for i in range(1, 35):
	predictionsImg = cv2.imread('Predictions/Epoch_12Image' + str(i) + '.png', 1)
	predictedLabels = np.asarray( predictionsImg, dtype="float64")

	carCenterHeight = 0
	carCenterWidth = 0
	carNum = 0
	bananaCenterHeight = 0
	bananaCenterWidth = 0
	bananaNum = 0
	horseCenterHeight = 0
	horseCenterWidth = 0
	horseNum = 0
	for j in range(0, height):
		for k in range(0, width):
			if predictedLabels[j][k][0] == 255 and predictedLabels[j][k][1] == 0 and predictedLabels[j][k][2] == 0:
				bananaNum += 1
				bananaCenterHeight += j 
				bananaCenterWidth += k
			elif predictedLabels[j][k][0] == 0 and predictedLabels[j][k][1] == 255 and predictedLabels[j][k][2] == 0:
				carNum += 1
				carCenterHeight += j
				carCenterWidth += k
			elif predictedLabels[j][k][0] == 0 and predictedLabels[j][k][1] == 0 and predictedLabels[j][k][2] == 255:
				horseNum += 1
				horseCenterHeight += j
				horseCenterWidth += k
			elif predictedLabels[j][k][0] == 255 and predictedLabels[j][k][1] == 255 and predictedLabels[j][k][2] == 0:
				bananaNum += 1
				bananaCenterHeight += j
				bananaCenterWidth += k
				carNum += 1
				carCenterHeight += j 
				carCenterWidth += k
			elif predictedLabels[j][k][0] == 255 and predictedLabels[j][k][1] == 0 and predictedLabels[j][k][2] == 255:
				bananaNum += 1
				bananaCenterHeight += j
				bananaCenterWidth += k
				horseNum += 1
				horseCenterHeight += j 
				horseCenterWidth += k
			elif predictedLabels[j][k][0] == 0 and predictedLabels[j][k][1] == 255 and predictedLabels[j][k][2] == 255:
				carNum += 1
				carCenterHeight += j 
				carCenterWidth += k
				horseNum += 1
				horseCenterHeight += j
				horseCenterWidth += k
	print('image_' + str(i))
	if carNum > 600:
		print('Car Centroid: ' + str(carCenterWidth/carNum) + ' , ' + str(carCenterHeight/carNum))
	if bananaNum > 600:
		print('Banana Centroid: ' + str(bananaCenterWidth/bananaNum) + ' , ' + str(bananaCenterHeight/bananaNum))
	if horseNum > 600:
		print('Horse Centroid: ' + str(horseCenterWidth/horseNum) + ' , ' + str(horseCenterHeight/horseNum))
	print('\n\n')