import math 

angel=eval(input("enter angel"))
height=eval(input("enter height"))

angler=(3.14/180)*angel
length=(height/math.sin(angler))
print("length is:",length)
