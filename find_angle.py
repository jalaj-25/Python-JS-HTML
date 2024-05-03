import math

# Read the lengths of sides a and b
a = float(input())
b = float(input())

# Calculate the angle in radians using the arctangent function
angle_rad = math.atan(b / a)

# Convert radians to degrees
angle_deg = math.degrees(angle_rad)

# Round the angle to the nearest integer
angle_deg = round(angle_deg)

# Output the result
print(str(angle_deg) + "°")
