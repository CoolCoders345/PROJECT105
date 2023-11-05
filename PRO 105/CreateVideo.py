import os
import cv2

path = "Images/"
images = []

for fileName in "C:/Users/kovai/Downloads/PRO 105/Images/PRO-C105-Project-Images-main":
    name, extension=os.path.splitext(fileName)
    print(name)
    print(extension)
    if extension=="":
        continue
    if extension in [".gif",".png","jpg",".jpeg",".jfif"]:
        fileName = path+"/"+name
        images.append(fileName)
        print(fileName)
count = len(images)
frame = cv2.imread(images[0])
width, height, channel = frame.shape()
size = (width, height)
print(size)
out=cv2.VideoWriter("Project.avi",fourcc=cv2.VideoWriter_fourcc(*'DIVX'),fps=0.8)
