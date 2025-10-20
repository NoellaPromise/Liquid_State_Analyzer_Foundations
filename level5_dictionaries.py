
# ============================================================================
# PART 1: Creating Dictionaries
# ============================================================================
print("📝 PART 1: Your First Dictionary")
print("-" * 50)

# TODO 1: Create a dictionary called 'water' with these key-value pairs:
# "name": "Water"
# "freezing": 0
# "boiling": 100
# Use curly braces {} and colons between keys and values
# Hint:
# water = {
#     "name": "Water",
#     "freezing": 0,
#     "boiling": 100
# }


# Testing Part 1
print("\n✅ Testing Part 1...")
try:
    print(f"Dictionary created: {water}")
    print("✨ Great! You created a dictionary!\n")
except NameError as e:
    print(f"❌ Not quite! Complete TODO 1 first.")
    print(f"Error: {e}\n")
    exit()

# ============================================================================
# PART 2: Accessing Dictionary Values
# ============================================================================
print("📝 PART 2: Getting Values from Dictionaries")
print("-" * 50)

# TODO 2: Get the liquid name from the water dictionary
# Use square brackets with the key name
# Store it in a variable called 'liquid_name'
# Hint: liquid_name = water["name"]


# TODO 3: Get the freezing point from the water dictionary
# Store it in a variable called 'freezing_point'
# Hint: freezing_point = water["freezing"]


# Testing Part 2
print("\n✅ Testing Part 2...")
try:
    print(f"Liquid: {liquid_name}")
    print(f"Freezes at: {freezing_point}°C")
    print("✨ Perfect! You accessed dictionary values!\n")
except (NameError, KeyError) as e:
    print(f"❌ Not quite! Complete TODO 2-3 first.")
    print(f"Error: {e}\n")
    exit()

# ============================================================================
# PART 3: Adding to Dictionaries
# ============================================================================
print("📝 PART 3: Modifying Dictionaries")
print("-" * 50)

# TODO 4: Add a new key-value pair to the water dictionary
# Key: "state_at_25"  Value: "Liquid"
# Hint: water["state_at_25"] = "Liquid"


# Testing Part 3
print("\n✅ Testing Part 3...")
try:
    print(f"Water at 25°C: {water['state_at_25']}")
    print("✨ Excellent! You added to a dictionary!\n")
except KeyError as e:
    print(f"❌ Not quite! Complete TODO 4 first.")
    print(f"Error: {e}\n")
    exit()

# ============================================================================
# PART 4: Multiple Dictionaries
# ============================================================================
print("📝 PART 4: Working with Multiple Dictionaries")
print("-" * 50)

# TODO 5: Create a dictionary called 'mercury' with these properties:
# "name": "Mercury"
# "freezing": -39
# "boiling": 357
# Hint: Follow the same pattern as the water dictionary


# Testing Part 4
print("\n✅ Testing Part 4...")
try:
    print(f"\nLiquid: {mercury['name']}")
    print(f"Freezing: {mercury['freezing']}°C")
    print(f"Boiling: {mercury['boiling']}°C")
    print("✨ Great! You created another dictionary!\n")
except (NameError, KeyError) as e:
    print(f"❌ Not quite! Complete TODO 5 first.")
    print(f"Error: {e}\n")
    exit()

# ============================================================================
# PART 5: Looping Through Dictionaries
# ============================================================================
print("📝 PART 5: Looping Through Dictionary Keys")
print("-" * 50)

print("\nWater properties:")

# TODO 6: Loop through all keys in the water dictionary
# Print each key and its value
# Hint:
# for key in water:
#     print(f"{key}: {water[key]}")


print("\n✨ Amazing! You looped through a dictionary!\n")

# ============================================================================
# BONUS: List of Dictionaries
# ============================================================================
print("📝 BONUS: List of Dictionaries")
print("-" * 50)

# Create a list of liquid dictionaries
liquids = [
    {"name": "Water", "freezing": 0, "boiling": 100},
    {"name": "Mercury", "freezing": -39, "boiling": 357},
    {"name": "Ethanol", "freezing": -114, "boiling": 78}
]

print("\nAll liquids:")
for liquid in liquids:
    print(f"- {liquid['name']}: {liquid['freezing']}°C to {liquid['boiling']}°C")

# Test with user input
temperature = float(input("\nEnter a temperature to test: "))

print(f"\nAt {temperature}°C:")
for liquid in liquids:
    if temperature < liquid["freezing"]:
        state = "Solid"
    elif temperature < liquid["boiling"]:
        state = "Liquid"
    else:
        state = "Gas"
    print(f"  {liquid['name']}: {state}")

# ============================================================================
# 🎉 CONGRATULATIONS!
# ============================================================================
print("\n" + "=" * 50)
print("🎉 LEVEL 5 COMPLETE! 🎉")
print("=" * 50)
print("\nYou've learned:")
print("✅ How to create dictionaries with {}")
print("✅ How to access values with keys")
print("✅ How to add and modify dictionary items")
print("✅ How to loop through dictionaries")
print("✅ How to use lists of dictionaries")
print("=" * 50)