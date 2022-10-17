hour = int(input("enter hours:"))
#rate = (input("enter rate of hour:"))
if(hour<=40):
    a=hour*100
    print("your salary:",a)
else:
    z=hour-40
    x=z*50+4000
    print("extra :",z)
    print("total salary:",x)
    
    