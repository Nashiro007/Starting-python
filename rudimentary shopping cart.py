foods = []
prices = []
quantities = []
total = 0

while True:
    food = input("Enter the food you want ( q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}: "))
        quantity = int(input(f"Enter the amount of {food}: "))
        foods.append(food)
        prices.append(price * quantity)
print("---YOUR CART---")
for food in foods:
    print(food)
for price in prices:
    total += price
print(f"your total is ${total}")
print("Do you accept the order?")
answer = input("yes or no: ")
if answer.lower() == "yes":
    print("Thank you for shopping with us!")
else:
    print("Order cancelled")
