from random import randint
print("=====Welcome to the number guessing game=====")
while True:
    try:
        diff = int(input("choose a difficulty level from 1/2/3: "))
        if diff not in (1,2,3):
            raise ValueError
    except ValueError:
        continue
    else:
        if diff ==1:
            rng = "1 to 20"
            num = randint(1,20)
        elif diff == 2:
            rng = "1 to 50"
            num = randint(1,50)
        else:
            rng = "1 to 100"
            num = randint(1,100)
        while True:
            try:
                you = int(input(f"Choose a number from {rng}: "))
                if not isinstance(you, int):
                    raise ValueError
            except ValueError:
                continue
            else:
                if you > num:
                    print("Guess lower")
                elif you < num:
                    print("guess higher")
                else:
                    print(f" You are goddamn right! The number was {num}")
                    to_continue = input("want to play another round? (y/n):").strip().lower()
                    break
        if to_continue == "y":
            continue
        else:
            break

    
    