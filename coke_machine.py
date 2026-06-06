# amount_due = 50.0
# while amount_due >0:
#     print(f"Amount Due: {amount_due}")
#     insert_coin = float(input("Insert coin :"))
#     if insert_coin in [25, 10, 5]:
#          amount_due -= insert_coin
#     else:
#          print("invalid coin")
#          continue
# if amount_due <0:
#      print(f"Change owned: {-amount_due}")
# else:
#      print("Change owned: 0")


# while True:
#      normal = input("Input:")

#      output = ""
#      for char in normal:
#           if char.lower() not in "aeiou":
#                output +=  char
#      print("Output :", output)
#      continue

# fruits = {
#         "apple": 130,"avocado": 50,"banana": 110,"cantaloupe": 50,"grapefruit": 60,
#         "grapes": 90,"honeydew melon": 50,"kiwifruit": 90,"lemon": 15,"lime": 20,
#         "nectarine": 60,"orange": 80,"peach": 60,"pear": 100,"pineapple": 50,
#         "plums": 70,"strawberries": 50,"sweet cherries": 100,"tangerine": 50,
#         "watermelon": 80}

# f = input("Item :").lower()

# for fruit,calories in fruits.items():
#      if f in fruit:
#           print(f"{fruit} : {calories}")

# def find_top_students():
#      top_students = []
#      grades = { "saumya":[90,86,68,66,95], "sarthak":[90,85,93,96,94],
#                          "parth":[45,43,44,85,83],"krishna":[68,65,42,45,60],
#                          "sarika":[75,74,70,64,55],"priyanshu":[85,83,94,96,88],
#                          "shagun":[85,84,90,94,87], "jitin":[45,60,65,63,80],
#                          "rashi":[75,74,78,79,87],"aastha":[83,85,88,77,76]}
#      threshold = int(input("Enter the threshold: "))

#      for student, grade in grades.items():
#           average = sum(grade) / len(grade)
#           if average >= threshold:
#                top_students.append(student)

#      return top_students
# print(find_top_students())


