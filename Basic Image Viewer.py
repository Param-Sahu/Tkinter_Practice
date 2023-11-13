from tkinter import *
from  PIL import ImageTk , Image # help to import images from directory.
root = Tk()
root.title("Image Viewer App")
root.geometry("500x500")
# Images to be shown in Image viewer App (List of Images)
my_image_1 = ImageTk.PhotoImage(Image.open(r'C:\Users\91989\Pictures\Saved Pictures\C++.png'))
my_image_2 = ImageTk.PhotoImage(Image.open(r'C:\Users\91989\Pictures\Saved Pictures\Arduino.png'))
my_image_3 = ImageTk.PhotoImage(Image.open(r'C:\Users\91989\Pictures\Saved Pictures\Python_1.jpg'))
my_image_4 = ImageTk.PhotoImage(Image.open(r'C:\Users\91989\Pictures\Saved Pictures\download.jpg'))
my_image_5 = ImageTk.PhotoImage(Image.open(r'C:\Users\91989\Pictures\Saved Pictures\IOT.jpg'))

''' PhotoImage() Function and open() function from ImageTk and Image respectively help to import images from directory .
  r'' finds the address of icon image.
 We store Python image in my_image variable and later we pack within the label.'''

# Creating List of Images

global image_list
image_list = [my_image_1,my_image_2,my_image_3,my_image_4,my_image_5]

# Creating functions for button's action.

def forward():
    global image_label
    global image_list
    global i
    if i<4:
        image_label.grid_forget()
        i+=1
        image_label = Label(root,image=image_list[i])
        image_label.grid(row=0,column=0,columnspan=3)
    else:
        last_image = Label(root,text='This is Last Image ')
        last_image.grid(row=2,columnspan=3)

def backward():
    global image_label
    global image_list
    global i
    if i!=0:
        image_label.grid_forget()
        i-=1
        image_label = Label(root,image=image_list[i])
        image_label.grid(row=0,column=0,columnspan=3)
    else:
        last_image = Label(root,text='This is First Image ')
        last_image.grid(row=2,columnspan=3)


# Deciding row, column and columnspan for images .
global image_label
global i 
i=0
image_label = Label(root,image=image_list[i])
image_label.grid(row=0,column=0,columnspan=3,padx=160,pady=90)

# Creating forward ,backward buttons and exit button.

button_back = Button(root,text="<<",command=backward).grid(row=1,column=0)

button_forward = Button(root,text=">>",command=forward).grid(row=1,column=2)

button_exit = Button(root,text="Exit",font=14,command = root.quit).grid(row=1,column=1)


root.mainloop()