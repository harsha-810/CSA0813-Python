year=int(input("Enter the year"))
if year%4==0:
    print("%d is leap year"%year)
else:
        print("%d is not leap year"%year)

x=year%4
if x==0:
    print("Next leap year:",year+4)
else:
        print("Previous leap year:",year-x)
