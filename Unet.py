import tensorflow as tf
import numpy as np
from model import model
import cv2
import random

batch_Size = 32
width = 368
height = 208

def train(batch_Size, width, height):
	a = np.zeros((batch_Size, height, width, 3),dtype = "float64")
	b = np.zeros((batch_Size, height*width, 7),dtype = "float64")
	for it in range(0, 6200):
		randImage = random.randint(0, 100)
		
		rawImage = cv2.imread('trainingData/trainingImages/' + str(randImage) +'.png', 1)
		rawImageArray = np.asarray( rawImage, dtype="float64" )
		groundTruth = cv2.imread('trainingData/groundTruth/' + str(randImage) +'.png', 1)
		groundTruthArray = np.asarray( groundTruth, dtype="float64" )

		oneHot = oneHotConverter(groundTruthArray, width, height)

		a[int(it)%batch_Size] = rawImageArray
		b[int(it)%batch_Size] = oneHot

		if(int(it)%batch_Size == (batch_Size)-1):
			runTrainingBatch(a, b)
			a = np.zeros((batch_Size, height, width, 3),dtype = "float64")
			b = np.zeros((batch_Size, height*width, 7),dtype = "float64")

def oneHotConverter(groundTruthArray, width, height):
	oneHot = np.zeros((height*width, 7),dtype = "float64")
	for i in range(0, height):
		for j in range(0, width):
			if groundTruthArray[i][j][0] == 1 and groundTruthArray[i][j][1] == 0 and groundTruthArray[i][j][2] == 0:
				oneHot[i*width+j][0] = 1
			elif groundTruthArray[i][j][0] == 0 and groundTruthArray[i][j][1] == 1 and groundTruthArray[i][j][2] == 0:
				oneHot[i*width+j][1] = 1
			elif groundTruthArray[i][j][0] == 0 and groundTruthArray[i][j][1] == 0 and groundTruthArray[i][j][2] == 1:
				oneHot[i*width+j][2] = 1
			elif groundTruthArray[i][j][0] == 1 and groundTruthArray[i][j][1] == 1 and groundTruthArray[i][j][2] == 0:
				oneHot[i*width+j][3] = 1
			elif groundTruthArray[i][j][0] == 1 and groundTruthArray[i][j][1] == 0 and groundTruthArray[i][j][2] == 1:
				oneHot[i*width+j][4] = 1
			elif groundTruthArray[i][j][0] == 0 and groundTruthArray[i][j][1] == 1 and groundTruthArray[i][j][2] == 1:
				oneHot[i*width+j][5] = 1
			elif groundTruthArray[i][j][0] == 1 and groundTruthArray[i][j][1] == 1 and groundTruthArray[i][j][2] == 1:
				oneHot[i*width+j][6] = 1
	return oneHot

def runTrainingBatch(a, b):
	keep_prob = tf.placeholder(tf.float32)
	CurCross = cross_entropy.eval(feed_dict={x_image: a, y_: b})
	train_accuracy = accuracy.eval(feed_dict={x_image: a, y_: b, keep_prob: .5})
	train_step.run(feed_dict={x_image: a, y_: b, keep_prob: .5})
	print('training accuracy %g' % (train_accuracy))
	print('Loss %g' % (CurCross))

x_image = tf.placeholder(tf.float32, shape=[batch_Size, height, width, 3])
y_ = tf.placeholder(tf.float32, shape=[None, None, 7])

modelResult = model(x_image) #sets modelResults to the final result of the model 

cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=modelResult, labels=y_))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(modelResult, 1), tf.argmax(tf.reshape(y_, [-1, 7]), 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

#run
with tf.Session() as sess:
	sess.run(tf.global_variables_initializer())
	for curEpoch in range(1, 500):
		print('Epoch: ' + str(curEpoch) + '\n')
		train(batch_Size, width, height)