# This Time using Tkinter canvas to display PDF 

from pdf2image import convert_from_path
import os
import time
from tkinter import *
from PIL import Image,ImageTk

photos = []
img = 0
def convert(file):
    global photos,img
    pages = convert_from_path(file,size=(550,650))
    #print(len(pages))
    for page in pages:
        photos.append(ImageTk.PhotoImage(page))
    #pdf.insert(END,file)
    pdf.create_image(0,0,anchor=NW,image=photos[img])
    
        
def next_img():
    global img
    img+=1
    if img >=len(photos):
        pdf.delete("all")
        pdf['bg'] = 'white'
        pdf.create_text(250, 300, text= "PDF Ended",fill="black",font=('Helvetica 15 bold'))
        img = len(photos)
    else:
        pdf.create_image(0,0,anchor=NW,image=photos[img])
        

def previous_img():
    global img
    img-=1
    if img >=0:
        pdf.create_image(0,0,anchor=NW,image=photos[img])
    else:
        img=0
        
               
        

root = Tk()
root.geometry("600x650")
root.title("PDF Viewer")

previous_btn = Button(root,text="<-",font=('arial',14,'bold'),command= previous_img)
previous_btn.pack(side=LEFT)

next_btn = Button(root,text="->",font=('arial',14,'bold'),command=next_img)
next_btn.pack(side=RIGHT)
# Creating the frame for PDF Viewer
pdf_frame = Frame(root).pack(fill=BOTH,expand=1)

# Adding text widget for inserting images
pdf = Canvas(pdf_frame,bg="grey",height=650,width=550)
# Finally packing the text widget
pdf.pack(fill=BOTH,expand=1)


file = r"C:\Users\alex\Desktop\Folders\Dino Game\mypdf.pdf"
convert(file)
root.resizable(0,0)
root.mainloop()
