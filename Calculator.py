from tkinter import *
root = Tk()
root.title("Calculator") # Define the main title or heading of Widget.

# Making Entry 
entry = Entry(root,width =10,fg= "blue",bg="yellow",borderwidth=5)
entry.grid(row=0,column=2)

#Making function for clicking 1,2,3 ... buttons
def clicked():
    pass
#Defineing and positioning (packing) Buttons for 1,2,3.... 0 
button_1 = Button(root,text="1",command=clicked,padx=40,pady=20).grid(row=3,column=3)
button_2 = Button(root,text="2",command=clicked,padx=40,pady=20).grid(row=3,column=2)
button_3 = Button(root,text="3",command=clicked,padx=40,pady=20).grid(row=3,column=1)
button_4 = Button(root,text="4",command=clicked,padx=40,pady=20).grid(row=2,column=3)
button_5 = Button(root,text="5",command=clicked,padx=40,pady=20).grid(row=2,column=2)
button_6 = Button(root,text="6",command=clicked,padx=40,pady=20).grid(row=2,column=1)
button_7 = Button(root,text="7",command=clicked,padx=40,pady=20).grid(row=1,column=3)
button_8 = Button(root,text="8",command=clicked,padx=40,pady=20).grid(row=1,column=2)
button_9 = Button(root,text="9",command=clicked,padx=40,pady=20).grid(row=1,column=1)
button_0 = Button(root,text="0",command=clicked,padx=40,pady=20).grid(row=4,column=2)



root.mainloop()