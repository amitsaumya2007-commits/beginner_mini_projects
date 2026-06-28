food = {"1":3.50, '2':2.50, '3':4.00,
         '4':3.50,'5':1.75,'6':1.50,
         '7':2.25, '8':3.75, '9':1.25, }
start = input("Start ordering (y/n): ").strip().lower()
while start == "y":
    order = input(f"""Please give the order by the numbers(eg.- 6785):
                    1.Chicken Strips - $3.50
                    2.French Fries - $2.50
                    3.Hamburger - $4.00
                    4.Hotdog - $3.50
                    5.Large Drink - $1.75
                    6.Medium Drink - $1.50
                    7.Milk Shake - $2.25
                    8.Salad - $3.75
                    9.Small Drink - $1.25
                    
                    Type 'q' to quit.
        
                        >> """)
    if order and all(item in food for item in order):
        total = 0
        for i in order:
            if i in food:
                total += food[i]
        print(f"Your total would be ${total:.2f}")
    elif order == "q":
        break
    else:
        print("Please give a valid order")

