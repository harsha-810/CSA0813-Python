n=int(input("Enter the number"))
r=0
original=n
while n>0:
    a=n%10
    r=r+a
    n=n//10
if original%r==0:
    print("Harshad number")
else:
    print("Not a Harshad number")
