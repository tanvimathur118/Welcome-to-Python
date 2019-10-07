##Error Handling:
    #There are various types of error that can occur. For example: SystemExit,ArithmeticError,KeyboardInterrupt,LookupError,TypeError,SyntaxError, IndexError...and many more. To deal with this lets see what we can do:
    #we should understand what type of error that can happen.\
    #To make it userfriendly we need to specify what we are excepting from them.

try:
    a=int(input('enter an integer'))
except ValueError:
    a=0    
    print('you have entered a wrong value')
print(a)
          
try:
    a=int(input('enter an integer'))
except ValueError as e:
    a=0
    print('you have entered a wrong value')
    print(e)
print(a)
          
try:
    a=eval(input('enter an integer'))
except ValueError as e:
    a=0
    print('you have entered a wrong value')
    print(e)
print(a)


        
try:
    a=int(input('enter your age'))
    assert a>0, 'enter age correctly'
except AssertionError as e:
    print(e)
    a=50
print(a)

#In such way we can deal with errors that might occur.
