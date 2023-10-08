#Data_Types

# subscripting [] - start counting from 0 upwards 
print("Hello"[4]) # to print a single letter 'o' from 'Hello' use subscripting by enter the number [] 
# = o

# Integer
print(123 + 345)
# = 468

# can use under_score in place of ,commas, for int
123_456_789

# Float
3.14159

# Boolean
True
False

# print two single letters from variable.
street_name = "Abbey Road"
print(street_name[4] + street_name[7])

# convert int to str
num_char = len(input("What is your name?\n"))
new_num_char = str(num_char)
print("Your name has "  + new_num_char + " characters.")
# = Your name has 4 characters

# use type function to investigate the data type you are working with.
print(type(num_char))
print(type(len)) 
print(type(len(input("What is ur name?"))))

# you can use str, int or float to convert to that data type. 
a = str(123)
print(type(a))
# = string

a = 123
print(type(a))
# = integer

a = float(123)
print(type(a))
# = float

# to convert str to floating point number, then adding 70 which then will print the result
print(70 + float("100.5"))
# = 170.5

# convert a str to int
print(str(70)+ str(100))
# = 70100
