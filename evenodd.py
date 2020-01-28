a=int(input("Enter 1 for Even\n Enter 2 for odd\n"))
if(a==1):
    b=2
elif(a==2):
    b=3
else:
    print("Wrong input -1")
for i in range(1,100):
    if(i%b==0):
        print(i)
