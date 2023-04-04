# print(4+"gfg") Syntax Error becaese both types must be the same.
# print("gfg"+4) Syntax Error becaese both types must be the same.

num="12"
print(int(num))
print(float(num))

num=12
print(str(num))

# String interpolation (https://www.programiz.com/python-programming/string-interpolation)
print(f"This is {num}")


int("3.5") # Syntax Error  (ValueError: invalid literal for int() with base 10: '3.5')
int(3.5)   # Correct
