while True:
    text = input("Enter the sentence or word to count the vowels: ").lower()
    vowels_count = []
    for vowel in text:
        if vowel in "aeiou":
            vowels_count.append(vowel)

    count = len(vowels_count)
    if count == 0:
        print("There are no vowels in the sentence/word.")
        x = input( "Type 'q' to quit or any other key to continue.").lower()

        if x == "q":
            break
        else:
            continue
    
    
    else:
        print(f"There are {count} vowels in this sentence")
        break