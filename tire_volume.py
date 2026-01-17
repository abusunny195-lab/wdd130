import math

width = float(input("Enter the width of the tire in mm: "))
aspect_ratio = float(input("Enter the aspect ratio of the tire: "))
diameter = float(input("Enter the diameter of the wheel in inches: "))

volume = (
    math.pi * width ** 2 * aspect_ratio *
    (width * aspect_ratio + 2540 * diameter)
) / 10000000000

print(f"The approximate volume is {volume:.2f} liters")