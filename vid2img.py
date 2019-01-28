import cv2
import os 
import sys
import pickle
from joblib import delayed
from joblib import Parallel
import random
import os
# l = open("trainHighRes.txt","rb").read().decode().split("\n")
l = pickle.load(open("validVid.p","rb"))
# random.shuffle(l)
l = l[:10]
print(len(l))

# l = ["test/deuKjxPCC68_000006_000016.mp4"]
# l = pickle.load(open("highres.p","rb"))
# a = os.listdir("test/")
global n
n = 0
# print(len(a))
num = 0 
# p = Parallel(24)
# print(len(set(a[:][:-14])))
directory = sys.argv[1]
if not os.path.exists(directory):
    os.makedirs(directory)

def vid2img(i):
	global n
	cap = cv2.VideoCapture(i) # 0=camera
	name = i.split("/")[2][:-4]
	# print(cap)
	# width = vcap.get(cv2.CAP_PROP_FRAME_WIDTH)   
	# height = vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)   
	num = 0
	n+=1
	while(True):
		ret, frame = cap.read()
		if ret:
			# cv2.imshow('capturing...', cv2.resize(frame, (0,0), fx=0.3, fy=0.3))
			if(num>=11):
				break
			elif(num>=0 and num<11):	

				sav_path =  directory +'/frame{}_{:04d}.jpg'.format(name,num)
				frame = cv2.resize(frame, (352,288))
				cv2.imwrite(sav_path, frame)
				# print("saved at "+ sav_path)
			num=num+1
		else:
			break
	print(n)

# print(l[:3])
status_lst = Parallel(n_jobs=32)(delayed(vid2img)(i) for i in l)

# for i in a:
# 	print(width,height)
# 	if width>710 and height>710:
# 		num+=1
# 		print("index",num)
# 		n.append(i[:-18])
# print(len(n))	
# pickle.dump(n,open("highrescheck.p","wb"))
	# return (height,width)