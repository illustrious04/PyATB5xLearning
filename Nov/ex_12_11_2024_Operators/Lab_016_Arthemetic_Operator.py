# Arithmetic operators
"""
+  	Addition 	    x + y
- 	Subtraction 	x - y
* 	Multiplication 	x * y
/ 	Division 	    x / y
% 	Modulus 	    x % y
** 	Exponentiation 	x ** y
// 	Floor division 	x // y
"""

num1 = float(input("Enter Your 1st number\n"))
num2 = float(input("Enter Your 2nd number\n"))

sum = num1 + num2
sub = num1 - num2
Mul = num1 * num2
div = num1 / num2
mod = num1 % num2
expo = num1 ** num2
floordiv: float = num1 // num2

print("Sum of entered numbers is :", sum)
print("Subtraction of entered numbers is :", sub)
print("Multiplication of entered numbers is :", Mul)
print("Division of entered numbers is :", div)
print("Modulus of entered numbers is :", mod)
print("Exponentiation of entered numbers is :", expo)
print("Floor division of entered numbers is :", expo)
