import tkinter as tk

root = tk.Tk()
root.title("Entry with Horizontal Scrollbar")

# Create an Entry widget
entry = tk.Entry(root)
entry.grid(row=0, column=0, sticky='ew')

# Create a horizontal Scrollbar widget
scrollbar = tk.Scrollbar(root, orient='horizontal', command=entry.xview)
scrollbar.grid(row=1, column=0, sticky='ew')

# Configure the Entry widget to communicate with the Scrollbar
entry.config(xscrollcommand=scrollbar.set)

root.mainloop()
  