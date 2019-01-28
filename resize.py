import cv2
import os 
import sys
import pickle
from joblib import delayed
from joblib import Parallel
# l = open("trainHighRes.txt","rb").read().decode().split("\n")
import glob
import pickle
# pickle.load(open())
# imgs = glob.glob("outTrainImgs/*")
imgs = pickle.load(open("random500.p","rb"))
print(len(imgs))

# l = pickle.load(open("highres.p","rb"))
# a = os.listdir("test/")
global n
n = 0
# print(len(a))
num = 0 
# p = Parallel(24)
# print(len(set(a[:][:-14])))

def vid2img(i):
	global n
	image = cv2.imread(i)
	rz_image = cv2.resize(image, (352,288))
	# cap = cv2.VideoCapture(i) # 0=camera
	name = i.split("/")[1][:-4]
	cv2.imwrite(i.replace("outValidImgs","random500"), rz_image)
	if image.shape is not (720, 1280, 3):
		print(image.shape,name)
	n+=1

	if n%10000:
		print(n)

# print(l[:3])
status_lst = Parallel(n_jobs=32,backend="threading")(delayed(vid2img)(i) for i in imgs)
