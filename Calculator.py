from tkinter import *
root = Tk()
root.title("Calculator") # Define the main title or heading of Widget.

# Making Entry 
entry = Entry(root,width =35,fg= "blue",bg="yellow",borderwidth=5,relief='flat',font=5)
entry.grid(row=0,column=1,columnspan=3,pady=20,padx=20)

#Making function for clicking 1,2,3 ... buttons
def clicked(value):
    #global current
    current = entry.get()
    entry.delete(0,END)
    entry.insert(0,str(current)+str(value))#insert function insert value at position on entry.

    ''' 
    Above three statements displaying the numbers enterred by user.
    entry.get() function get the value available on screen
    entry.delete() function delete whole value at index position 0 
    entry.insert() function print the whole value :
        current takes value available on screen and value is at the time enterred by user.
        This whole is continuously running in loop.       
    '''
def clear(): #Creating function for clearing whole screen.
    entry.delete(0,END)


def backspace(): # Creating function for Backspace
    pass

def add():
    first_num =entry.get()
    global f_num 
    f_num = int(first_num)
    entry.delete(0,END)

def equal():
    global f_num
    second_num = entry.get()
    entry.delete(0,END)
    entry.insert(0,f_num + int(second_num))


#Defineing and positioning (packing) Buttons for 1,2,3.... 0 
button_1 = Button(root,text="1",command=lambda : clicked(1),padx=40,pady=20).grid(row=3,column=3)
button_2 = Button(root,text="2",command=lambda : clicked(2),padx=40,pady=20).grid(row=3,column=2)
button_3 = Button(root,text="3",command=lambda : clicked(3),padx=40,pady=20).grid(row=3,column=1)
button_4 = Button(root,text="4",command=lambda : clicked(4),padx=40,pady=20).grid(row=2,column=3)
button_5 = Button(root,text="5",command=lambda : clicked(5),padx=40,pady=20).grid(row=2,column=2)
button_6 = Button(root,text="6",command=lambda : clicked(6),padx=40,pady=20).grid(row=2,column=1)
button_7 = Button(root,text="7",command=lambda : clicked(7),padx=40,pady=20).grid(row=1,column=3)
button_8 = Button(root,text="8",command=lambda : clicked(8),padx=40,pady=20).grid(row=1,column=2)
button_9 = Button(root,text="9",command=lambda : clicked(9),padx=40,pady=20).grid(row=1,column=1)
button_0 = Button(root,text="0",command=lambda : clicked(0),padx=40,pady=20).grid(row=4,column=1)
button_add = Button(root,text="+",command=add,padx=40,pady=20).grid(row=4,column=2)
button_equal = Button(root,text="=",command=equal,padx=40,pady=20).grid(row=4,column=3)
button_clear = Button(root,text="Clear",command=clear,padx=30,pady=20).grid(row=5,column=1)
button_backspace = Button(root,text="<-",command=backspace,padx=40,pady=20).grid(row=5,column=2)

'''
command = lambda : clicked(value)
By use of lambda , we can pass the parameter with use of parenthesis ,
without lambda we can not use parenthesis.
command keyword argument decides what button will perform action when clicked.
'''
root.mainloop()