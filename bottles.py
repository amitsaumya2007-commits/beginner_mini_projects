

def bottles():
    count = 99
    for lyrics in range(count,1,-1):
        
        if lyrics > 2:
            yield f"""[Verse {count - lyrics+1}]
    {lyrics} bottles of beer on the wall, {lyrics} bottles of beer
    Take one down and pass it around, {lyrics -1} bottles of beer on the wall"""
        elif lyrics == 2:
            yield f"""[Verse {count-lyrics+1}]
    {lyrics} bottles of beer on the wall, {lyrics} bottles of beer
    Take one down and pass it around, {lyrics -1} bottle of beer on the wall"""
        else:
            yield f"""[Verse {count-lyrics+1}]
    {lyrics} bottle of beer on the wall, {lyrics} bottls of beer
    Take one down and pass it around, no more bottles of beer on the wall"""
     
obj = bottles()
for all_bottles in obj:
    print(all_bottles)