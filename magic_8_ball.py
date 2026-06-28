import random,time, sys
magic_8_ball_answers = [
    # Affirmative answers (10)
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    
    # Non-committal/Neutral answers (5)
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    
    # Negative answers (5)
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful"
]
start = input("Ready to start (y/n): ").lower()
while True:
    if start == "y":
        print("""--------------MAGIC 8 BALL------------""")
        input("Enter your question and let the ball decide: ")
        print("Processing", end="")
        for i in range(3):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(1)

        print("")
        answer = random.choice(magic_8_ball_answers)
        print(answer)
        cntinue = input("Want to ask more questions (y/n): ")
        if cntinue == "y":
            continue
        else:
            break

    else:
        break