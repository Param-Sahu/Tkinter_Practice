from tkinter import *
root = Tk()
root.title("Frames")
#root.geometry("500x500")
root.iconbitmap(r'C:\Users\91989\Pictures\Camera Roll\Python.ico')

frame = LabelFrame(root,bd=5,relief='groove',padx=50,pady=50,font='Calibri 20') #  size of frame
frame.pack(padx=100,pady=100) # size of frame  in root gui (how much space frames take.)
# LabelFrame() function create a frame in root.
# text= in LabelFrame function is optional 
'''
inside Button and LabelFrame function padx and pady decides inner surface area .
while in pack function padx and pady decides outer surface area . (beyond the boundry)
'''

button = Button(frame,text='Click here ! ',fg='red',bg='yellow',bd=8,anchor='nw',font='Verdana 20',padx=50,pady=50)
# bd decides border side and anchor decides direction. East , West , North , South.
# In Button function padx and pady decides size of  inner surface of button. (inside surface area of button.)

button.pack(side=LEFT)
# in pack function padx and pady decides the size of button outer surface in frame. (outer  surface decide)

root.mainloop()