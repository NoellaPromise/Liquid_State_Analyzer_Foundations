#!/usr/bin/env python3
"""
🧪 LIQUID STATE ANALYZER - LEVEL 4 🧪
Learn: Debugging - Finding and Fixing Errors

Your Mission: This program has 10 BUGS! Find and fix them all!

INSTRUCTIONS:
1. Complete Levels 1, 2, and 3 first!
2. This code has intentional bugs
3. Read error messages carefully
4. Fix ONE bug at a time
5. Test after each fix
6. Keep track of bugs you've fixed

🐛 = Bug marker - these comments show where bugs are!
"""

print("=" * 50)
print("🧪 Welcome to Liquid State Analyzer - Level 4!")
print("🐛 DEBUG MODE: Find and fix 10 bugs!")
print("=" * 50)

# Liquid data
liquid_names = ["Water", "Ethanol", "Mercury"]
freezing_points = [0, -114.1, -38.8]
boiling_points = [100, 78.4, 356.7]

# ============================================
# BUG SECTION 1: SYNTAX ERRORS
# ============================================
print("\n📚 BUG SECTION 1: Syntax Errors")
print("Look for missing colons, wrong indentation, typos")
print("Syntax errors prevent the code from running at all!")

# 🐛 BUG 1: Missing colon at the end of function definition
# ERROR TYPE: SyntaxError
# HINT: Function definitions need a colon (:) at the end
def display_liquids()
    print("\n🔬 Available liquids:")
    for i in range(len(liquid_names)):
        print(f"   {i+1}. {liquid_names[i]}")

# 🐛 BUG 2: Wrong indentation in if statement
# ERROR TYPE: IndentationError
# HINT: The return statement should be indented inside the if block
def determine_state(temperature, freezing, boiling):
    if temperature <= freezing:
        return "SOLID"
    elif temperature >= boiling:
        return "GAS"
    else:
        return "LIQUID"

# ============================================
# BUG SECTION 2: LOGIC ERRORS
# ============================================
print("\n📚 BUG SECTION 2: Logic Errors")
print("The code runs but gives wrong results!")
print("Check comparison operators and conditions carefully")

# 🐛 BUG 3: Wrong comparison operator
# ERROR TYPE: Logic Error
# HINT: Boiling happens when temperature is >= boiling point (not just >)
# Current code says temperature must be ABOVE boiling, but it should include the boiling point itself
def is_boiling(temperature, boiling_point):
    if temperature > boiling_point:  # Should be >=
        return True
    else:
        return False

# 🐛 BUG 4: Wrong list index
# ERROR TYPE: Logic Error (IndexError when choice=1)
# HINT: Python lists start at 0! If user chooses 1, we want index 0
def get_liquid_name(choice):
    # User chooses 1, 2, or 3 but we need index 0, 1, or 2
    return liquid_names[choice]  # Should be choice - 1

# 🐛 BUG 5: Swapped return values
# ERROR TYPE: Logic Error
# HINT: Function should return (freezing, boiling) in that order
def get_temperature_range(freezing, boiling):
    # Should return freezing first, then boiling
    return (boiling, freezing)  # Wrong order!

# ============================================
# BUG SECTION 3: VARIABLE NAME ERRORS
# ============================================
print("\n📚 BUG SECTION 3: Variable Name Errors")
print("Typos in variable names cause NameError")
print("Python is case-sensitive: 'temp' is not the same as 'Temp'")

# 🐛 BUG 6: Variable name typo
# ERROR TYPE: NameError
# HINT: Look for 'temprature' - should be 'temperature'
def analyze_liquid(liquid_name, temperature, freezing, boiling):
    state = determine_state(temperature, freezing, boiling)
    print(f"\n🔬 Analyzing {liquid_name} at {temprature}°C")  # Typo!
    print(f"🏷️  STATE: {state}")

# ============================================
# BUG SECTION 4: STRING FORMATTING ERRORS
# ============================================
print("\n📚 BUG SECTION 4: String Formatting Errors")
print("f-strings need the 'f' before the quote!")

# 🐛 BUG 7: Missing 'f' in f-string
# ERROR TYPE: Logic Error (prints literal {name} instead of value)
# HINT: Put 'f' before the opening quote
def print_liquid_info(name, freezing, boiling):
    print("Liquid: {name}")  # Missing f!
    print(f"Freezing: {freezing}°C")
    print(f"Boiling: {boiling}°C")

# ============================================
# BUG SECTION 5: TYPE ERRORS
# ============================================
print("\n📚 BUG SECTION 5: Type Errors")
print("Using wrong data types causes errors")

# 🐛 BUG 8: Forgot to convert input to integer
# ERROR TYPE: TypeError (can't compare string with int)
# HINT: Use int() to convert the input string to a number
def get_user_choice():
    choice = input("Enter liquid number (1-3): ")
    # Need to convert to int before returning!
    return choice  # Should be: return int(choice)

# 🐛 BUG 9: Index out of range in loop
# ERROR TYPE: IndexError
# HINT: range(len(list) + 1) goes too far! Should be range(len(list))
def show_all_liquids():
    for i in range(len(liquid_names) + 1):  # Goes one too far!
        print(f"{i+1}. {liquid_names[i]}")

# 🐛 BUG 10: Using string as list index
# ERROR TYPE: TypeError
# HINT: List indices must be integers, not strings
# Need to find the index of the name first
def get_freezing_by_name(name):
    # Can't use a string (name) as a list index!
    # Should find the index first: index = liquid_names.index(name)
    freezing = freezing_points[name]  # Wrong!
    return freezing

# ============================================
# DEBUGGING TIPS
# ============================================
print("\n" + "=" * 50)
print("🔍 DEBUGGING TIPS:")
print("=" * 50)
print("1. Read error messages - they tell you the line number!")
print("2. Fix ONE bug at a time, then test")
print("3. Use print() statements to check variable values")
print("4. Check for:")
print("   • Missing colons (:) after if, for, while, def")
print("   • Wrong indentation (all code in a block must line up)")
print("   • Typos in variable names")
print("   • Missing 'f' in f-strings")
print("   • List indices (remember: start at 0!)")
print("   • Converting input() to int or float")
print("=" * 50)

# ============================================
# HOW TO DEBUG THIS PROGRAM
# ============================================
print("\n" + "=" * 50)
print("📝 YOUR DEBUGGING PROCESS:")
print("=" * 50)
print("1. Run this program")
print("2. Python will stop at the first error")
print("3. Read the error message carefully")
print("4. Find the bug marker (🐛) near that line")
print("5. Fix the bug")
print("6. Save and run again")
print("7. Repeat until all bugs are fixed!")
print("\n💡 TIP: Keep track of which bugs you've fixed!")
print("=" * 50)

# ============================================
# TEST SECTION (RUN THIS AFTER FIXING BUGS)
# ============================================
def run_tests():
    """Tests to verify all bugs are fixed"""
    print("\n" + "=" * 50)
    print("🧪 RUNNING TESTS...")
    print("=" * 50)
    
    bugs_fixed = 0
    total_bugs = 10
    
    # Test 1: display_liquids (Bug 1 - syntax error)
    try:
        display_liquids()
        bugs_fixed += 1
        print("✅ Bug 1 fixed: display_liquids() works!")
    except:
        print("❌ Bug 1: display_liquids() still has a syntax error")
    
    # Test 2: determine_state (Bug 2 - indentation)
    try:
        result = determine_state(50, 0, 100)
        if result == "LIQUID":
            bugs_fixed += 1
            print("✅ Bug 2 fixed: determine_state() works!")
        else:
            print("❌ Bug 2: determine_state() has logic issues")
    except:
        print("❌ Bug 2: determine_state() still has errors")
    
    # Test 3: is_boiling logic (Bug 3 - wrong operator)
    try:
        if is_boiling(100, 100) == True and is_boiling(99, 100) == False:
            bugs_fixed += 1
            print("✅ Bug 3 fixed: is_boiling() logic correct!")
        else:
            print("❌ Bug 3: is_boiling() logic still wrong (hint: use >= not >)")
    except:
        print("❌ Bug 3: is_boiling() still has errors")
    
    # Test 4: get_liquid_name indexing (Bug 4)
    try:
        name = get_liquid_name(1)
        if name == "Water":
            bugs_fixed += 1
            print("✅ Bug 4 fixed: get_liquid_name() indexing correct!")
        else:
            print(f"❌ Bug 4: get_liquid_name(1) returned '{name}', expected 'Water'")
            print("   HINT: Lists start at 0, so choice 1 needs index 0")
    except:
        print("❌ Bug 4: get_liquid_name() still has errors")
    
    # Test 5: get_temperature_range order (Bug 5)
    try:
        freezing, boiling = get_temperature_range(0, 100)
        if freezing == 0 and boiling == 100:
            bugs_fixed += 1
            print("✅ Bug 5 fixed: get_temperature_range() returns correct order!")
        else:
            print("❌ Bug 5: get_temperature_range() values are swapped")
    except:
        print("❌ Bug 5: get_temperature_range() still has errors")
    
    # Test 6: analyze_liquid typo (Bug 6)
    try:
        analyze_liquid("Water", 25, 0, 100)
        bugs_fixed += 1
        print("✅ Bug 6 fixed: analyze_liquid() has no typos!")
    except NameError as e:
        print(f"❌ Bug 6: analyze_liquid() has variable name error: {e}")
        print("   HINT: Check spelling of 'temperature'")
    
    # Test 7: print_liquid_info f-string (Bug 7)
    try:
        print("\n🧪 Testing print_liquid_info:")
        print_liquid_info("Water", 0, 100)
        bugs_fixed += 1
        print("✅ Bug 7 fixed: print_liquid_info() uses f-string correctly!")
        print("   (Check that it printed 'Liquid: Water' not 'Liquid: {name}')")
    except:
        print("❌ Bug 7: print_liquid_info() still has errors")
    
    # Test 8-10: Note for students
    print("\n💡 Bugs 8-10: Test by running the full program after fixing!")
    print("   Bug 8: get_user_choice() needs int() conversion")
    print("   Bug 9: show_all_liquids() loop goes too far")
    print("   Bug 10: get_freezing_by_name() uses string as index")
    
    print("\n" + "=" * 50)
    print(f"🎯 SCORE: {bugs_fixed}/10 bugs fixed!")
    print("=" * 50)
    
    if bugs_fixed == 7:
        print("🎉 Great progress! Fix the remaining 3 bugs!")
    elif bugs_fixed >= 5:
        print("👍 Good work! Keep debugging!")
    else:
        print("💪 Keep going! Read error messages carefully!")

# ============================================
# RUN THE TESTS
# ============================================
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("Ready to start debugging?")
    print("The program will crash on the first bug.")
    print("Fix it, then run again!")
    print("=" * 50)
    input("\nPress Enter to run tests...")
    run_tests()
    
    print("\n" + "=" * 50)
    print("After fixing all bugs, you'll have learned:")
    print("✅ How to read error messages")
    print("✅ Common syntax errors (colons, indentation)")
    print("✅ Logic errors (wrong operators, wrong indices)")
    print("✅ Type errors (strings vs numbers)")
    print("✅ How to debug systematically")
    print("\n🎉 LEVEL 4 COMPLETE - You're a debugging expert!")
    print("=" * 50)