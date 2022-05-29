import tkinter as tk
import threading
import slr

class Frames(object):
    def output(self):
        newwin = tk.Toplevel(root)
        newwin.title('New Window')
        # newwin.geometry("200x100") 
        newwin.resizable(0, 0)

        slr.main(grammar_file='grammar.txt', automaton=False, tokens=self.query.get(), context=newwin)
        # display = tk.Label(newwin, text="Hello, " + self.query.get()) #getting parameter via query var
        # display.pack()
 
    
    def mainFrame(self,root):
        self.query = tk.StringVar() #passing parameter via query var
        
        root.title('SLR Parser')
        root.geometry("280x50") 
        root.resizable(0, 0)

        tk.Label(root, text='Enter string: ').grid(row=0)
        self.e1 = tk.Entry(root, textvariable=self.query)
        self.e1.insert(0, 'id + id * id')  # TODO: Remove later
        self.e1.grid(row=0, column=1)

        button = tk.Button(root, text="Submit", width=15,
                           command=self.output)
        button.grid(row=1, column=1)

root = tk.Tk()
app = Frames()
app.mainFrame(root)
root.mainloop()