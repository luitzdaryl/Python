"""Write a Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
Sample data : 3, 5, 7, 23
Output :
List : ['3', ' 5', ' 7', ' 23']
Tuple : ('3', ' 5', ' 7', ' 23')
"""

userInput = input("Enter a sequence of comma-separated numbers: ")
inputList = list(userInput.split(","))
inputTuple = tuple(inputList)


print(f"List: {inputList}")
print(f"Tuple: {inputTuple}")

