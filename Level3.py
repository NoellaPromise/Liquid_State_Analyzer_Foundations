#!/usr/bin/env python3
"""
🧪 LIQUID STATE ANALYZER - LEVEL 3 🧪
Learn: Functions with def, parameters, return values

Your Mission: Organize code using functions to make it reusable!

INSTRUCTIONS:
1. Complete Levels 1 and 2 first!
2. Functions are like mini-programs that do specific jobs
3. They help organize code and avoid repetition
4. Write your code where indicated
"""

print("=" * 50)
print("🧪 Welcome to Liquid State Analyzer - Level 3!")
print("=" * 50)

# Liquid data (same as Level 2, but with 2 more liquids!)
liquid_names = ["Water", "Ethanol", "Mercury", "Nitrogen", "Oxygen"]
freezing_points = [0, -114.1, -38.8, -210.0, -218.8]
boiling_points = [100, 78.4, 356.7, -195.8, -183.0]

# ============================================
# PART 1: FUNCTIONS WITHOUT PARAMETERS
# ============================================
print("\n📚 PART 1: Creating a function to display liquids")
print("Functions are defined with 'def' keyword")
print("Example: def say_hello():")
print("             print('Hello!')")

# TODO 1: Create a function called 'display_liquids' that shows all liquids
# The function should:
# 1. Print a header: "\n🔬 Available liquids:"
# 2. Use a FOR loop to print each liquid with its number
# 3. Format: "   1. Water"
#
# Hint:
# def display_liquids():
#     print("\n🔬 Available liquids:")
#     for i in range(len(liquid_names)):
#         print(f"   {i+1}. {liquid_names[i]}")
#
# Write your code here:


# ===== CHECKPOINT 1 =====
# Test your function!
try:
    display_liquids()
    print("✅ display_liquids() function works!")
except NameError:
    print("❌ ERROR: Create the display_liquids() function (TODO 1)")
    exit()

# ============================================
# PART 2: FUNCTIONS WITH PARAMETERS
# ============================================
print("\n📚 PART 2: Functions that take input")
print("Parameters let you pass information into functions")
print("Example: def greet(name):")
print("             print(f'Hello {name}!')")

# TODO 2: Create a function called 'get_liquid_info'
# Parameters: liquid_index (a number)
# The function should:
# 1. Get the name from liquid_names[liquid_index]
# 2. Get the freezing point from freezing_points[liquid_index]
# 3. Get the boiling point from boiling_points[liquid_index]
# 4. Return all three as a tuple: (name, freezing, boiling)
#
# Hint:
# def get_liquid_info(liquid_index):
#     name = liquid_names[liquid_index]
#     freezing = freezing_points[liquid_index]
#     boiling = boiling_points[liquid_index]
#     return (name, freezing, boiling)
#
# Write your code here:


# ===== CHECKPOINT 2 =====
# Test your function!
try:
    test_info = get_liquid_info(0)
    print(f"✅ Test: {test_info[0]} has freezing point {test_info[1]}°C")
except NameError:
    print("❌ ERROR: Create the get_liquid_info() function (TODO 2)")
    exit()

# ============================================
# PART 3: FUNCTIONS THAT RETURN VALUES
# ============================================
print("\n📚 PART 3: Functions that calculate and return results")
print("'return' sends a value back from the function")
print("Example: def add(a, b):")
print("             return a + b")

# TODO 3: Create a function called 'determine_state'
# Parameters: temperature, freezing_point, boiling_point
# The function should:
# 1. Check if temperature <= freezing_point, return "SOLID"
# 2. Check if temperature >= boiling_point, return "GAS"
# 3. Otherwise, return "LIQUID"
#
# Hint:
# def determine_state(temperature, freezing_point, boiling_point):
#     if temperature <= freezing_point:
#         return "SOLID"
#     elif temperature >= boiling_point:
#         return "GAS"
#     else:
#         return "LIQUID"
#
# Write your code here:


# ===== CHECKPOINT 3 =====
# Test your function!
try:
    test_state = determine_state(50, 0, 100)
    if test_state == "LIQUID":
        print(f"✅ Test passed! Water at 50°C is {test_state}")
    else:
        print(f"⚠️  Test result: {test_state} - check your logic!")
except NameError:
    print("❌ ERROR: Create the determine_state() function (TODO 3)")
    exit()

# ============================================
# PART 4: FUNCTIONS WITH MULTIPLE PARAMETERS
# ============================================
print("\n📚 PART 4: More complex functions")
print("Functions can call other functions!")
print("This makes your code organized and easy to read")

# TODO 4: Create a function called 'analyze_liquid'
# Parameters: liquid_name, temperature, freezing_point, boiling_point
# The function should:
# 1. Call determine_state() to get the state
# 2. Print a complete analysis report with:
#    - Header line with "="
#    - "🎉 ANALYSIS COMPLETE!"
#    - Liquid name
#    - Temperature
#    - STATE
#    - Footer line with "="
#
# Hint:
# def analyze_liquid(liquid_name, temperature, freezing_point, boiling_point):
#     state = determine_state(temperature, freezing_point, boiling_point)
#     print("\n" + "=" * 50)
#     print("🎉 ANALYSIS COMPLETE!")
#     print("=" * 50)
#     print(f"🔬 Liquid: {liquid_name}")
#     print(f"🌡️  Temperature: {temperature}°C")
#     print(f"🏷️  STATE: {state}")
#     print("=" * 50)
#
# Write your code here:


# ===== CHECKPOINT 4 =====
# Test your function!
try:
    print("\n🧪 Test Analysis:")
    analyze_liquid("Water", 25, 0, 100)
    print("✅ analyze_liquid() function works!")
except NameError:
    print("❌ ERROR: Create the analyze_liquid() function (TODO 4)")
    exit()

# ============================================
# PART 5: FUNCTIONS FOR INPUT VALIDATION
# ============================================
print("\n📚 PART 5: Input validation function")
print("Functions can handle repetitive tasks like getting valid input")

# TODO 5: Create a function called 'get_valid_choice'
# Parameters: min_value, max_value
# The function should:
# 1. Use a WHILE loop to keep asking until valid input
# 2. Ask user to enter a number between min_value and max_value
# 3. Convert input to integer
# 4. Check if it's valid (between min and max)
# 5. If invalid, print error and loop again
# 6. Return the valid choice
#
# Hint:
# def get_valid_choice(min_value, max_value):
#     choice = 0
#     while choice < min_value or choice > max_value:
#         choice_input = input(f"Enter a number ({min_value}-{max_value}): ")
#         choice = int(choice_input)
#         if choice < min_value or choice > max_value:
#             print(f"❌ Please enter a number between {min_value} and {max_value}")
#     return choice
#
# Write your code here:


# ===== CHECKPOINT 5 =====
# Test will happen in Part 6!
print("✅ Move on to Part 6 to test all functions together!")

# ============================================
# PART 6: PUTTING IT ALL TOGETHER
# ============================================
print("\n📚 PART 6: Complete program using all functions")
print("Now let's use ALL your functions to create the analyzer!")

# TODO 6: Use all your functions to create the complete analyzer
# Steps:
# 1. Call display_liquids() to show options
# 2. Use get_valid_choice(1, len(liquid_names)) to get user choice
# 3. Use get_liquid_info(choice - 1) to get liquid data
#    Store in variables: name, freezing, boiling
# 4. Get temperature from user (use input and float)
# 5. Call analyze_liquid(name, temperature, freezing, boiling)
#
# Hint:
# display_liquids()
# choice = get_valid_choice(1, len(liquid_names))
# name, freezing, boiling = get_liquid_info(choice - 1)
# temperature = float(input("\n🌡️  Enter temperature in Celsius: "))
# analyze_liquid(name, temperature, freezing, boiling)
#
# Write your code here:


# ===== FINAL CHECKPOINT =====
print("\n" + "=" * 50)
print("✅ If you see analysis results above, LEVEL 3 COMPLETE! 🎉")
print("   Next: Try level_4_debugging.py")
print("=" * 50)

# ============================================
# TEST YOUR UNDERSTANDING
# ============================================
print("\n" + "=" * 50)
print("🧪 UNDERSTAND YOUR FUNCTIONS:")
print("=" * 50)
print("You created 5 functions:")
print("  1. display_liquids() - Shows all liquids")
print("  2. get_liquid_info(index) - Gets data for one liquid")
print("  3. determine_state(temp, freeze, boil) - Calculates state")
print("  4. analyze_liquid(name, temp, freeze, boil) - Prints report")
print("  5. get_valid_choice(min, max) - Gets valid input")
print("\nFunctions help organize code and avoid repetition!")
print("=" * 50)

# ============================================
# BONUS CHALLENGE (Optional)
# ============================================
print("\n🌟 BONUS CHALLENGE:")
print("Create a function called 'run_multiple_analyses()' that:")
print("  • Uses a WHILE loop")
print("  • Lets users analyze multiple liquids")
print("  • Asks if they want to continue after each analysis")
print("  • Stops when they say 'no'")
print("\nAsk your teacher for help if you want to try this!")