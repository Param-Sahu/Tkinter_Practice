import math
from tkinter import *
root = Tk()
root.title("Calculator") # Define the main title or heading of Widget.
root.geometry('500x500')
root.maxsize(500,500)
root.minsize(500,500)
# Making Entry 
entry = Entry(root,width =35,fg= "blue",bg="yellow",borderwidth=5,relief='flat',font=100)
entry.grid(row=0,column=1,columnspan=5,pady=10)

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
    lenth= len(entry.get())
    entry.delete(lenth-1,END)

def action(value):
    
    global first_num 
    global operator 
    operator = value
    
    first_num=float(entry.get())
    entry.delete(0,END)

    

def equal():
    global first_num
    global operator

    if operator == 'sqrt':
        num = entry.get()[1:]
        entry.delete(0,END)
        entry.insert(0,math.sqrt(float(num)))

    elif operator == 'sin':
        degree = entry.get()[4:]
        radian = (math.pi/180)*float(degree) 
        entry.delete(0,END)
        entry.insert(0,math.sin(float(radian)))

    elif operator == 'cos':
        degree = entry.get()[4:]
        radian = (math.pi/180)*float(degree) 
        entry.delete(0,END)
        entry.insert(0,math.cos(radian))

    elif operator == 'tan':
        degree = entry.get()[4:]
        radian = (math.pi/180)*float(degree) 
        entry.delete(0,END)
        entry.insert(0,math.tan(float(radian)))

    elif operator == 'cosec':
        degree = entry.get()[6:]
        radian = (math.pi/180)*float(degree) 
        entry.delete(0,END)
        entry.insert(0,1/(math.sin(float(radian))))

    elif operator == 'sec':
        degree = entry.get()[4:]
        radian = (math.pi/180)*float(degree) 
        entry.delete(0,END)
        entry.insert(0,1/(math.cos(float(radian))))

    elif operator == 'cot':
        degree = entry.get()[4:]
        radian = (math.pi/180)*float(degree) 
        entry.delete(0,END)
        entry.insert(0,1/(math.tan(float(radian))))

    elif operator == 'log':
        value = entry.get()[4:]
        entry.delete(0,END)
        entry.insert(0,math.log10(float(value)))

    elif operator == 'ln':
        value = entry.get()[3:]
        entry.delete(0,END)
        entry.insert(0,math.log(float(value)))

    elif operator == 'e':
        value = entry.get()[3:]
        entry.delete(0,END)
        entry.insert(0,math.exp(float(value)))

    

    else:
        second_num = float(entry.get())
        entry.delete(0,END)

    if operator == '+':
        entry.insert(0,first_num + second_num)
    elif operator == '-':
        entry.insert(0,first_num-second_num)
    elif operator == '*':
        entry.insert(0,first_num * second_num) # Always write index position number
    elif operator == '/':
        if second_num == 0:
            zero = Label(root,text = "Can't divided by zero.",font=20)
            zero.grid(row=7,column=1,columnspan=4) #columnspan decides how much columns have to merge.

        else:         
            entry.insert(0,first_num/second_num) #Always write index position number .
    

        
    
def facto():
    value=float(entry.get())
    entry.delete(0,END)
    entry.insert(0,math.factorial(int(value)))

def square_root():
    entry.delete(0,END)
    global operator
    entry.insert(0,'√')
    operator = 'sqrt'

    
def scientific(function):
    global operator
    entry.delete(0,END)

    if function == 'sin':
        entry.insert(0,'sin(')
        operator = 'sin'

    elif function == 'cos':
        entry.insert(0,'cos(')
        operator = 'cos'

    elif function == 'tan':
        entry.insert(0,'tan(')
        operator = 'tan'

    elif function == 'cosec':
        entry.insert(0,'cosec(')
        operator = 'cosec'
    
    elif function == 'sec':
        entry.insert(0,'sec(')
        operator = 'sec'

    elif function == 'cot':
        entry.insert(0,'cot(')
        operator = 'cot'

    elif function == 'log':
        entry.insert(0,'log(')
        operator = 'log'
    
    elif function == 'ln':
        entry.insert(0,'ln(')
        operator = 'ln'

    elif function == 'e':
        entry.insert(0,'e^(')
        operator = 'e'

    
def negative():
    lenth = len(entry.get())
    entry.insert(lenth,'-')

#Defineing and positioning (packing) Buttons for 1,2,3.... 0 
button_1 = Button(root,text="1",command=lambda : clicked(1),padx=40,pady=20,font=9).grid(row=3,column=3)

button_2 = Button(root,text="2",command=lambda : clicked(2),padx=40,pady=20,font=9).grid(row=3,column=2)

button_3 = Button(root,text="3",command=lambda : clicked(3),padx=40,pady=20,font=9).grid(row=3,column=1)

button_4 = Button(root,text="4",command=lambda : clicked(4),padx=40,pady=20,font=9).grid(row=2,column=3)

button_5 = Button(root,text="5",command=lambda : clicked(5),padx=40,pady=20,font=9).grid(row=2,column=2)

button_6 = Button(root,text="6",command=lambda : clicked(6),padx=40,pady=20,font=9).grid(row=2,column=1)

button_7 = Button(root,text="7",command=lambda : clicked(7),padx=40,pady=20,font=9).grid(row=1,column=3)

button_8 = Button(root,text="8",command=lambda : clicked(8),padx=40,pady=20,font=9).grid(row=1,column=2)

button_9 = Button(root,text="9",command=lambda : clicked(9),padx=40,pady=20,font=9).grid(row=1,column=1)

button_0 = Button(root,text="0",command=lambda : clicked(0),padx=40,pady=20,font=9).grid(row=4,column=1)

button_add = Button(root,text="+",command=lambda : action('+'),padx=40,pady=20,font=20).grid(row=4,column=2)

button_minus = Button(root,text="- ",command=lambda : action('-'),padx=40,pady=20,font=20).grid(row=4,column=3)

button_multiply = Button(root,text="×",command=lambda : action('*'),padx=40,pady=20,font=9).grid(row=5,column=1)

button_divide = Button(root,text="/",command=lambda : action('/'),padx=42.49,pady=20,font=20).grid(row=5,column=2)

button_decimal = Button(root,text=" .",command=lambda : clicked('.'),padx=40,pady=20,font=20).grid(row=5,column=3)

button_equal = Button(root,text="=",command=equal,padx=40,pady=20,font=9).grid(row=6,column=1)

button_clear = Button(root,text="Clear",command=clear,padx=25,pady=20,font=9).grid(row=6,column=2)

button_backspace = Button(root,text="<<",command=backspace,padx=35,pady=20,font=9).grid(row=6,column=3)

button_factorial = Button(root,text='!',command=facto,padx=42,pady=20,font=20).grid(row=1,column=4)

button_sqrt = Button(root,text='√',command= square_root,padx=40,pady=20,font=20).grid(row=2,column=4)

button_sin = Button(root,text='sin',command=lambda : scientific('sin'),padx=35,pady=20,font=20).grid(row=3,column=4)

button_cos = Button(root,text='cos',command=lambda : scientific('cos'),padx=32,pady=20,font=20).grid(row=4,column=4)

button_tan = Button(root,text='tan',command=lambda : scientific('tan'),padx=34,pady=20,font=20).grid(row=5,column=4)

button_cosec = Button(root,text='cosec',command=lambda : scientific('cosec'),padx=24,pady=20,font=20).grid(row=6,column=4)

button_sec = Button(root,text='sec',command=lambda : scientific('sec'),padx=35,pady=20,font=20).grid(row=1,column=5)

button_tan = Button(root,text='cot',command=lambda : scientific('cot'),padx=37,pady=20,font=20).grid(row=2,column=5)

button_log = Button(root,text='log',command=lambda : scientific('log'),padx=37,pady=20,font=20).grid(row=3,column=5)

button_ln = Button(root,text='ln',command=lambda : scientific('ln'),padx=42,pady=20,font=20).grid(row=4,column=5)

button_e = Button(root,text='e',command=lambda : scientific('e'),padx=42,pady=20,font=20).grid(row=5,column=5)

button_negative = Button(root,text='+/-',command=negative,padx=38,pady=20,font=20).grid(row=6,column=5)

'''
command = lambda : clicked(value)
By use of lambda , we can pass the parameter with use of parenthesis ,
without lambda we can not use parenthesis.
command keyword argument decides what button will perform action when clicked.
'''
root.mainloop()