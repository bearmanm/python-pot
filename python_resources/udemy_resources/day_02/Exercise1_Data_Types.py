# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
# Your program should work for different inputs. e.g. any two-digit number.

two_digit = input("enter a two digit number:\n")

print(type(two_digit)) #checks data type
# = <class 'str'>

first_digit = two_digit[0] #4
second_digit = two_digit[1] #6

a = int(first_digit)
b = int(second_digit)

print(type(a+b)) #checks data type
# = <class 'int'>

print(a+b)
# = 10

#could also get rid of a, b, variables and replace with

#result = int(first_digit) + int(second_digit)
#print(result)









