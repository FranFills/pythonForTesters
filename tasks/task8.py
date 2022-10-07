"""
Use for loop to iterate from 0 to 10
For each iteration print out "Number ", i
If the i value is equal to 2 add the continue
If the i value is equal to 8 add the break statement
"""

nums = 10
for num in range(nums):

    if num == 2:
        continue
    if num == 8:
        break

    print("Number", num)
