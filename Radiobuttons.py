from tkinter import *
root = Tk()
root.title('RadioButtons')
root.iconbitmap(r'C:\Users\91989\Pictures\Camera Roll\Python.ico')

a = IntVar()#Keep track changes of value changing over the time (By default 0). By this Funtion You can use .get()/.set() function 
a.set(0) # To set value to variable.

def Clicked(value):
    
    Label_1 = Label(root,text= str(value)+f"  {a.get()}" ,fg='Yellow',bg='Blue')
    Label_1.pack()
    Label_1.grid_forget()

frame = LabelFrame(root)
frame.pack()
for i in range(1,11):
    Radiobutton(frame,text=f'Option {i}',variable=a,value=i,fg="RED",background='Yellow',command= lambda : Clicked(a.get())).pack()

#Radiobutton(root, text='Option 2',variable=a,value=2,fg='Black',background='Yellow',command= lambda : Clicked(a.get())).pack(padx=40,pady=40)

Label_1 = Label(root,text= a.get(),fg='Yellow',bg='Blue') # If You do not use IntVar() ,StringVar() , You can not use .get()/.set() function.
Label_1.pack()
Label_1.pack()

root.mainloop()