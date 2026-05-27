foods = []
prices = []
quantities = []
total = 0

while True:
    food = input("Enter the food you want (q to quit) (r to remove): ")
    if food.lower() == "q":
        break
    elif food.lower() == "r":
        remove = input("Enter the item you want to remove: ")
        if remove in foods:
            index = foods.index(remove)
            foods.pop(index)
            quantities.pop(index)
            prices.pop(index)
            print(f"{remove} has been removed from your cart")
        else:
            print(f"{remove} was not found in your cart")
    else:
        price = float(input(f"Enter the price of {food}: "))
        quantity = int(input(f"Enter the amount of {food}: "))
        foods.append(food)
        prices.append(price * quantity)
        quantities.append(quantity)
print("---YOUR CART---")
for food in foods:
    print(food)
for price in prices:
    total += price
print(f"your total is ${total:.2f}")
print("Do you accept the order?")
answer = input("yes or no: ")
if answer.lower() == "yes":
    print("Thank you for shopping with us!")
else:
    print("Order cancelled")
