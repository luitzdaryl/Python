"""Write a Python program that calculates the area of a circle based on the radius entered by the user.
Sample Output :
r = 1.1
Area = 3.8013271108436504
"""

PI = 3.141592653589793    
r = float(input("Enter the radius of the circle: "))
area = PI * r*r    

print(f'Area = {area}')

