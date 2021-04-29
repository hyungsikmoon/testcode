import os
from PIL import Image
from shutil import copyfile

filename_dir_path = '/home/youngtak.na/work_yolo/yolov4_train'
train_list_dir_path = '/home/youngtak.na/work_yolo/train_list/'

file_list = os.listdir(filename_dir_path)
filenames = [file for file in file_list if file.endswith(".jpg")]

cnt = 0
train_f = open(train_list_dir_path+'train.txt', mode='wt', encoding='utf-8')
val_f = open(train_list_dir_path+'val.txt', mode='wt', encoding='utf-8')

for filename in filenames:
    if cnt < 10000:
        train_f.write(filename_dir_path+"/"+filename+"\n")
        cnt += 1
    else:
        val_f.write(filename_dir_path+"/"+filename+"\n")

train_f.close()
val_f.close()
