# #age_calculator 1.2

def age_calculator():
    print("\n\n**AGE CALCUALTOR**")
    name = input("\nPlease enter your name: ")
    from datetime import date
    today = date.today()
    
    current_year = today.year
    birth_year = float(input("Your birth year: "))
    birth_month = float(input("Your birth month: "))
    current_month = today.month
    birth_date = float(input("Your birthdate: "))
    current_date = today.day
    age  = current_year - birth_year
    months = current_month - birth_month
    days = current_date - birth_date

    if current_month - birth_month < 0:
        age -= 1
        months += 12
    if current_date - birth_date < 0:
        days += 30.5
        months -= 1

    print(F"Hello,{name}",f"you're {age} years, {months} months and {days} days old or {age*12+months} months and {days} days or {(age*12+months)*30.5+days} days old") 

age_calculator()  


