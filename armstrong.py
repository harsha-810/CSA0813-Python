n=int(input("Enter the number:"))
r=0
original=n
while n>0:
    a=n%10
    r=r+(a*a*a)
    n=n//10
if r==original:
    print("Armstrong number")
else:
    print("Not armstrong number")
