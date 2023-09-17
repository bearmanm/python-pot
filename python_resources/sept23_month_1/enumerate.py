#The enumerate() function adds a counter to an iterable and returns it (the enumerate object).
#The enumerate() function takes two arguments:

#iterable - a sequence, an iterator, or objects that support iteration
#start (optional) - enumerate() starts counting from this number. If start is omitted, 0 is taken as start.

#The enumerate() function adds counter to an iterable and returns it. The returned object is an enumerate object.
#You can convert enumerate objects to list and tuple using list() and tuple() functions respectively.
#Tuples are used to store multiple items in a single variable.

# Example 1: Working of enumerate()
grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)

print(type(enumerateGrocery))

# converting to list
print(list(enumerateGrocery))

# changing the default counter
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery))

#output
#<class 'enumerate'>
#[(0, 'bread'), (1, 'milk'), (2, 'butter')]
#[(10, 'bread'), (11, 'milk'), (12, 'butter')]



# Example 2: Looping Over an Enumerate object
grocery = ['bread', 'milk', 'butter']

for item in enumerate(grocery):
  print(item)

print()

for count, item in enumerate(grocery):
  print(count, item)

print()

# changing default start value
for count, item in enumerate(grocery, 100):
  print(count, item)
  
#output
#(0, 'bread')
#(1, 'milk')
#(2, 'butter')

#0 bread
#1 milk
#2 butter

#100 bread
#101 milk
#102 butter