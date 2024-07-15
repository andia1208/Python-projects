#SHOPPING CART PROGRAM

foods = []       #I create a list
prices = []      # a list
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")

for food in foods:                   #for every food that is in the list food
    print(food, end=" ")

for price in prices:
    total += price

print()
print(f"Your total is: ${total}")