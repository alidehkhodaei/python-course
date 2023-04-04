# raise similar throw in java

#raise IndexError("throw index error")

#raise IndexError("invalid value")

def colorize(text,color):
    if type(text) is not str:
        raise TypeError("text must be a string")
    print(f"printed {text} in {color}")

colorize("Hello","Red")

colorize(2,"Red") # TypeError: text must be a string
