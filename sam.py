# def greeter():
#     x = input("What is your name? ")
#     print("Hello, " + x + "!")

# count = int(input("enter the range: "))
# for i in range(count):
#     greeter()


# while True:
#     i = int(input("what's the number ?"))
#     if i >= 0 :
#         continue
#     else:
#         break

# while i <= 10:
#     print("Saumya")
#     i += 1

# for i in range(1, 11):
#     print(f" 5 x {i} = {5*i}")

students = {"Saumya": "Delhi",
                "Shivam": "Noida", 
                "Satyam": "Gurgaon",
                "Saksham": "Ghaziabad", 
                "Setu": "Faridabad"      
            }

for index,(student,resident) in enumerate(students.items(), start=1):
    print(  index, student,"lives in",resident, sep = " ")
# def bike_list():
#     bikes = ["Bullet 350", "Hunter 350", "Classic 350",
#             "Thunderbird 350", "Meteor 350", "Electra 350", 
#             "Interceptor 650", "Continental GT 650", "Himalayan 450",
#                 "Royal Enfield Classic/Bullet 650 Twins"]

#     while True:
#         x = input("Do you want the traditional method or the enumerate method? (t/e): ").strip().lower()
#         if x in ("t", "e"):
#             break
#         print("Please enter a valid option among 't' and 'e'.")

#     if x == "t":
#         # iterating a list with index through the traditional method
#         for index in range(len(bikes)):
#             print(f"{index+1}: {bikes[index]}")
#     else:
#         # iterating a list with index through the enumerate method
#         for index, bike in enumerate(bikes, start=1):
#             print(f"{index}: {bike}")

#     show_350 = input("Do you want to see only the bikes with 350? (y/n): ").strip().lower()
#     small_cruisers = []
#     if show_350 == "y":
#         for bike in bikes:
#             if "350" in bike:
#                 small_cruisers.append(bike)

#         if small_cruisers:
#             print("\nBikes with 350:")
#             for bike in small_cruisers:
#                 print(f"- {bike}")
#         else:
#             print("No 350 bikes found.")

#     return small_cruisers

# if __name__ == "__main__":
#     bike_list()