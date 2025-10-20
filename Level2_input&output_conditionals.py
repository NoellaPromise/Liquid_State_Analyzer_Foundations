# ============================================================================
# PART 3: Input and Output
# ============================================================================
print("📝 PART 3: Input and Output")
print("-" * 50)

# TODO 7: Ask the user for their favorite liquid using input()
# Store the answer in a variable called 'favorite_liquid'
# Hint: favorite_liquid = input("What is your favorite liquid? ")


# TODO 8: Ask the user to enter a temperature (as a number)
# Store it in a variable called 'temperature'
# IMPORTANT: Convert the input to float using float()
# Hint: temperature = float(input("Enter temperature in Celsius: "))


# Testing Part 3 - do not modify!
print("\n✅ Testing Part 3...")
try:
    print(f"\nYou entered:")
    print(f"Favorite liquid: {favorite_liquid}")
    print(f"Temperature: {temperature}°C")
    print("✨ Part 3 Complete! You can get user input!\n")
except NameError as e:
    print(f"❌ Not quite! You need to complete TODO 7-8 first.")
    print(f"Error: {e}\n")
    exit()

# ============================================================================
# PART 4: Basic Operations
# ============================================================================
print("📝 PART 4: Basic Operations")
print("-" * 50)

# TODO 9: Calculate the temperature range (boiling_point - freezing_point)
# Store the result in a variable called 'temperature_range'


# TODO 10: Calculate how far the current temperature is from freezing
# Store the result in a variable called 'degrees_from_freezing'
# Hint: Use temperature - freezing_point


# Testing Part 4 - do not modify!
print("\n✅ Testing Part 4...")
try:
    print(f"Temperature range for water: {temperature_range}°C")
    print(f"Current temperature is {degrees_from_freezing}°C from freezing")
    print("✨ Part 4 Complete! You can do math in Python!\n")
except NameError as e:
    print(f"❌ Not quite! You need to complete TODO 9-10 first.")
    print(f"Error: {e}\n")
    exit()

# ============================================================================
# PART 5: Conditional Statements
# ============================================================================
print("📝 PART 5: Conditional Statements")
print("-" * 50)

print(f"\nAnalyzing {liquid_name} at {temperature}°C...")

# TODO 11: Write an if/elif/else statement to determine the state
# If temperature is less than freezing_point, the state is "Solid"
# Else if temperature is less than boiling_point, the state is "Liquid"
# Else, the state is "Gas"
# Store the result in a variable called 'state'

# Hint: Structure should be:
# if temperature < freezing_point:
#     state = "Solid"
# elif temperature < boiling_point:
#     state = "Liquid"
# else:
#     state = "Gas"


# Testing Part 5 - do not modify!
print("\n✅ Testing Part 5...")
try:
    print(f"\n🎯 RESULT: At {temperature}°C, {liquid_name} is in the {state} state!")

    # Additional analysis
    if state == "Solid":
        print(f"❄️  It needs to warm up {freezing_point - temperature}°C to melt.")
    elif state == "Liquid":
        print(f"💧 It's {temperature - freezing_point}°C above freezing.")
        print(f"💧 It's {boiling_point - temperature}°C below boiling.")
    else:
        print(f"☁️  It's {temperature - boiling_point}°C above boiling!")

    print("\n✨ Part 5 Complete! You mastered conditionals!\n")
except NameError as e:
    print(f"❌ Not quite! You need to complete TODO 11 first.")
    print(f"Error: {e}\n")
    exit()



# ============================================================================
# 🎉 CONGRATULATIONS!
# ============================================================================
print("=" * 50)
print("🎉 LEVEL 2 COMPLETE! 🎉")
print("=" * 50)
print("\nYou've learned:")
print("✅ How to get input from users")
print("✅ How to do basic math operations")
print("✅ How to make decisions with if/elif/else")
print("=" * 50)