# other operators
# // is truncating division (not rounding)
# % is modulus (the remainder.  this is different from the fraction)
# divmod(n1, n2) returns a tuple of (n1 // n2, n1 % n2)
# all of these are integers

print()
print(13 / 5) # 2.6
print(13 // 5) # 2
print(13 % 5) # 13 - (2 * 5) = 3
print(divmod(13, 5))
print('-----------------')

# Making a list out of a range:

# range() is designed to take only a small amount of memory
# it is saved in memory as start, stop, and step values
# thus it is never stored as a list
print(range(5)) # range(0, 5)
print(type(range(5))) # range

# surrounding range with [] doesn't work
print([range(5)]) # [range(0, 5)]
print(type([range(5)])) # list
print(len([range(5)])) # but this list only has length of 1
print([range(5)][0]) # the only item in the list is range(0, 5)

#this is what we want
print([0, 1, 2, 3, 4])
print(type([0, 1, 2, 3, 4]))

# to create a list from a range use list()
print(list(range(5))) # [0, 1, 2, 3, 4]
print(type(list(range(5)))) # list

# or use an argument unpacking operator (*)
print([*range(5)]) # [0, 1, 2, 3, 4]
print(type([*range(5)])) # list

# Printing out a mix of types:

n = 5
# concatenation won't work because mixing str with int
# print("my number is" + n) # TypeError

# need to change int to str
print("my number is " + str(n))
# which is annoying

# comma-delimeted argument works (remember it adds spaces)
print("my number is", n)
