import Tkinter,tkFileDialog
from Tkinter import *
from tkMessageBox import askokcancel           
import os

class Quitter(Frame):                          
    def __init__(self, parent=None):           
        Frame.__init__(self, parent)
        self.pack()
        widget = Button(self, text='Quit', command=self.quit)
        widget.pack(expand=YES, fill=BOTH, side=LEFT)
    def quit(self):
        ans = askokcancel('Verify exit', "Really quit?")
        if ans: Frame.quit(self)
fields = 'Base Code', 'C Code', 'Results'
def makeform(root, fields):
    form = Frame(root)                              
    left = Frame(form)
    rite = Frame(form)
    form.pack(fill=X) 
    left.pack(side=LEFT)
    rite.pack(side=RIGHT, expand=YES, fill=X)

    variables = []
    for field in fields:
        lab = Label(left, width=15, text=field  )
        ent = Entry(rite)
        lab.pack(side=TOP)
        ent.pack(side=TOP, fill=X)
        var = StringVar()
        ent.config(textvariable=var)
        var.set('') 
        variables.append(var)
    return variables


def Click(variables):
    dirname = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
    if len(dirname ) > 0:
        print "You chose %s" % dirname 
        form = Frame(root)
        rite = Frame(form)
        ent = Entry(rite)
        var = StringVar()
        ent.config(textvariable=var)
        var.set('Set path here...') 
        variables.append(var)
    return dirname

if __name__ == '__main__':
    root = Tkinter.Tk()
    vars = makeform(root, fields)
    
    Button(root, text='Base Path', command=(lambda v=vars: Click(v))).pack(side=LEFT)
    Button(root, text='C Code Path', command=(lambda v=vars: Click(v))).pack(side=LEFT)
    Button(root, text='Results Path', command=(lambda v=vars: Click(v))).pack(side=LEFT)
    Button(root, text='Execute query', command=(lambda v=vars: Click(v))).pack(side=LEFT)
    Tkinter.Button(root,text='Test button',command = Click)
    Quitter(root).pack(side=RIGHT)
    root.bind('<Return>', (lambda event, v=vars: Click(v)))   
    root.mainloop()


