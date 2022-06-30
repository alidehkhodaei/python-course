#Example 1--------------------------------

text=open("./text.txt")

print(text.read())

'''
Ali
This is python!
'''

print(text.read()) # Show a empty text because cursor is end of file.

'''
'''

text.close()

#Example 2--------------------------------

text=open("./text.txt")

print(text.read())

'''
Ali
This is python!
'''

text.seek(0) # Set cursor in zero index.

print(text.read())

'''
Ali
This is python!
'''
text.close()

#Example 3--------------------------------

text=open("./text.txt")

print(text.read())

'''
Ali
This is python!
'''

text.seek(1)

print(text.read())

'''
li
This is python!
'''

text.close()

#Example 4--------------------------------

text=open("./text.txt")

print(text.readline()) # Ali
print(text.readline()) # This is python!
text.close()

#Example 5--------------------------------

# Show lines file in a list

text=open("./text.txt")
text_lines=text.readlines()
print(text_lines) # ['Ali\n', 'This is python!']
text.close()

#Example 6--------------------------------

# Automatically closes the file

with open("./text.txt") as file:
    print(file.read())

#Example 7--------------------------------

text=open("./text.txt",mode='w') # Write a text in file. (Before texts cleared)
text.write("This is a text\n")
text.close()

#--------------------------------

text=open("./text.txt",mode='a') # Add a text in file.
text.write("This is a new text")
text.close()
