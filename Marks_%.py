from tkinter import*
from tkinter import ttk
from tkinter import messagebox

root =Tk() 
root.geometry("400x250")
root.title("Calculate stream percentage")
label=Label(root,text="Choose the stream from below dropdown")
label.pack(padx=2,pady=10)

guielements=["English","Physics","Geography"]

dropdown=ttk.Combobox(root,state="readonly",values=guielements)
dropdown.pack()

class CreateElements:
    def __init__(self,studentname,stream,marks): 
        #print("Student details & percentage")
        self.studentname=studentname
        self.stream=stream
        self.marks=float(marks)
   
    def createlabel_ENG(self):
        subject_percent=float((self.marks/100)*100)
        label=Label(root,text=self.studentname+" scored {}% ".format(round(subject_percent),2)+" in "+self.stream)
        label.pack()
    def createlabel_PHY(self):
        subject_percent=float((self.marks/75)*100)
        label=Label(root,text=self.studentname+" scored {}% ".format(round(subject_percent),2)+" in "+self.stream)
        label.pack()   
    def createlabel_GEO(self):
        subject_percent=float((self.marks/80)*100)
        label=Label(root,text=self.studentname+" scored {}% ".format(round(subject_percent),2)+" in "+self.stream)
        label.pack()
        
    def choose(self):
        global dropdown
        element=dropdown.get()
        if(element=="English"):
         student1.createlabel_ENG()
         student4.createlabel_ENG()
        elif(element=="Physics"):
           student2.createlabel_PHY()
        elif(element=="Geography"):
           student3.createlabel_GEO()
    def message(self):
        messagebox.showinfo("showinfo","you clicked the button created using class")
        
def close_window():
    root.destroy()

btn2=Button(root,text="Close the window",command=close_window)
btn2.pack(pady=90)
btn2.place(relx=0.5,rely=0.8, anchor=CENTER)     

btn=Button(root,text="Show percentage",command=lambda:object1.choose())
btn.pack(padx=20,pady=10)

#Creating student instances                 
student1 = CreateElements("Amanda","English",80)
student4 = CreateElements("Riviera","English",83)
student2 = CreateElements("Olivia","Physics",73)
student3 = CreateElements("Roxanne","Geography",70)

object1 = CreateElements("","",0)

# Main loop to run the Tkinter window
root.mainloop()