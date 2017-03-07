from Tkinter import Tk, Label, Button, Entry

class GuiTest:
    def __init__(self,master):
        self.master = master
        master.title("Magic 8 Ball")

        self.label = Label(master, text="Ask your question!")
        self.label.pack()

        self.entry = Entry(master)
        self.entry.pack()

        self.greet_button = Button(master, text="Ask", command=self.Ask)
        self.greet_button.pack()

        self.greet_button = Button(master, text="Play Again", command=self.Ask)
        self.greet_button.pack()

        self.clear_button = Button(master, text="Clear", command=self.clear)
        self.clear_button.pack()

        self.close_button = Button(master, text="Quit", command=master.quit)
        self.close_button.pack()
    def clear(self):
        end = len(self.entry.get())
        self.entry.delete(0,end)
    def Ask(self):
        print(self.entry.get())

root = Tk()
my_gui = GuiTest(root)
root.mainloop()
