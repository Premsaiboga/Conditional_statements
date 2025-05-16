# === CONDITIONAL STATEMENTS PRACTICE ===

# 1. Check if a number is positive, negative, or zero
print("1. Check Positive, Negative or Zero")
num = int(input("Enter a number: "))
if num > 0:
    print("Result: Positive number")
elif num < 0:
    print("Result: Negative number")
else:
    print("Result: Zero")

print("\n---------------------------\n")

# 2. Check if a number is even or odd
print("2. Check Even or Odd")
num = int(input("Enter another number: "))
if num % 2 == 0:
    print("Result: Even number")
else:
    print("Result: Odd number")

print("\n---------------------------\n")

# 3. Find the largest of 3 numbers
print("3. Find the Largest of 3 Numbers")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print("Result: Largest number is", a)
elif b >= a and b >= c:
    print("Result: Largest number is", b)
else:
    print("Result: Largest number is", c)

print("\n---------------------------\n")

# 4. Check if a year is a leap year
print("4. Check Leap Year")
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Result: Leap year")
else:
    print("Result: Not a leap year")

print("\n---------------------------\n")

# 5. Simple grade calculator
print("5. Grade Calculator")
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Result: Grade A")
elif marks >= 75:
    print("Result: Grade B")
elif marks >= 60:
    print("Result: Grade C")
elif marks >= 40:
    print("Result: Grade D")
else:
    print("Result: Fail")

print("\n=== END OF PROGRAM ===")
