# Multipication table of  18 :
# def multipication_table(num):
#     for  multiple in range(1,11):
#         yield  f"{num} x {multiple} = {num*multiple}"
    
# table = multipication_table(18)
# #  pythonn will automatically assign i = next(table) behind the curtains
# for i in table:
#     print(next(i))

# The Batch/Chunk processing tool:  
# def chunk_data(dataset,chunk_size):
#     for  lst in range(0,len(dataset),chunk_size):
#         yield dataset[lst: lst + chunk_size]

# obj = chunk_data([1,2,3,4,5,6,7],3)
# for list in obj:
#     print(list)

# The  Sliding Window: 
# def sliding_window(dataset, window_size):
#     stop_index = len(dataset) - window_size+1
#     for  lst in range(0,stop_index, 1):
#         yield dataset[lst: lst +window_size]

# obj = sliding_window([1,2,3,4,5],3)
# for list in obj:
#     print(list)

# def generate_ngram(text,n):
#     x = tuple(text.split(" "))
#     stop_index = len(x) - n +1
#     for tup in range(0,stop_index,1):
#         yield x[tup: tup+n]

# obj = generate_ngram("The quick brown fox jumps",2)
# for tuple in obj:
#     print(tuple)


# List chunk maker with pairable outputs
# def lst_split(lst,chunk_size):
#     stop_index = len(lst) - chunk_size +1
#     for i in range(0,stop_index,chunk_size):
#         yield lst[i: i+chunk_size]

# obj = lst_split([x for x in range(1,101)],2)
# for chunk in obj:
#     print(chunk)


def split_paragraph(lines):
    para = []
    for junct in lines:
        if junct != "":
            para.append(junct)
        else:
            yield para
            break

        
        

obj = split_paragraph(["Hello world.", "Welcome to Python.", "", "This is a new paragraph.", "Goodbye."])
for para_lst in obj:
    print(para_lst)


