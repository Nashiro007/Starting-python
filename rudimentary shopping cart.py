foods = []
prices = []
quantities = []
total = 0
menu = {
    "Burger": 5.99,
    "Pizza": 8.50,
    "Fries": 2.99,
    "Hotdog": 3.50,
    "Sandwich": 4.75,
    "Taco": 2.50,
    "Pasta": 7.25,
    "Salad": 4.00,
    "Ice Cream": 3.25,
    "Soda": 1.50
}
while True:
    for key, value in menu.items():
        print(f"{key:10} : {value:.2f}$")
    food = input("Enter the food you want (q to quit) (r to remove): ")
    if food.lower() == "q":
        break
    elif food.lower() == "r":
        remove = input("Enter the item you want to remove")
        if remove in foods:
            index = foods.index(remove)
            foods.pop(index)
            quantities.pop(index)
            prices.pop(index)
            print(f"{remove} has been removed from your cart")
        else:
            print(f"{remove} was not found in your cart")
    else:
        price = menu[food]
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
