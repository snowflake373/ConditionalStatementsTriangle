side1 = input("Enter the length of the triangle's side #1: ")
side2 = input("Enter the length of the triangle's side #2: ")
side3 = input("Enter the length of the triangle's side #3: ")

if side1 == side2 == side3:
  print("This triangle is equilateral.")
elif side1 == side2 or side1 == side3 or side2 == side3:
  print("This triangle is isosceles.")
else:
  print("This triangle is scalene.")