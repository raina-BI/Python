from tkinter import*
from tkinter import ttk
import random

root =Tk() 
root.geometry("400x200")
root.title("oops implementation")

guielements=["Label","Button","Dropdown"]

dropdown=ttk.Combobox(root,state="readonly",values=guielements)
dropdown.pack()

class CreateElements:
    def __init__(self):
        print("This is create element class")
   
    def createlabel(self):
        randomno=random.randint(1,20)
        label=Label(root,text="new label is created using oops with random number " +str(randomno))
        label.pack()
        
    def createbutton(self):
        classbtn=Button(root,text="button", command=self.message)
        classbtn.pack(padx=20, pady=10)
    
    def createDropdown(self):
        value=[1,2,3,4]
        classdropdown=ttk.Combobox(root,state="readonly", values=value)
        classdropdown.pack()
        
    def choose(self):
        global dropdown
        element=dropdown.get()
        if(element=="Label"):
         self.createlabel()
        elif(element=="Button"):
           self.createbutton()
        elif(element=="Dropdown"):
           self.createDropdown()
    def message(self):
        messagebox.showinfo("showinfo","you clicked the button created using class")

object1=CreateElements()
btn=Button(root,text="createElement",command=object1.choose)
btn.pack(padx=20,pady=10)

root.mainloop()