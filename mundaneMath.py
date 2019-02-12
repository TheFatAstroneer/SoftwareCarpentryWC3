# This script adds together all the even numbers between 1 and 100, and prints
# to the terminalself.

total = 0
for i in range(0, 100):
    if (i%2 == 0):
        total += i

print (total)
