# Practice series

# Exercise 1: Shopping cart program

# my_shop_dict = {
#     "Soap": 3.50,
#     "Bread": 1.90,
#     "Milk": 5.50,
#     "Oil": 10.50
# }

# user_total_cost = []
# final_bill = None
# user_cart = {}

# is_shopping = True

# while is_shopping:
#     print("-----------------Shop Items-------------------")
#     for key, value in my_shop_dict.items():
#         print(f"{key} : ${value:.2f}")
#     user_choice = input("Enter the name of the product to purchase(q to quit): ").strip().capitalize()
#     if user_choice == "Q":
#         print("Exiting program, thank you for shopping, come again.")
#         is_shopping = False
#     elif user_choice not in my_shop_dict:
#         print("Item not found")
#         continue
#     elif user_choice in my_shop_dict:
#         print(f"'{user_choice}' successfully added to cart")
#         user_total_cost.append(my_shop_dict[user_choice])
#         user_cart[user_choice] = my_shop_dict[user_choice]
#         print("------------Your Cart-------------")
#         for items, price in user_cart.items():
#             print(items, end=", ")
#         print()
#         continue_shopping = input("Do you want to continue shopping? (y/n): ").strip().lower()
#         if not continue_shopping == "y":
#             print("Exiting program, thank you for shopping, come again.")
#             is_shopping = False
#         else:
#             continue

# final_bill = sum(user_total_cost)

# if final_bill:
#     print("Thanks for shopping with us:")
#     print("---------------Your Order-----------------")
#     for item, price in user_cart.items():
#         print(f"{item} : ${price:.2f}")
#     print(f"Total cost is: ${final_bill:.2f}")


# Exercise 2: 2D grid printer
total_sum = 0
for row in range(1, 4):
    for col in range(1, 4):
        total_sum += col
        print(col, end=" ")
    print()

print(f"Total Sum: {total_sum}")


# Exercise 3: Filter with sets

# list_1 = [1, 1, 3, 4, 5, 1, 2, 5, 5, 9]
# list_2 = [1, 2, 3, 6, 7, 8, 10, 4, 6, 8]

# set_1 = set(list_1)
# set_2 = set(list_2)
# # print(list_1)
# # print(list_2)

# for num in set_1 & set_2:
#     if (num % 2 == 0):
#         print(num, end=", ")
# print()

# # Exercise 2 Fixed: 2D Grid Printer
# grid = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# total_sum = 0

# print("--- 2D Grid ---")
# # Outer loop goes through each row
# for row in grid:
#     # Inner loop goes through each item in the row
#     for num in row:
#         print(num, end=" ")
#         total_sum += num
#     print() # New line after each row

# print(f"Total Sum: {total_sum}")

