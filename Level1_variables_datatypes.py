"""
INSTRUCTIONS:
Complete each TODO section below. Run the program after each level
to test your code. The program will tell you if you're on the right track!
"""

# ============================================================================
# PART 1: Creating Variables
# ============================================================================
print("📝 PART 1: Creating Variables")
print("-" * 50)

# TODO 1: Create a variable called 'liquid_name' and set it to "Water"
# Hint: Use the = sign to assign a value to a variable
# Example: my_variable = "some value"
# Write your code here:


# TODO 2: Create a variable called 'freezing_point' and set it to 0
# Hint: This is a number (integer), so don't use quotes
# Write your code here:

# TODO 3: Create a variable called 'boiling_point' and set it to 100.0
# Hint: This is a decimal number (float), notice the .0
# Write your code here:


# Testing Part 1 - do not modify!
print("\n✅ Testing Part 1...")
try:
    print(f"Liquid: {liquid_name}")
    print(f"Freezing point: {freezing_point}°C")
    print(f"Boiling point: {boiling_point}°C")
    print("✨ Part 1 Complete! Great job creating variables!\n")
except NameError as e:
    print(f"❌ Not quite! You need to complete TODO 1-3 first.")
    print(f"Error: {e}\n")
    exit()

# ============================================================================
# PART 2: Understanding Data Types
# ============================================================================
print("📝 PART 2: Understanding Data Types")
print("-" * 50)

# TODO 4: Create a variable 'student_name' with YOUR name as a string


# TODO 5: Create a variable 'current_grade' and set it to 8 (your grade)(integer)


# TODO 6: Create a variable 'python_version' and set it to 3.11 (float)


# Testing Part 2 - do not modify!
print("\n✅ Testing Part 2...")
try:
    print(f"Student: {student_name}")
    print(f"Grade: {current_grade}")
    print(f"Python version: {python_version}")
    print("✨ Part 2 Complete! You understand data types!\n")
except NameError as e:
    print(f"❌ Not quite! You need to complete TODO 4-6 first.")
    print(f"Error: {e}\n")
    exit()



# ============================================================================
# 🎉 CONGRATULATIONS!
# ============================================================================
print("=" * 50)
print("🎉 LEVEL 1 COMPLETE! 🎉")
print("=" * 50)
print("\nYou've learned:")
print("✅ How to create and use variables")
print("✅ Different data types (string, int, float)")
print("=" * 50)