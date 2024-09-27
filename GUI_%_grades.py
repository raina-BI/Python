# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 18:09:22 2024

explain the concept of polymorphism and inheritance

@author: raina
"""
from tkinter import *
import random

# Initialize the main window
root = Tk()
root.geometry("400x300")
root.title("GRADES")
# Initialize a label for showing the generated password
label = Label(root, text="")
label.pack(pady=10)

class Student:
    def __init__(self,studentname,stream,marks):
        #print("Student details & percentage")
        self.studentname=studentname
        self.stream=stream
        self.marks=float(marks)                           
        
        
class English(Student):
    def grades(self):
        subject_percent=float((self.marks/100)*100)
        label=Label(root,text=self.studentname+" scored {}% ".format(round(subject_percent),2)+" in "+self.stream)
        label.pack()
              
class Physics(Student):   
    def grades(self):
        subject_percent=float((self.marks/75)*100)
        label=Label(root,text=self.studentname+" scored {}% ".format(round(subject_percent),2)+" in "+self.stream)
        label.pack()
       
class Geography(Student):
    def grades(self):
        subject_percent=float((self.marks/80)*100)
        label=Label(root,text=self.studentname+" scored {}% ".format(round(subject_percent),2)+" in "+self.stream)
        label.pack()
      
def close_window():
    root.destroy()

btn2=Button(root,text="Click to close the window",command=close_window)
btn2.pack(pady=90)
btn2.place(relx=0.5,rely=0.6, anchor=CENTER)             

#Creating student instances                 
student1 = English("Amanda","English",80)
student1.grades()
student2 = Physics("Olivia","Physics",73)
student2.grades()
student3 = Geography("Roxanne","Geography",70)
student3.grades()

# Main loop to run the Tkinter window
root.mainloop()
