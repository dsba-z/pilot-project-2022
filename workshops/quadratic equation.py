a=float(input())
b=float(input())
c=float(input())
a!=0
d=b**2-4*a*c
if d>0:
    x1=(-b+d**(1/2))/(2*a)
    x2=(-b-d**(1/2))/(2*a)
    if x1>x2:
        print (x2, x1)
    else:
        print (x1, x2)
elif d==0:
    x3=-b/(2*a)
    print (x3)
else:
    print ()