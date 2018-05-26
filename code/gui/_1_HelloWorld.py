from tkinter import *
import tkinter.messagebox as messagebox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.entry = Entry(self)
        self.entry.pack()
        self.quitButton = Button(self, text='hello', command=self.hello)
        self.quitButton.pack()

    def hello(self):
        name  = self.entry.get() or "world"
        messagebox.showinfo("Message","Hello, %s" %name)
        pass


app = Application()
app.master.title('hello world')
app.mainloop()
