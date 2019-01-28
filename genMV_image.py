import cv2
import os 
import sys
import pickle
import glob
from joblib import delayed
from joblib import Parallel
import numpy as np
# l = open("trainHighRes.txt","rb").read().decode().split("\n")
# l = pickle.load(open("validVid.p","rb"))
# print(len(l))
import pickle 
import sys
import glob
files = pickle.load(open("motiongen_tempValid_till260_10Vid.p","rb"))
# folder_name = "outTrain100/*"
# files = glob.glob(folder_name)
# fl = len(folder_name) -1
# l = ["test/deuKjxPCC68_000006_000016.mp4"]
# l = pickle.load(open("highres.p","rb"))
# a = os.listdir("test/")
global n
bound = 15
norm_width = 500
n = 0
# print(len(a))
# all_list = []
num = 0 
# p = Parallel(24)
# print(len(set(a[:][:-14])))
# index = 30 +fl

def cvReadGrayImg(img_path):
	return cv2.cvtColor(cv2.imread(img_path), cv2.COLOR_BGR2GRAY)

def saveOptFlowToImage(flow, basename):
	cv2.imwrite(basename+'_x.JPEG', flow[...,0])
	cv2.imwrite(basename+'_y.JPEG', flow[...,1])  

def saveImage(img1,img2, basename):
	cv2.imwrite(basename+'_first.JPEG', img1)
	cv2.imwrite(basename+'_curr.JPEG', img2)  
def vid2img(i):
	global n,all_list
	first_img = cvReadGrayImg(i[1])
	curr_img = cvReadGrayImg(i[0])
	h, w = first_img.shape
	fxy = norm_width / w
	# normalize image size
	flow = cv2.calcOpticalFlowFarneback(cv2.resize(first_img, None, fx=fxy, fy=fxy),cv2.resize(curr_img, None, fx=fxy, fy=fxy),None,0.5, 3, 15, 3, 7, 1.5, 0)
	flow = flow / fxy
	# normalization
	flow = np.round((flow + bound) / (2. * bound) * 255.)
	flow[flow < 0] = 0
	flow[flow > 255] = 255
	flow = cv2.resize(flow, (w, h))
	saveOptFlowToImage(flow, os.path.join(sys.argv[1], i[0].split("/")[1]))
	# saveImage(first_img,curr_img, os.path.join("temp", i[0].split("/")[1][:-8]))

	# print(n+=1)

	# cap = cv2.VideoCapture(i) # 0=camera
	# name = i.split("/")[2][:-4]
	# print(cap)
	# width = vcap.get(cv2.CAP_PROP_FRAME_WIDTH)   
	# height = vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)   
	# print(n)
	# if os.path.isfile(i[:index] + "_0.jpg") and os.path.isfile(i[:index] + "_1.jpg") and os.path.isfile(i[:index] + "_2.jpg"): 
	# 	row = (i,i[:index] + "_0.jpg",i[:index] + "_1.jpg",i[:index] + "_2.jpg")
	# 	all_list.append(row)
	# else:
	# 	print("not theere",i,i[:index] + "_0.jpg")
	# else:
	# 	if os.path.isfile(i.replace(i[-6:-4],'0')) and os.path.isfile(i.replace(i[-6:-4],'1')) and os.path.isfile(i.replace(i[-6:-4],'2')): 
	# 		row = (i,i.replace(i[-6:-4],'0'),i.replace(i[-6:-4],'1'),i.replace(i[-6:-4],'2'))
	# 		all_list.append(row)
	# 	else:
	# 		print("not there",i)	
# print(l[:3])
status_lst = Parallel(n_jobs=32,backend="threading")(delayed(vid2img)(i) for i in files)
# import pickle
# pickle.dump(all_list,open("motiongen_outTrain100.p","wb"))
# print(len(files),len(all_list))
# for i in all_list:
# 	print(i)
	# print(for i in )
# for i in a:
# 	print(width,height)
# 	if width>710 and height>710:
# 		num+=1
# 		print("index",num)
# 		n.append(i[:-18])
# print(len(n))	
# pickle.dump(n,open("highrescheck.p","wb"))
	# return (height,width)
