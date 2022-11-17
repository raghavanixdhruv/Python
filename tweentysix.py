def triangle(d):
     
    
    h = d - 1
    for i in range(1, d):
        
       
        for j in range(1, i+1):
         
            print(j, end=" ")
        print("\r")
    h = d - 1
    for i in range(0, d):
        for j in range(0, h):
            print(end=" ")
        h = h - 1
        for j in range(0, i+1):
         
            print("* ", end="")
            
        print("\r")
 

d = 5
triangle(d)


