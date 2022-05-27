import tkinter as tk
import threading
import slr


class Base(tk.Tk):
    values = dict()

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title('SLR Parser')
        self.geometry("280x50")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def onsubmit(self):
        inp = self.e1.get()
        Base.values['inp'] = inp
        # print(inp)
        # os.system('cmd /k slr -g grammar.txt "' + inp + '"')
        # slr.main(grammar_file='grammar.txt',
        #          automaton=False, tokens=inp)
        self.controller.show_frame('PageOne')

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        tk.Label(self, text='Enter string: ').grid(row=0)
        self.e1 = tk.Entry(self)
        self.e1.insert(0, 'id + id * id')  # TODO: Remove later
        self.e1.grid(row=0, column=1)

        button = tk.Button(self, text="Submit", width=15,
                           command=threading.Thread(target=self.onsubmit).start)
        button.grid(row=1, column=1)


class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        if ('inp' in Base.values):
            tk.Label(self, text=Base.values['inp']).grid(row=0)
        else:
            print(Base.values)
            tk.Label(self, text="Nope").grid(row=0)


if __name__ == "__main__":
    app = Base()
    app.mainloop()
