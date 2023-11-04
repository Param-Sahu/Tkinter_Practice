from tkinter import *
root = Tk()
root.title("Entry and Buttons: ") # Title of main widget 

head = Label(root,text="Enter text here : -")
head.pack()
entry = Entry(root,width=60,fg= "blue",bg="yellow",borderwidth=10,border=10)
entry.pack()
entry.get() # Get data enter from the user enter in entry box.
entry.insert(0,"Enter")#Insert default text in Entry Box but default text also come in get() function of entry.
"""
borderwidth and border(most preferred) work as its name, width keyword argument decides size.

"""
mybutton = Button(root,text = "Can't Click Here!",state=DISABLED,padx=50,pady=50)
'''
root tells that Labels and buttons are in widgets .
DISABLED state makes button inactive. (disabled  or enabled by state.).
padx and pady are responsible for size of the button.
'''
mybutton.pack()

def clicked():
    mylabel = Label(root,text="You Press Button. ")
    mylabel.pack()
    label2 = Label(root,text = "Hello "+entry.get())
    label2.pack()
    # text written in label2 is Hello and text enter in entry box.
    
    #print("You pressed Button.")
    # Print function print the message on console not on widget.

button = Button(root,text="Click Here ! ",command=clicked,background= "blue",foreground="#f00000")
'''
While calling a function we use parenthesis () but in command parameter , You wil have to write only 
function name without parenthesis .
If You add parenthesis Your function will automaticly execute without pressing buttons.

fg : fg refers to the font color (forground color) 
bg : bg refers to background color. 
Name of colors must be written in "".
You can also write hex color code instead of color name.
'''
button.pack()
#pack function pack the labels and  the button in widget
root.mainloop()