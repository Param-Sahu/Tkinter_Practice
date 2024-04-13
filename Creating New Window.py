import tkinter as tk

def create_new_window():
    new_window = tk.Tk()  # Create a new instance of Tk
    new_window.title("New Window")  # Set title for the new window

    # Add components to the new window
    label = tk.Label(new_window, text="This is a new window!")
    label.pack()

    # Run the new window's main loop
    new_window.mainloop()

def main_window():
    root = tk.Tk()
    root.title("Main Window")

    # Button to create a new window
    button = tk.Button(root, text="Create New Window", command=create_new_window)
    button.pack()

    root.mainloop()

if __name__ == "__main__":
    main_window()
