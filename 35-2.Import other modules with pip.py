import pyfiglet # For install (python -m pip install pyfiglet)
from termcolor import colored # For install (python -m pip install termcolor2)

text=input("What would you like to print? : ")

color=input("What color? : ")

ascii_art=pyfiglet.figlet_format(text)

result=colored(ascii_art,color)

print(result) 
