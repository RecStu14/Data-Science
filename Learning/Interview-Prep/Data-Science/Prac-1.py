# PRAC 1

# In your choice of language, write a program that prints the numbers ranging from one to 50. But for multiples of three, print "Fizz" instead of the 
# number, and for the multiples of five, print "Buzz." For numbers which are multiples of both three and five, print "FizzBuzz" 

for i in range(1,50):
    if (((i % 3) == 0) and (i % 5) == 0):
        print('FizzBuzz')
    elif ((i % 5) == 0):
        print('Buzz')
    elif ((i % 3) == 0):
          print('Fizz')
    else:
        print(i)

# LEARNING POINT:
"""
The order in which we write the if and elif statements really matters alot!
If you put either %3 only or %5 only above the statement having 'and', then 'FizzBuzz' 
would never be displayed.
"""