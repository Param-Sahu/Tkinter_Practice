from tkinter import *
root = Tk()  # Object of Widget created. this will create widget.


mylabel = Label(root,text="Hello World").grid(row=0,column=0)
mylabel1 = Label(root,text = "Hello Python 3.11").grid(row=1,column =1)
mylabel2 = Label(root,text = "Hello Param Sahu").grid(row=2,column=2)

'''
#You can also done the same thing by this , just remove .grid(...) function from mylabels. This is more cleaner way by up.
mylabel.grid(row =0,column=0)
mylabel1.grid(row =1,column=1)
mylabel2.grid(row=2,column=2)
'''

#If you write column = 12 although its remains in next closest common ,because grid system is relative.
#And does not posses actual grid lines.
root.mainloop() # Mainloop remembers all positioning and functions of tkinter in your widget.