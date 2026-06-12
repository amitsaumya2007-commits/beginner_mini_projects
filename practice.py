# Problem 1 :

# for i in range(1,6):
#     print()
#     for num in range(1,6):
#         x = num*i
#         print(x,end=" ")

# Problem 2 :

# users = ["admin", "coder99", "python_king", "pixel_art"]
# u_input = input("Please create a username :")
# for user in users:
#     if u_input == user:
#         print("Username already exists.")
#         break
# else:
#     print("Registered successfully")

# Problem 3 :

# rng = int(input("please enter the range :"))
# for row in range(1,rng+1):
#     print("$"*(rng-row),end="")
    
#     for num in range(row):
        
#         print(f"{row}", end=" ")
#     print()

# Problem 4 :

# spams = ["crypto","money","cash","win","lottery","winner","millionare","luck"]
# email = input("Paste the email here : ").split(" ")
# for word in email:
#     if word in spams:
#         print("Email flagged as spam.")
#         break   
# else:
#     print("Legitimate email")

# Problem 5 :

# for x in range(1,4):
#     print()
#     for y in range(1,4):
#         print(f"({x},{y})",end=" ")

# Problem 6 :

# num_lst = [1,2,-3,4,-5,6,-7,8,9]
# for num in num_lst:
#     if num <0:
#         print("Validation failed: Negative number found.")
#         break
#     else:
#         continue
# else:
#     print("Validation passed: All numbers are positive.")

# Problem 7 :

# shirts = ["Red", "Blue", "White"]
# pants = ["Jeans", "Khakis"]
# for  shirt in shirts:
#     for pant in pants:
#         print(f"{shirt} Shirt with {pant}",end="")
#         print()

# Problem 8 :

# word = input("Enter a word :")
# for char in word:
#     if word.count(char) >=2:
#         print("The word has duplicate letters.")
#         break
# else:
#     print("The word is a clean isogram (all letters are unique)!")

