from pdf2image import convert_from_path
import os
import time
from tkinter import *
from PIL import Image,ImageTk

photos = []
def convert(file):
    global photos
    pages = convert_from_path(file,size=(500,600))
    #print(len(pages))
    for page in pages:
        photos.append(ImageTk.PhotoImage(page))
    count=1
    #pdf.insert(END,file)
    for photo in photos:
        #pdf.create_image(0,y,anchor=NW,image=photo)
        pdf.insert(END,f"Page Number : {count}")
        pdf.image_create(END,image=photo)
        pdf.insert(END,"\n")
        count+=1
        
        
        

root = Tk()
root.geometry("500x600")
root.title("PDF Viewer")

# Creating the frame for PDF Viewer
pdf_frame = Frame(root).pack(fill=BOTH,expand=1)

# Adding Scrollbar to the PDF frame
scrol_y = Scrollbar(pdf_frame,orient=VERTICAL)
# Adding text widget for inserting images
pdf = Text(pdf_frame,yscrollcommand=scrol_y.set,bg="grey",height=600,width=400)
# Setting the scrollbar to the right side
scrol_y.pack(side=RIGHT,fill=Y)
scrol_y.config(command=pdf.yview)

# Finally packing the text widget
pdf.pack(fill=BOTH,expand=1)


file = r"C:\Users\alex\Desktop\Folders\Dino Game\mypdf.pdf"
convert(file)
root.resizable(0,0)
root.mainloop()
