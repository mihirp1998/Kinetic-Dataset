# import cv2
import os 
import sys
import pickle
import glob
from joblib import delayed
from joblib import Parallel
# l = open("trainHighRes.txt","rb").read().decode().split("\n")
# l = pickle.load(open("validVid.p","rb"))
# print(len(l))
import glob
folder_name = "tempValid10/*"
files = glob.glob(folder_name)
fl = len(folder_name) -1
# l = ["test/deuKjxPCC68_000006_000016.mp4"]
# l = pickle.load(open("highres.p","rb"))
# a = os.listdir("test/")
global n
n = 0
# print(len(a))
all_list = []
num = 0 
# p = Parallel(24)
# print(len(set(a[:][:-14])))
index = 30 +fl

def vid2img(i):
	global n,all_list
	# cap = cv2.VideoCapture(i) # 0=camera
	# name = i.split("/")[2][:-4]
	# print(cap)
	# width = vcap.get(cv2.CAP_PROP_FRAME_WIDTH)   
	# height = vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)   
	# print(n)
	n+=1

	if os.path.isfile(i[:index] + "_0000.jpg") and os.path.isfile(i[:index] + "_0005.jpg") and os.path.isfile(i[:index] + "_0010.jpg"): 
		row = (i,i[:index] + "_0000.jpg",i[:index] + "_0005.jpg",i[:index] + "_0010.jpg")
		all_list.append(row)
	else:
		print("not theere",i,i[:index] + "_0000.jpg")

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
import pickle
pickle.dump(all_list,open("validHyperTuple10.p","wb"))
print(len(files),len(all_list))
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
