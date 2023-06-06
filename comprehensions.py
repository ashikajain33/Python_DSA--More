# list comprehension
"""l=[i*i for i in range(1,11)]
print(l)

# dictonary comparihension
d={ i:i*i for i in range(1,11)}
print(d)

# set comparihension
d={ i*i for i in range(1,11)}
print(d)

# generator object can be iterated only 1 time in a program

filter : filters the non zero/ null values from a list of data
"""

l=[i for i in range(1,11)]
f=filter( lambda x: x%2==0,1)
print(list(f))

# r= reduce(lambda x,y: x+y, l)
# print(list(r))