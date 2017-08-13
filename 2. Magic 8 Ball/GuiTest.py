__author__ = 'Shane Yang'
from Tkinter import *
import random
import time

class GuiTest(Frame):
    #setup gui and organize the elements in the gui
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master = master
        master.title("Magic 8 Ball")

        self.label = Label(master, text="Ask your question!")
        self.label.pack()

        frame = Frame(master)
        frame.pack(fill=BOTH, expand=True)

        self.entry = Entry(frame)
        self.entry.pack(side=LEFT, padx=5, pady=5)

        self.ask_button = Button(frame, text="Ask", command=self.ask)
        self.ask_button.pack(side=LEFT, padx=0, pady=0)

        self.clear_button = Button(frame, text="Clear", command=self.clear)
        self.clear_button.pack(side=LEFT, padx=5, pady=5)

        frame1 = Frame(master)
        frame1.pack(fill=BOTH, expand=True)

        self.thinking = Label(frame1, text = " ")
        self.thinking.pack()
        self.answer = Label(frame1, text = " ")
        self.answer.pack()

        self.again_button = Button(master, text="Play Again", command=self.again)
        self.again_button.pack(side= LEFT, padx=5, pady=5)

        self.close_button = Button(master, text="Quit", command=master.quit)
        self.close_button.pack(side=RIGHT, padx=5, pady=5)


    def clear(self):
        end = len(self.entry.get())
        self.entry.delete(0,end)
    def ask(self):
        self.thinking.config(text = "Thinking...")
        self.update();
        time.sleep(2)
        choice = random.randint(0,19)
        response = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
        self.answer.config(text = response[choice])
    def again(self):
        self.clear()
        self.thinking.config(text = " ")
        self.answer.config(text= " ")

root = Tk()
my_gui = GuiTest(root)
root.mainloop()
