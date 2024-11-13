"""
Write a program to take the 2 user input
then sum the number
 mul -> *
div -> /
"""

"""
Logic building formula:
Step-1
What will be the input num1, num2: int
What will be the output : sub, mul, div

Step-2
Rough logic

Step-3
Writing the real logic
"""

num1 = int(input("Enter 1st number\n"))
num2 = int(input("Enter 2nd number\n"))

sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2

print("Sum of 2 numbers is: ", sum)
print("Sub of 2 numbers is: ", sub)
print("Mul of 2 numbers is: ", mul)
print("Dic of 2 numbers is: ", div)
