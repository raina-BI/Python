"""
Program to Generate fibonacci series

@author: raina
"""

from  tkinter import*
root=Tk()

root.title("fibonacci series")
root.geometry("500x500")

enter_no=Entry(root)
label=Label(root,text="Fibonaci Series")


def Fibonacci():
    x=int(input("Enter until which number, the fibonacci series need to be generated: "))
    n1,n2=0,1
    nth=0
    count=0
    print(n1)
    
    while nth<=x:
        print(n2)
        nth=n1+n2
        n1=n2
        n2=nth
        count=count+1
        
enter_no.pack()
btn=Button(root,text="generate the series",fg="blue",bg="white",command=Fibonacci())
btn.pack(padx=20,pady=10)     
        
label.pack()
root.mainloop()
    
        
        
        
    
