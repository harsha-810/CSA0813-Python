n=int(input("Enter the number:"))
r=0
while n>0:
    a=n%10
    r=r+a
    n=n//10
print("sum of digits:",r)
