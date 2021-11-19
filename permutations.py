import itertools


# Enter the remembered part of the pw

rem_pw = 'password'

# Create sets of values that I might have made up my remaining characters of the pw

first = ['1', '2', '3', '4']
second = ['!', '@', '#', '$']
third = ['1', '2', '3', '4']
fourth = ['!', '@', '#', '$']
fifth = ['1', '2', '3', '4']
sixth = ['!', '@', '#', '$']
# nth = []

# Use itertools to create permutations of the sets

l = list(itertools.product(first, second, third, fourth, fifth, sixth)) # nth

# Write the permutations to a pw file

with open('output.txt', 'w') as f:
    for i in l:
        f.write(rem_pw + ''.join([str(v) for v in i]) + '\n')

# See what your up against!

print(len(l))