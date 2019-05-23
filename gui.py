import tkinter as tk
import sys


def txt_changed():
    lbl_slogan.config(text="I am Clicked")


root = tk.Tk()
root.title("Real Time Object Detection")
root.config()
root.minsize(300,160)
root.maxsize(300,160)   
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

btn_manual = tk.Button(sec_frame,command=txt_changed,text="Open Webcam",bg="#ff8000",width=45)
btn_manual.grid(row=0,column=1)

btn_manual = tk.Button(sec_frame,command=txt_changed,text="Detect",bg="#ff8000",width=45)
btn_manual.grid(row=1,column=1)

btn_manual = tk.Button(sec_frame,command=txt_changed,text="Show Objects",bg="#ff8000",width=45)
btn_manual.grid(row=2,column=1)

btn_manual = tk.Button(sec_frame,command=txt_changed,text="Show Previous Result",bg="#ff8000",width=45)
btn_manual.grid(row=3,column=1)

btn_manual = tk.Button(sec_frame,command=txt_changed,text="Delete Previous Result",bg="#ff8000",width=45)
btn_manual.grid(row=4,column=1)



root.mainloop()


#----------------------

def exit():
    root.destroy()
