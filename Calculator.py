import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root=root
        self.root.title("Calculator")
        self.root.geometry('330x360')
        self.root.config(bg='lightgray')
        self.root.resizable(False, False)
        self.entry=tk.Entry(root, font=("Arial",20),bg="white",fg="black")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        buttons=[('e',1,0),('pi',1,1),('**',1,2),('C',1,3),
                 ('(',2,0),(')',2,1),('%',2,2),('/',2,3),
                 ('7',3,0),('8',3,1),('9',3,2),('*',3,3),
                 ('4',4,0),('5',4,1),('6',4,2),('-',4,3),
                 ('1',5,0),('2',5,1),('3',5,2),('+',5,3),
                 ('.',6,0),('0',6,1),('<-',6,2),('=',6,3)]
        for(text,row,column) in buttons:
            bgc="lightblue" if text in ('<-','=','C','.','e','pi','**','sqrt') else "white"
            btn=tk.Button(root,text=text,font=("Arial",15), bg=bgc,fg="black", command= lambda t=text:self.onclick(t))
            btn.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")

    def onclick(self, text):
        if(text == '='):
            try:
                r=round(eval(self.entry.get()), 10)
                self.entry.delete(0,tk.END)
                self.entry.insert(tk.END,str(r))
            except:
                self.entry.delete(0,tk.END)
                self.entry.insert(tk.END,"ERROR")
        elif(text== '<-'):
            val= self.entry.get()[:-1]
            self.entry.delete(0,tk.END)
            self.entry.insert(tk.END, str(val))
        elif(text=='C'):
            self.entry.delete(0,tk.END)
        elif(text=='pi'):
            self.entry.insert(tk.END, str(math.pi))
        elif(text== 'e'):
            self.entry.insert(tk.END, str(math.e))
        else:
            self.entry.insert(tk.END,text)
root=tk.Tk()
Calculator=Calculator(root)
root.mainloop()
