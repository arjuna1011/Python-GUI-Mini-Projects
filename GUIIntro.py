from tkinter import *

App = Tk()
App.title('App')
App.geometry('450x450')

Display = Label(App, text = "Application Window")
Display.pack()

def show_msg():
    msg = Label(App, text = "Have a nice day.")
    msg.pack()

B = Button(App, text = "Click Me!", command = show_msg)
B.pack()



App.mainloop()