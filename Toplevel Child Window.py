import tkinter as tk

root = tk.Tk()
root.geometry("200x300")
root.title("Main Window")

# Create a Toplevel window
top = tk.Toplevel(root)
top.geometry("180x100")
top.title("Toplevel Window")

# Add labels to both windows
l1 = tk.Label(root, text="This is the root window")
l2 = tk.Label(top, text="This is the toplevel window")
btn = tk.Button(root,text='Exit',command=root.destroy)
btn2 = tk.Button(top,text = 'Exit',command=top.destroy)
l1.pack()
l2.pack()
btn.pack()
btn2.pack()

root.mainloop()
