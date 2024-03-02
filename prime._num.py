num=int(input("enter number"))
flag=False
for i in range(2,num//2):
    if  num%i==0:
      flag=True
      break
    else:
      Flag=False
      break
if flag==True:
   print("number is not prime")
elif flag==False:
   print("number is prime")


num=int(input("enter number"))
#flag=False
for i in range(2,num//2):
     a=num%i
     print(a)
     if a==0:
        break