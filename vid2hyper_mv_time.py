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
folder_name = "tempValid_till260_10Vid/*"
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
index = 30 
index = -8
def vid2img(i):
	global n,all_list
	# cap = cv2.VideoCapture(i) # 0=camera
	# name = i.split("/")[2][:-4]
	# print(cap)
	# width = vcap.get(cv2.CAP_PROP_FRAME_WIDTH)   
	# height = vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)   
	# print(n)

	index = int(i[-8:-4])

	n+=1
	i_strip = i.split("/")
	zero_file = i_strip[1][:-8] + "0000.jpg"
	fifth_file = i_strip[1][:-8] + "0005.jpg"
	tenth_file = i_strip[1][:-8] + "0010.jpg"
	# mv_folder = os.path.join(i_strip[0]+"_mv",i_strip[1])
	zero_file_xflow = os.path.join(i_strip[0]+"_mv",zero_file +"_x.JPEG")
	zero_file_yflow = os.path.join(i_strip[0]+"_mv",zero_file +"_y.JPEG")
	
	fifth_file_xflow = os.path.join(i_strip[0]+"_mv",fifth_file +"_x.JPEG")
	fifth_file_yflow = os.path.join(i_strip[0]+"_mv",fifth_file +"_y.JPEG")

	tenth_file_xflow = os.path.join(i_strip[0]+"_mv",tenth_file +"_x.JPEG")
	tenth_file_yflow = os.path.join(i_strip[0]+"_mv",tenth_file +"_y.JPEG")		

	zero_file = os.path.join(i_strip[0],zero_file)
	fifth_file = os.path.join(i_strip[0],fifth_file)
	tenth_file = os.path.join(i_strip[0],tenth_file)

	if (index>=0 and index<20):
		if os.path.isfile(zero_file) and os.path.isfile(fifth_file) and os.path.isfile(tenth_file) and os.path.isfile(zero_file_yflow) and os.path.isfile(zero_file_xflow) and os.path.isfile(fifth_file_yflow) and os.path.isfile(fifth_file_xflow) and os.path.isfile(tenth_file_yflow) and os.path.isfile(tenth_file_xflow): 
			row = (i,zero_file,fifth_file,tenth_file,zero_file_xflow,zero_file_yflow,fifth_file_xflow,fifth_file_yflow,tenth_file_xflow,tenth_file_yflow)
			all_list.append(row)
		else:
			print("not theere",tenth_file_yflow)

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
pickle.dump(all_list,open("0to20_mv.p","wb"))
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

