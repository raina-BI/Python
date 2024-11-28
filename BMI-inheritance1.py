# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 21:10:06 2024

@author: kajal
"""

#inheritance
#Inheritance is concept in OOPS which allows you to defina a class that inherits all/some of the methods and attributes defined in the another class

#base class/parent class--the class whose methods and attributes are being inherited 
#derived/child class:the class which inherits methods and properties from another class

#base class/parent class-
class Doctor():
    def __init__(self):
        print("this is class doctor")
    def BMI(weight,height):
        bmi=weight/(height*height)
        print("Your BMI is" +str(bmi))
    def heart_rate(heartrate):
        if(heartrate>60 and heartrate<100):
            print("your heart rate is normal")
        else:
            print("your heart rate is not normal")
            
class Patient(Doctor):
    def __init__(self,name,weight,height,heartrate):
        self.patientname=name
        self.patientweight=weight
        self.patientheight=height
        self.patientheartrate=heartrate
    def healthcheck(self):
        print("Patient name: " , self.patientname)
        Doctor.BMI(self.patientweight,self.patientheight)
        Doctor.heart_rate(self.patientheartrate)

patient1=Patient("Kajal",70,0.91,80)
patient1.healthcheck()
patient2=Patient("Amit",80,0.91,90)
patient2.healthcheck()
    
    