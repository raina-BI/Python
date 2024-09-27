#Generate fibonacci series

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
        
        
        
        
    