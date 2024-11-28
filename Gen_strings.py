"""
OOPS implementation by generation of strings in a GUI
@author: raina
"""
from tkinter import *
import random
root=Tk()
root.geometry("400x400")
root.title("oops implementation")
array_3d=[[['1','2','3','4','5','6','7','8','9','0'],["!","@",'$','%'],["A","B","C","E","F"]]]
c=0

# Initialize a label for showing the generated password
label = Label(root, text="Generated string will appear here")
label.pack(pady=100)
# Initialize a label for showing the number of generated strings
count_label = Label(root, text="Total strings generated: 0")
count_label.pack(pady=10)


class CreateElements:
    
    def __init__(self):
        print("This is create element class")
               
    def newpassword(self):
        random1=random.randint(0,5)
        random2=random.randint(0,1)
        random3=random.randint(0,4)
        
        letter1=array_3d[0][0][random1]
        letter2=array_3d[0][1][random2]
        letter3=array_3d[0][2][random3]
        label["text"]= letter1+letter2+letter3
        # Update the count label and generated strings list display
        self.update_display()
        
    def update_display(self):
       # Update the count of generated strings
        count_label["text"] = f"Total no of strings generated: {len(generated_strings)}"
       # Clear and update the text area with all generated strings
        generated_strings_text.delete(1.0, END)
        for string in generated_strings:
            generated_strings_text.insert(END, string + "\n" )   
    
    def createNewelements(self):
        global c
        c=c+1
        btn1=Button(root,text="String{}".format(c),command=self.newpassword)
        btn1.pack()
        btn1.place(relx=0.5,rely=0.2, anchor=CENTER)
        
    def close_window(self):
        root.destroy()    
                    
obj=CreateElements()
btn=Button(root,text="Generate random strings", command=obj.createNewelements)
btn.pack(pady=50)
btn.place(relx=0.5,rely=0.1, anchor=CENTER)

btn2=Button(root,text="Click to close the window",command=obj.close_window)
btn2.pack(pady=90)
btn2.place(relx=0.5,rely=0.6, anchor=CENTER)

root.mainloop()

