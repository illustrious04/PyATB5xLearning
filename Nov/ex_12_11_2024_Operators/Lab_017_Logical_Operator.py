"""
Comparison Operators:
== 	Equal 	                   x == y
!= 	Not equal 	               x != y
> 	Greater than 	           x > y
< 	Less than 	               x < y
>= 	Greater than or equal to   x >= y
<= 	Less than or equal to 	   x <= y

and   Returns True if both statements are true 	                x < 5 and  x < 10
or 	  Returns True if one of the statements is true 	        x < 5 or x < 4
not   Reverse the result, returns False if the result is true 	not(x < 5 and x < 10)
"""

x = 10
y = 20

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
print("------------------With User Input------------------------------")
num1 = int(input("Enter your 1st Number\n"))
num2 = int(input("Enter your 2nd Number\n"))

equal = num1 == num2
not_equal = num1 != num2
greater_than = num1 > num2
less_then = num1 < num2
greater_than_equal = num1 >= num2
less_then_equal = num1 <= num2

print(equal)
print(not_equal)
print(greater_than)
print(less_then)
print(greater_than_equal)
print(less_then_equal)

print("--------------------With if else condition")

num3 = int(input("Enter your 1st number"))
num4 = int(input("Enter your 2nd number"))

if num3 == num4:
    print("Number 1 and Number 2 are equal")
    if num3 != num4:
        print("Number 1 and Number 2 are not equal")
    elif num3 > num4:
        print("Number 1 is greater than Number 2")
else:
    print("You are out")
