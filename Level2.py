#!/usr/bin/env python3
"""
🧪 LIQUID STATE ANALYZER - LEVEL 2 🧪
Learn: Lists, Loops (for and while)

Your Mission: Analyze MULTIPLE liquids, not just water!

INSTRUCTIONS:
1. Complete Level 1 first!
2. Read each TODO carefully
3. Write your code where indicated
4. Run and test your program
"""

print("=" * 50)
print("🧪 Welcome to Liquid State Analyzer - Level 2!")
print("=" * 50)

# ============================================
# PART 1: WORKING WITH LISTS
# ============================================
print("\n📚 PART 1: Creating lists of liquids")
print("Lists store multiple items in one variable")
print("Example: colors = ['red', 'blue', 'green']")

# TODO 1: Create a list called 'liquid_names' with these liquids:
# "Water", "Ethanol", "Mercury"
# Hint: liquid_names = ["Water", "Ethanol", "Mercury"]
# Write your code here:


# TODO 2: Create a list called 'freezing_points' with these values:
# 0, -114.1, -38.8
# (These match the liquids above in the same order)
# Hint: freezing_points = [0, -114.1, -38.8]
# Write your code here:


# TODO 3: Create a list called 'boiling_points' with these values:
# 100, 78.4, 356.7
# Hint: boiling_points = [100, 78.4, 356.7]
# Write your code here:


# ===== CHECKPOINT 1 =====
# Don't change this - it checks your work!
try:
    print("✅ Available liquids:")
    for i in range(len(liquid_names)):
        print(f"   {i+1}. {liquid_names[i]} (Freezes: {freezing_points[i]}°C, Boils: {boiling_points[i]}°C)")
except NameError as e:
    print(f"❌ ERROR: You need to create the lists: {e}")
    print("   Complete TODOs 1, 2, and 3!")
    exit()

# ============================================
# PART 2: FOR LOOPS - Displaying Options
# ============================================
print("\n📚 PART 2: Using FOR loops to show options")
print("FOR loops repeat code for each item in a list")
print("Example: for i in range(3): print(i)  → prints 0, 1, 2")

print("\n🔬 Choose a liquid to analyze:")

# TODO 4: Use a FOR loop to print each liquid with its number
# Example output should look like:
#   1. Water
#   2. Ethanol
#   3. Mercury
#
# Hint: 
# for i in range(len(liquid_names)):
#     print(f"{i+1}. {liquid_names[i]}")
#
# Write your code here:


# ============================================
# PART 3: WHILE LOOPS - Getting Valid Input
# ============================================
print("\n📚 PART 3: Using WHILE loops for input validation")
print("WHILE loops repeat until a condition is met")
print("Perfect for making sure user enters valid data!")

# TODO 5: Create a WHILE loop that keeps asking for a choice until valid
# The choice should be between 1 and the length of liquid_names
# 
# Steps:
# 1. Set choice = 0 (start with invalid value)
# 2. Create while loop: while choice < 1 or choice > len(liquid_names):
# 3. Inside loop: ask for input and convert to int
# 4. If invalid, print error message
#
# Hint: 
# choice = 0
# while choice < 1 or choice > len(liquid_names):
#     choice_input = input("Enter liquid number: ")
#     choice = int(choice_input)
#     if choice < 1 or choice > len(liquid_names):
#         print("❌ Invalid choice! Try again.")
#
# Write your code here:
choice = 0


# ===== CHECKPOINT 2 =====
# Don't change this - it checks your work!
if choice == 0:
    print("❌ ERROR: Complete TODO 5 to get user's choice!")
    print("   Your WHILE loop needs to ask for input and validate it.")
    exit()

# ============================================
# PART 4: ACCESSING LIST ITEMS
# ============================================
print("\n📚 PART 4: Getting data from lists")
print("Access list items using square brackets: mylist[0]")
print("IMPORTANT: Python lists start at index 0!")
print("So if user chooses 1, we need index 0")

# TODO 6: Get the selected liquid's name from the liquid_names list
# Remember: Python lists start at index 0, so subtract 1 from choice
# Store it in 'selected_liquid'
# Hint: selected_liquid = liquid_names[choice - 1]
# Write your code here:


# TODO 7: Get the freezing point from freezing_points list
# Store it in 'selected_freezing'
# Hint: selected_freezing = freezing_points[choice - 1]
# Write your code here:


# TODO 8: Get the boiling point from boiling_points list
# Store it in 'selected_boiling'
# Hint: selected_boiling = boiling_points[choice - 1]
# Write your code here:


# ===== CHECKPOINT 3 =====
# Don't change this - it checks your work!
try:
    print(f"\n✅ You selected: {selected_liquid}")
    print(f"   Freezing point: {selected_freezing}°C")
    print(f"   Boiling point: {selected_boiling}°C")
except NameError:
    print("❌ ERROR: Complete TODOs 6, 7, and 8!")
    print("   You need to get the selected liquid's data from the lists.")
    exit()

# ============================================
# PART 5: PUTTING IT ALL TOGETHER
# ============================================
print("\n📚 PART 5: Complete analysis")
print("Now use what you learned in Level 1 to analyze the selected liquid!")

# Get temperature from user
temperature = float(input("\n🌡️  Enter temperature in Celsius: "))

# TODO 9: Use if/elif/else to determine state
# Same as Level 1, but use selected_freezing and selected_boiling
# instead of hardcoded 0 and 100
#
# Hint:
# if temperature <= selected_freezing:
#     state = "SOLID"
# elif temperature >= selected_boiling:
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
    print(f"🔬 Liquid: {selected_liquid}")
    print(f"🌡️  Temperature: {temperature}°C")
    print(f"🏷️  STATE: {state}")
    print("=" * 50)
    
    if state == "SOLID":
        print(f"❄️  {selected_liquid} is frozen solid!")
    elif state == "GAS":
        print(f"💨 {selected_liquid} has turned to gas!")
    else:
        print(f"💧 {selected_liquid} is in liquid form!")
    
    print("\n✅ LEVEL 2 COMPLETE! Awesome! 🎉")
    print("   Next: Try level_3_functions.py")
    
except NameError:
    print("❌ ERROR: Complete TODO 9!")
    print("   You need to determine the state using if/elif/else")
    exit()

# ============================================
# TEST YOUR UNDERSTANDING
# ============================================
print("\n" + "=" * 50)
print("🧪 TEST CASES TO TRY:")
print("=" * 50)
print("Run this program again and try:")
print("  • Water at -5°C (should be SOLID)")
print("  • Water at 50°C (should be LIQUID)")
print("  • Water at 150°C (should be GAS)")
print("  • Ethanol at -120°C (should be SOLID)")
print("  • Mercury at 0°C (should be LIQUID - it doesn't freeze until -38.8!)")
print("=" * 50)

# ============================================
# BONUS CHALLENGE (Optional)
# ============================================
print("\n🌟 BONUS CHALLENGE:")
print("Can you modify the code to analyze MULTIPLE temperatures?")
print("Hint: Add another WHILE loop that asks if user wants to continue!")
print("Ask your teacher for help if you want to try this!")