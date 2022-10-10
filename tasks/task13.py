"""
Create a function that prints out "Hello World"
Invoke the same function in it own body
Invoke the function outside the function block
"""

def recurse(loop):
    print('Hello World')
    if loop == 0:
        return
        #loop += 1
    recurse(loop-1)

recurse(6)
