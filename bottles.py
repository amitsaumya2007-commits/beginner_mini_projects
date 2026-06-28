def bottles():
    count = 99
    for lyrics in range(count,0,-1):
        if lyrics >2:
            suffix = "s"
        elif lyrics < 2:
            suffix = ""
        end_phrase = f"{lyrics -1} bottle{suffix} of beer on the wall" if lyrics != 1 else f"no more bottles of beer.\n Go to the store and buy some more, {count} bottles of beer on the wall."
        
        yield f"""[Verse {count - lyrics+1}]
    {lyrics} bottle{suffix} of beer on the wall, {lyrics} bottle{suffix} of beer
    Take one down and pass it around, {end_phrase}"""
     
obj = bottles()
for all_bottles in obj:
    print(all_bottles)