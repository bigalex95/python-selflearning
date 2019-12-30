# int
number = 5

# float
fNumber = 5.5

# str
name = "Alibek"

# bool
status = True

# comment
#For comment ==> #
#For multi string comment ==> """Write comments here"""

""" 
    To toggle line comments, execute editor.action.commentLine (CTRL+/ on Windows)

    or

    To add line comments, execute editor.action.addCommentLine (CTRL+K CTRL+C)

    To remove line comments, execute editor.action.removeCommentLine (CTRL+K CTRL+U)

    or

    To toggle a block comment, execute editor.action.blockComment (SHIFT-ALT-A)
 """

# printing out arguments
print("String") # <== print a string
print(name) # <== print a variable
print("he is \"noob\" man!") # <== writing multi under dots
print('he is "noob" man!') # <== different way
print("he is 'noob' man!") # one more way
print(name + " is 'noob' man!") # <== cancatenate string variable and strinbg
print("there are {} births.".format(number)) # <== printing variable in string
format_list = ['five','three']
print ("there are {} births and {} deaths".format(*format_list)) # unpack the list
print ("{:d} {:03d} {:>20f}".format(1,2,1.1))
print ("If there was a birth every 7 seconds, there would be: ",number,"births") # cancatenate int with string

# get input from user
name = input("Whats your name: ") # return string
print(type(name))

# base operations ==> +,-,*,/,**,%, unary minus, rounding, number Pi
x = 5
y = 10
print("x=",x,"y=",y)
z = x + y
print (z,"x+y")
z = x - y
print (z," x-y")
z = x * y
print (z," x*y")
z = x / y
print (z," x/y")
z = x ** y
print (z, "x**y")
z = x % y
print (z," x%y")
x = -x
print (x," unary minus")
a = 5.65
print (round(a)," rounding")
import math
print(math.floor(a)," under rounding")
print(math.ceil(a)," upper rounding")
print(math.pi," number Pi")

# Conditions/Decision-Making Statements
condition = 0
another_condition = 1
do_something = print("The end")
if (condition):
    do_something
elif (another_condition):
    do_something
else:
    do_something

# change color foreground and background of terminal
from colorama import Fore, Back, Style
# use Colorama to make termcolor work on windows
from colorama import init
init()
# available formatting constants are:
"""Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL"""
print(Fore.red,Back.GREEN)
print("something colored with colorama")

# getting weather information use pyowm package
# https://github.com/csparpa/pyowm all documentation see here

# using telegrambot
# https://github.com/eternnoir/pyTelegramBotAPI all documentation see here

