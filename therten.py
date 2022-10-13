from cmath import sqrt


a=int(input("enter tha value of a:"))
b=int(input("enter tha value of b:"))
c=int(input("enetr the value of c:"))
delta=((b**2)-(4*a*c))
sol1=((-b+sqrt(delta))/(2*a))
sol2=((-b-sqrt(delta))/(2*a))
print("the value of delta:",delta)
print("the value of sol1:",sol1)
print("the value of sol2:",sol2)
