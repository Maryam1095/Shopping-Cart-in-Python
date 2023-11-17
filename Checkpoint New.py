print("Welcome to Style Haven")
print("Explore our curated collection of shoes, bags, accessories, and clothing.")

shopping_list = []
Products_in_our_inventory = ["shoes", "bags", "accessories", "clothing"]

while True:
    question = int(input("Press 1: Add items to cart\nPress 2: Remove item from cart\nPress 3: View items in cart\nPress 4: Exit\nResponse: "))

    if question == 1:
        if len(shopping_list) == 5:
            print("\nYour cart is full. Remove some items to allow you to shop more\n")
        else:
            item_to_add = input("\nItem: ").strip()
            if item_to_add in Products_in_our_inventory:
                shopping_list.append(item_to_add)
                print("Item added successfully\n")
            else:
                print("Item not available for sale\n")

    elif question == 2:
        if len(shopping_list) == 0:
            print("\nYour cart is empty.\n")
        else:
            item_to_remove = input("\nItem: ").strip().capitalize()
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print("Item removed successfully.\n")
            else:
                print("You cannot remove this item because it is not in your shopping list.\n")

    elif question == 3:
        if len(shopping_list) ==  0:
            print("\nYour cart is empty:")
        else:
            print(f"\nThis is your shopping list: {shopping_list}\n")
    elif question == 4:
        print("Thank you for shopping with Style Haven. Goodbye!")
        break

    else:
        print("Invalid input. Please enter a valid option.\n")
