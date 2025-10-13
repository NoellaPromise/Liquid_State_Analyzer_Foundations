#!/usr/bin/env python3
"""
🧪 LIQUID STATE ANALYZER - LEVEL 1 🧪
Learn: Variables, Data Types, Basic Operations, Input/Output, Conditionals

Your Mission: Help scientists determine if water is solid, liquid, or gas!

INSTRUCTIONS:
1. Read each TODO carefully
2. Write your code where it says "Write your code here"
3. Run the program to test
4. Fix any errors and try again!
"""

print("=" * 50)
print("🧪 Welcome to Liquid State Analyzer - Level 1!")
print("=" * 50)

# ============================================
# PART 1: VARIABLES AND DATA TYPES
# ============================================
print("\n📚 PART 1: Setting up our liquid data")
print("Variables store information in your program")

# TODO 1: Create a variable called 'liquid_name' and set it to "Water"
# A variable is like a labeled box that holds information
# Hint: liquid_name = "Water"
# Write your code here:


# TODO 2: Create a variable called 'freezing_point' and set it to 0
# This is the temperature where water freezes (in Celsius)
# Hint: freezing_point = 0
# Write your code here:


# TODO 3: Create a variable called 'boiling_point' and set it to 100
# This is the temperature where water boils (in Celsius)
# Hint: boiling_point = 100
# Write your code here:


# ===== CHECKPOINT 1 =====
# Don't change this - it checks your work!
try:
    print(f"✅ Analyzing: {liquid_name}")
    print(f"   Freezing point: {freezing_point}°C")
    print(f"   Boiling point: {boiling_point}°C")
except NameError as e:
    print(f"❌ ERROR: You need to create the variable: {e}")
    print("   Go back and complete TODOs 1-3!")
    exit()

# ============================================
# PART 2: INPUT AND OUTPUT
# ============================================
print("\n📚 PART 2: Getting temperature from user")
print("input() gets information from the user")
print("print() displays information to the user")

# TODO 4: Use input() to ask the user for a temperature
# Store it in a variable called 'temperature_input'
# Hint: temperature_input = input("Enter temperature in Celsius: ")
# Write your code here:


# TODO 5: Convert temperature_input to a float (decimal number)
# input() always gives you text (string), we need a number!
# Store it in a variable called 'temperature'
# Hint: temperature = float(temperature_input)
# Write your code here:


# ===== CHECKPOINT 2 =====
# Don't change this - it checks your work!
try:
    print(f"🌡️  Temperature entered: {temperature}°C")
except NameError:
    print(
        "❌ ERROR: You need to create 'temperature_input' and 'temperature' variables"
    )
    print("   Complete TODOs 4 and 5!")
    exit()

# ============================================
# PART 3: BASIC OPERATIONS (CALCULATIONS)
# ============================================
print("\n📚 PART 3: Calculating temperature ranges")
print("You can do math with variables using +, -, *, /")

# TODO 6: Calculate how far the temperature is from freezing
# Subtract freezing_point from temperature
# Store the result in 'temp_above_freezing'
# Hint: temp_above_freezing = temperature - freezing_point
# Write your code here:


# TODO 7: Calculate how far the temperature is from boiling
# Subtract temperature from boiling_point
# Store the result in 'temp_below_boiling'
# Hint: temp_below_boiling = boiling_point - temperature
# Write your code here:


# ===== CHECKPOINT 3 =====
# Don't change this - it checks your work!
try:
    print(f"📊 Temperature is {temp_above_freezing}°C above freezing")
    print(f"📊 Temperature is {temp_below_boiling}°C below boiling")
except NameError:
    print("❌ ERROR: Complete TODOs 6 and 7!")
    exit()

# ============================================
# PART 4: CONDITIONAL STATEMENTS
# ============================================
print("\n📚 PART 4: Determining the state of water")
print("if/elif/else helps make decisions in your code")

# TODO 8: Use if/elif/else to determine the state
# Rules:
# - If temperature <= freezing_point: state = "SOLID"
# - Elif temperature >= boiling_point: state = "GAS"
# - Else: state = "LIQUID"
#
# Hint:
# if temperature <= freezing_point:
#     state = "SOLID"
# elif temperature >= boiling_point:
#     state = "GAS"
# else:
#     state = "LIQUID"
#
# Write your code here:


# ===== FINAL CHECKPOINT =====
# Don't change this - it checks your work!
try:
    print("\n" + "=" * 50)
    print("🎉 ANALYSIS COMPLETE!")
    print("=" * 50)
    print(f"🔬 Liquid: {liquid_name}")
    print(f"🌡️  Temperature: {temperature}°C")
    print(f"🏷️  STATE: {state}")
    print("=" * 50)

    # Bonus: Give a fun description
    if state == "SOLID":
        print("❄️  Brrr! The water is frozen into ice!")
    elif state == "GAS":
        print("💨 Whoosh! The water is steam/vapor!")
    else:
        print("💧 Perfect! The water is in liquid form!")

    print("\n✅ LEVEL 1 COMPLETE! Great job! 🎉")
    print("   Next: Try level_2_loops_lists.py")

except NameError:
    print("❌ ERROR: Complete TODO 8 to determine the state!")
    print("   You need to create the 'state' variable using if/elif/else")
    exit()

# ============================================
# TEST YOUR UNDERSTANDING
# ============================================
print("\n" + "=" * 50)
print("🧪 TEST CASES TO TRY:")
print("=" * 50)
print("Run this program again with different temperatures:")
print("  • Try -10  (should be SOLID)")
print("  • Try 25   (should be LIQUID)")
print("  • Try 0    (should be SOLID)")
print("  • Try 100  (should be GAS)")
print("  • Try 150  (should be GAS)")
print("=" * 50)
