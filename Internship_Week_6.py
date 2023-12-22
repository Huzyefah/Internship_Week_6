# Constants
COST_CEMENT = 3
COST_GRAVEL = 2
COST_SAND = 2
DISCOUNT_PACK = {'C': 1, 'S': 2, 'G': 2, 'price': 10}

# Task 1 - Check the contents and weight of a single sack
def check_single_sack():
    sack_contents = input("Enter the contents of the sack (C for cement, G for gravel, S for sand): ").upper()
    sack_weight = float(input("Enter the weight of the sack in kilograms: "))

    # Check contents
    if sack_contents not in ['C', 'G', 'S']:
        print("Error: Invalid contents. Sack rejected.")
        return

    # Check weight
    if (sack_contents == 'C' and not (24.9 < sack_weight < 25.1)) or \
       ((sack_contents == 'G' or sack_contents == 'S') and not (49.9 < sack_weight < 50.1)):
        print("Error: Invalid weight. Sack rejected.")
        return

    print(f"Sack accepted! Contents: {sack_contents}, Weight: {sack_weight} kg")


# Task 2 - Check a customer’s order for delivery
def check_customer_order():
    total_weight = 0
    rejected_sacks = 0

    num_cement = int(input("Enter the number of sacks of cement: "))
    num_gravel = int(input("Enter the number of sacks of gravel: "))
    num_sand = int(input("Enter the number of sacks of sand: "))

    for _ in range(num_cement):
        result = check_single_sack()
        if result is None:
            total_weight += 25

    for _ in range(num_gravel):
        result = check_single_sack()
        if result is None:
            total_weight += 50

    for _ in range(num_sand):
        result = check_single_sack()
        if result is None:
            total_weight += 50

    print(f"Total weight of the order: {total_weight} kg")
    print(f"Number of rejected sacks: {rejected_sacks}")


# Task 3 - Calculate the price for a customer’s order
def calculate_order_price():
    regular_price = 0
    num_discount_packs = 0

    # Calculate regular price
    num_cement = int(input("Enter the number of sacks of cement: "))
    num_gravel = int(input("Enter the number of sacks of gravel: "))
    num_sand = int(input("Enter the number of sacks of sand: "))

    regular_price += num_cement * COST_CEMENT
    regular_price += num_gravel * COST_GRAVEL
    regular_price += num_sand * COST_SAND

    # Check for discount packs
    while num_cement >= DISCOUNT_PACK['C'] and num_sand >= DISCOUNT_PACK['S'] and num_gravel >= DISCOUNT_PACK['G']:
        num_cement -= DISCOUNT_PACK['C']
        num_sand -= DISCOUNT_PACK['S']
        num_gravel -= DISCOUNT_PACK['G']
        num_discount_packs += 1

    # Calculate discounted price
    discount_price = num_discount_packs * DISCOUNT_PACK['price']
    final_price = regular_price - discount_price

    print(f"Regular price for the order: ${regular_price}")
    print(f"Number of discount packs applied: {num_discount_packs}")
    print(f"Discounted price for the order: ${final_price} (You saved ${discount_price})")


# Test the program
check_single_sack()
check_customer_order()
calculate_order_price()
