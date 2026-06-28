import time
win = [('rck','scr'),('scr','ppr'),('ppr','rck')]
lose = [(x,y) for y,x in win]
tie = [(x,x) for x,_ in win]

start = input("Shall we start the game (y/n): " ).lower().strip()
while True:
    if start == "y":
        value = ["rck","ppr","scr"]
        try:
            you = input("Enter (rck/ppr/scr) : ").lower().strip()
            if you not in value:
                raise ValueError("Wrong Input")
        except ValueError:
            print("Enter a valid choice from 'rck','ppr','scr'" )
            continue
        else:
            current_ns = time.time_ns()
            computer_index = current_ns%3
            computer = value[computer_index]
            result = (you,computer)
            print(f"Computer: {computer}")
            if result in win:
                print("---YOU WON---")
            elif result in lose:
                print("---YOU LOST---")
            else:
                print("---IT'S A TIE---")
            to_continue = input("Want to play another around (y/n): ").lower().strip()
            if to_continue == "y":
                continue
            else:

                break
    else:
        break