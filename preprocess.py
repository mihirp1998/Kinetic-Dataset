import cv2
import os 
import pickle
from joblib import delayed
from joblib import Parallel
# a = os.listdir("test/")
import glob
a = glob.glob("out/*/*")
# a = glob.glob("test/*")
n = 0
global n
print(len(a))
num = 0 
f = open("trainHighRes.txt","wb")
# p = Parallel(24)
# print(len(set(a[:][:-14])))

def calDim(i):
	global n
	vcap = cv2.VideoCapture(i) # 0=camera
	width = vcap.get(cv2.CAP_PROP_FRAME_WIDTH)   
	height = vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)   
	if width>710 and height>710:
		i+="\n"
		f.write(i.encode("utf-8"))
	n+=1
	print(n)


status_lst = Parallel(n_jobs=24,backend="threading")(delayed(calDim)(i) for i in a)

# for i in a[:100]:
# 	vcap = cv2.VideoCapture("test/"+i) # 0=camera
# 	width = vcap.get(cv2.CAP_PROP_FRAME_WIDTH)   
# 	height = vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)
# 	print(width,height)
# 	if width>710 and height>710:
# 		num+=1
# 		print("index",num)
# 		n.append(i[:-18])

	# return (height,width)
        