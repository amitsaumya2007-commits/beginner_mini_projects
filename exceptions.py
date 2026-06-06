while True:
    try:
        x = int(input("What's the nummber ? "))
       
        break
    except ValueError:
        print("please enter a valid number")
        

print(f"x is {x}")
        
    
