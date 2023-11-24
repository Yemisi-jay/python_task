#implement a program that generates any five random numbers from 0 to 20.

#import random
#random_number = [random.randint(0, 20) for i in range (4)]
#print(random_number)


#number = int(input('Guess a number from 1 to 5 '))
#import random
#random_numbers = [random.randint(1, 5) for i in range (4)]
#if random_numbers == 1:
 #   print('Congratulations')


import random
for count in range (6):
    number = random.randint(1,6)
    print(number, end="")
    number += number
print("\n" + str(number))

 
           



