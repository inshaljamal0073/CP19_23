# Libraries
import cv2 # Webcam, Saving Image, Viewing Images, Connection with Dataset (Pretrained Models)
import pyttsx3 # Text to Speech
import win32com.client # In order to run Pyttsx3
import keyboard # Keyboard commands
import time # Time Handling
import tkinter as tk # For GUI
from tkinter import messagebox # importing messagebox
import sys # For some builtin functions
import os # For removing the file

def detection(img):

    # Defining Objects
    classNames = {0: 'background',
                  1: 'person', 2: 'bicycle', 3: 'car', 4: 'motorcycle', 5: 'airplane', 6: 'bus',
                  7: 'train', 8: 'truck', 9: 'boat', 10: 'traffic light', 11: 'fire hydrant',
                  13: 'stop sign', 14: 'parking meter', 15: 'bench', 16: 'bird', 17: 'cat',
                  18: 'dog', 19: 'horse', 20: 'sheep', 21: 'cow', 22: 'elephant', 23: 'bear',
                  24: 'zebra', 25: 'giraffe', 27: 'backpack', 28: 'umbrella', 31: 'handbag',
                  32: 'tie', 33: 'suitcase', 34: 'frisbee', 35: 'skis', 36: 'snowboard',
                  37: 'sports ball', 38: 'kite', 39: 'baseball bat', 40: 'baseball glove',
                  41: 'skateboard', 42: 'surfboard', 43: 'tennis racket', 44: 'bottle',
                  46: 'wine glass', 47: 'cup', 48: 'fork', 49: 'knife', 50: 'spoon',
                  51: 'bowl', 52: 'banana', 53: 'apple', 54: 'sandwich', 55: 'orange',
                  56: 'broccoli', 57: 'carrot', 58: 'hot dog', 59: 'pizza', 60: 'donut',
                  61: 'cake', 62: 'chair', 63: 'couch', 64: 'potted plant', 65: 'bed',
                  67: 'dining table', 70: 'toilet', 72: 'tv', 73: 'laptop', 74: 'mouse',
                  75: 'remote', 76: 'keyboard', 77: 'cell phone', 78: 'microwave', 79: 'oven',
                  80: 'toaster', 81: 'sink', 82: 'refrigerator', 84: 'book', 85: 'clock',
                  86: 'vase', 87: 'scissors', 88: 'teddy bear', 89: 'hair drier', 90: 'toothbrush'}

    def id_class_name(class_id, classes):
        for key, value in classes.items():
            if class_id == key:
                return value

    # Loading model
    model = cv2.dnn.readNetFromTensorflow('models/frozen_inference_graph.pb',
                                          'models/ssd_mobilenet_v2_coco_2018_03_29.pbtxt')
    image = cv2.imread(img)

    image_height, image_width, _ = image.shape

    model.setInput(cv2.dnn.blobFromImage(image, size=(300, 300), swapRB=True))
    output = model.forward()
    # print(output[0,0,:,:].shape)


    # Detection Code
    a = []

    for detection in output[0, 0, :, :]:
        confidence = detection[2]
        if confidence > .5:
            class_id = detection[1]
            class_name=id_class_name(class_id,classNames)
            #print(str(str(class_id) + " " + str(detection[2])  + " "))
            a.append(class_name)
            box_x = detection[3] * image_width
            box_y = detection[4] * image_height
            box_width = detection[5] * image_width
            box_height = detection[6] * image_height
            cv2.rectangle(image, (int(box_x), int(box_y)), (int(box_width), int(box_height)), (23, 230, 210), thickness=1)
            cv2.putText(image,class_name ,(int(box_x), int(box_y+.05*image_height)),cv2.FONT_HERSHEY_SIMPLEX,(.005*image_width),(0, 0, 255))
            #cv2.putText(image,str(detection[2]) ,(int(box_x), int(box_y+.03*image_height)),cv2.FONT_HERSHEY_SIMPLEX,(.003*image_width),(0, 0, 255))

    cv2.imshow('Result', image)
    # cv2.imwrite("image_box_text.jpg",image)

    # Creating dictionary for the objects
    counter = 0
    data = {  }
    for i in range( len(a) ):
        data.update( { a[i]: a.count( a[i] ) } ) # It will replace previous pair when found new
    
    # Creating a sentence for the text to speech
    string = "There are"
    
    for i in range( len(data) ):
        string+=" "+str(data[ a[i] ])+" "+a[i]+" and"
    
    newString = string.rstrip('and')

    # Find if there is no object found
    if len(a)==0:
        engine = pyttsx3.init()
        engine.say( "No Object Found, Try Again" )
        engine.runAndWait()
    else:
        engine = pyttsx3.init()
        engine.say( newString )
        engine.runAndWait()
    
    write_file = open('last_objects.txt','w')
    for i,j in data.items():
        write_file.write(i+":"+str(j)+"\n")
    write_file.close()

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def store_img():
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, None, fx=1, fy=1, interpolation=cv2.INTER_AREA)
        cv2.imshow('Webcam', frame)
        cv2.imwrite(filename='saved_img.jpg', img=frame)
        c = cv2.waitKey(1)
        if keyboard.is_pressed(' '):  # if key 'q' is pressed 
            break  # finishing the loop
        else:
            pass


    cap.release()
    cv2.destroyAllWindows()

    return 'saved_img.jpg'

def open_webcam():
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, None, fx=1, fy=1, interpolation=cv2.INTER_AREA)
        cv2.imshow('Webcam', frame)
        cv2.imwrite(filename='saved_img.jpg', img=frame)
        c = cv2.waitKey(1)
        if keyboard.is_pressed(' '):
            break  # finishing the loop
        else:
            pass

    cap.release()
    cv2.destroyAllWindows()

    detection('saved_img.jpg')

def show_presult():
    try:
        reading_objects = open('last_objects.txt','r')

        tk.messagebox.showinfo("Last Objects", reading_objects.read())

        reading_objects.close()
    except:
        tk.messagebox.showinfo("Error", "File not found.")

def delete_result():
    try:
        os.remove('last_objects.txt')
    except:
        tk.messagebox.showinfo("Error", "File not found. There is nothing to remove.")

root = tk.Tk()
root.title("Real Time Object Detection")
root.config()
root.minsize(300,110)
root.maxsize(300,110)   
root.columnconfigure(2, weight=2)

#---------------------TITLE----------------------

title_frame = tk.Frame(root,bg="#0B0C10")   
title_frame.grid(row=0,column=0,columnspan=3,sticky="ew")

lbl_title= tk.Label(title_frame,text="Real Time Object Detection",fg="#ffffff")
lbl_title['bg']=title_frame['bg']
lbl_title.config(font=("Arial",18))
lbl_title.grid(row=0,column=1,columnspan=2)

sec_frame = tk.Frame(root,bg="#1F2833")
sec_frame.grid(row=1,column=0,columnspan=4,sticky="ew")

btn_webcam = tk.Button(sec_frame,command=open_webcam,text="Open Webcam (Hit space to detect the objects)",bg="#ff8000",width=45)
btn_webcam.grid(row=0,column=1)

btn_presult = tk.Button(sec_frame,command=show_presult,text="Show Previous Result",bg="#ff8000",width=45)
btn_presult.grid(row=3,column=1)

btn_dpresult = tk.Button(sec_frame,command=delete_result,text="Delete Previous Result",bg="#ff8000",width=45)
btn_dpresult.grid(row=4,column=1)


root.mainloop()

def exit():
    root.destroy()
