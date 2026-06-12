# import sys
# try :
#     x = int(sys.argv[1])
#     y = int(sys.argv[2])

#     z = x+y
    
# except (IndexError,ValueError):
#     while True:
#         try:
#             print("index not found")
#             a = int(input("enter the first number here :"))
#             b = int(input("enter the second number here :"))
#             c = a+b
#             print(c)
#         except ValueError:
#             continue
#         else:
#             break
        
# else:
#    print(z)


# print("hello my name is", sys.argv[1], "and i am very", sys.argv[2])

from compre import hello

hello("sam")