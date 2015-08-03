# Import module
import Tkinter
import tkMessageBox

# Define form
window = Tkinter.Tk()

# Set wide height of winfow
window.geometry("300x300")

window.title("Demo form")


def helloCallBack():
  tkMessageBox.showinfo( "Hello Python", "Hello World")

# Define button
btn = Tkinter.Button(window, text ="Hello", command = helloCallBack)

# Add button to form
btn.pack()

window.mainloop()