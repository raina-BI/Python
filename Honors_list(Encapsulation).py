"""
explain the concept of encapsulation

@author: raina
"""
from tkinter import *
import random

# Initialize the main window
root = Tk()
root.geometry("400x300")
root.title("GRADES")
# Initialize a label 
label = Label(root, text="")
label.pack(pady=10)
label1=Label(root,text="Student Details")
label1.pack(pady=10)

class Student:
    def __init__(self,studentname,stream,marks):
        #private variables
        self.__studentname=studentname
        self.__stream=stream
        self.__marks=float(marks)
        
    #public method to access private variables    
    def get_info(self):
        return f"{self.__studentname}, {self.__stream}, {self.__marks}"
    
    #private method to display Honors list
    def __honors(self):
        if self.__marks > 90:
           print(f"{self.__studentname}"+" is in Honors class")
           label2=Label(root,text=self.__studentname+" is in Honors class")
           label2.pack()
           
    #public method to use the private method       
    def Student_Details(self):
        label=Label(root,text=self.__studentname+" "+self.__stream+" "+str(self.__marks))
        label.pack()
        self.__honors()

def close_window():
    root.destroy()

btn2=Button(root,text="Click to close the window",command=close_window)
btn2.place(relx=0.5,rely=0.6, anchor=CENTER)             

#Creating student instances #1                
student1 = Student("Sophia","English",80)
print(student1.get_info())
student1.Student_Details()

#student instance #2
student2 = Student("Rima","Physics",93)
print(student2.get_info())
student2.Student_Details()

#student instance #3
student3 = Student("Dora","Geography",70)
print(student3.get_info())
student3.Student_Details()

# Main loop to run the Tkinter window
root.mainloop()
