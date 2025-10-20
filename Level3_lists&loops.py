# ============================================================================
# PART 1: Creating Lists
# ============================================================================
print("📝 PART 1: Creating Lists")
print("-" * 50)

# TODO 1: Create a list called 'liquids' with these 5 liquid names:
# "Water", "Mercury", "Ethanol", "Nitrogen", "Oxygen"
# Hint: liquids = ["Water", "Mercury", "Ethanol", "Nitrogen", "Oxygen"]


# TODO 2: Create a list called 'freezing_points' with these values:
# 0, -39, -114, -210, -218
# Hint: Make sure the order matches the liquids list!


# TODO 3: Create a list called 'boiling_points' with these values:
# 100, 357, 78, -196, -183


# Testing Part 1
print("\n✅ Testing Part 1...")
try:
    print(f"Number of liquids: {len(liquids)}")
    print(f"First liquid: {liquids[0]}")
    print(f"Last liquid: {liquids[4]}")
    print("✨ Part 1 Complete! You created lists!\n")
except (NameError, IndexError) as e:
    print(f"❌ Not quite! You need to complete TODO 1-3 first.")
    print(f"Error: {e}\n")
    exit()

# ============================================================================
# PART 2: Accessing List Items
# ============================================================================
print("📝 PART 2: Accessing List Items")
print("-" * 50)

# TODO 4: Get the second liquid from the list (Mercury)
# Store it in a variable called 'second_liquid'
# Hint: Remember, lists start at index 0! So second item is index 1


# TODO 5: Get the freezing point of Water (first item in freezing_points)
# Store it in a variable called 'water_freezing'


# TODO 6: Get the boiling point of Ethanol (third item in boiling_points)
# Store it in a variable called 'ethanol_boiling'


# Testing Part 2
print("\n✅ Testing Part 2...")
try:
    print(f"Second liquid: {second_liquid}")
    print(f"Water freezes at: {water_freezing}°C")
    print(f"Ethanol boils at: {ethanol_boiling}°C")
    print("✨ Part 2 Complete! You can access list items!\n")
except (NameError, IndexError) as e:
    print(f"❌ Not quite! You need to complete TODO 4-6 first.")
    print(f"Error: {e}\n")
    exit()

# ============================================================================
# PART 3: For Loops - Displaying All Liquids
# ============================================================================
print("📝 PART 3: For Loops")
print("-" * 50)

print("\nAll liquids in our database:")

# TODO 7: Write a for loop to print each liquid in the liquids list
# Hint:
# for liquid in liquids:
#     print(f"- {liquid}")


# Testing Part 3
print("\n✨ Part 3 Complete! You used a for loop!\n")

# ============================================================================
# PART 4: For Loops with Index - Displaying Complete Information
# ============================================================================
print("📝 PART 4: For Loops with Index")
print("-" * 50)

print("\nComplete liquid database:")

# TODO 8: Use a for loop with range() to print each liquid with its properties
# Hint: Use range(len(liquids)) to get indices 0, 1, 2, 3, 4
# Then access: liquids[i], freezing_points[i], boiling_points[i]
#
# for i in range(len(liquids)):
#     print(f"{i+1}. {liquids[i]}")
#     print(f"   Freezing: {freezing_points[i]}°C")
#     print(f"   Boiling: {boiling_points[i]}°C")


# Testing Part 4
print("\n✨ Part 4 Complete! You used for loops with indices!\n")

# ============================================================================
# PART 5: While Loops - Input Validation
# ============================================================================
print("📝 PART 5: While Loops - User Selection")
print("-" * 50)

# TODO 9: Use a while loop to get a valid liquid choice from the user
# The user should enter a number from 1 to 5
# Keep asking until they enter a valid number
# Store the result in a variable called 'choice'
#
# Hint:
# choice = 0
# while choice < 1 or choice > 5:
#     choice = int(input("Select a liquid (1-5): "))
#     if choice < 1 or choice > 5:
#         print("Invalid! Please enter a number between 1 and 5.")


# Testing Part 5
try:
    selected_liquid = liquids[choice - 1]  # Subtract 1 because lists start at 0
    selected_freezing = freezing_points[choice - 1]
    selected_boiling = boiling_points[choice - 1]

    print(f"\n✅ You selected: {selected_liquid}")
    print(f"Freezing point: {selected_freezing}°C")
    print(f"Boiling point: {selected_boiling}°C")
    print("\n✨ Part 5 Complete! You validated input with while loops!\n")
except (NameError, IndexError, ValueError) as e:
    print(f"❌ Not quite! You need to complete TODO 9 first.")
    print(f"Error: {e}\n")
    exit()

# ============================================================================
# PART 6: Putting It All Together - Temperature Analysis
# ============================================================================
print("📝 PART 6: Complete Analysis")
print("-" * 50)

# TODO 10: Ask the user for a temperature
# Store it in a variable called 'temperature' and convert to float


# TODO 11: Determine the state of the selected liquid at that temperature
# Use if/elif/else like in Level 1
# Store the result in a variable called 'state'


# Testing Part 6
try:
    print(f"\n🎯 ANALYSIS COMPLETE!")
    print("=" * 50)
    print(f"Liquid: {selected_liquid}")
    print(f"Temperature: {temperature}°C")
    print(f"State: {state}")
    print("=" * 50)

    # Additional analysis using a for loop
    print(f"\n🔍 Comparing with all liquids at {temperature}°C:")
    for i in range(len(liquids)):
        if temperature < freezing_points[i]:
            current_state = "Solid"
        elif temperature < boiling_points[i]:
            current_state = "Liquid"
        else:
            current_state = "Gas"
        print(f"  {liquids[i]}: {current_state}")

    print("\n✨ Part 6 Complete! You combined everything!\n")
except NameError as e:
    print(f"❌ Not quite! You need to complete TODO 10-11 first.")
    print(f"Error: {e}\n")
    exit()



# ============================================================================
# 🎉 CONGRATULATIONS!
# ============================================================================
print("=" * 50)
print("🎉 LEVEL 3 COMPLETE! 🎉")
print("=" * 50)
print("\nYou've learned:")
print("✅ How to create and use lists")
print("✅ How to access items by index")
print("✅ How to use for loops to iterate")
print("✅ How to use while loops for validation")
print("✅ How lists work with indices starting at 0")
print("=" * 50)