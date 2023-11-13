from tkinter import *
from PIL import ImageTk,Image #PIL Pillow , ImageTk and Image help us to import images from our storage.
root = Tk()
root.title('Icons,Images and Exit Button')
root.iconbitmap(r'C:\Users\91989\Pictures\Camera Roll\Python.ico')
# iconbitmap function help to import .ico file to set as a icon.
# r'adress' finds the address of icon imaage.
#Please Image in format of .ico

my_image = ImageTk.PhotoImage(Image.open(r'C:\Users\91989\Pictures\Saved Pictures\Python.jpg'))
# PhotoImage() Function and open() function from ImageTk and Image respectively help to import images from directory .
#  r'' finds the address of icon image.
# We store Python image in my_image variable and later we pack within the label.

my_label= Label(image=my_image,padx=40,pady=40) # In Label function there is a keyword argument image like text argument which takes image value.
my_label.pack()

button_exit = Button(root,text="click here to exit.",command=root.quit).pack()
# root.quit function ends the gui , You can use root.destroy as well.
button_destroy = Button(root,image=my_image,padx=100,pady=100,fg="RED",bg="Yellow",command=root.destroy,font="Verdana 50",activebackground='red').pack()
# active background reflect color when button is clicked.
root.mainloop()