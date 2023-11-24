import random

import datetime

def myfunc():
    a = 4
    print(a)
myfunc()

#a global scope

a = 30

def func():
    print(a)
func()

print(a)

#def age(birthdate):
    
    #x = datetime.datetime
    #a = datetime.datetime - birthdate
    #print(a.strptime(birthdate, '%d-%m-%Y'))
    
#birthdate = '04, 08, 2000'
#age(birthdate)

#x = math.sqrt(124)

#print(x)

def num(num1, num2):
    ans = num1 / num2
    try:
        print(ans)
    except ZeroDivisionError:
        print('Something else went wrong')
        
num1 = int(input('enter the first number'))
num2 = int(input('enter the second number'))
num(num1, num2)
    
num_list = random.randint(1,10)
print(num_list)

def string_len(a):
    for i in a:
        j +=1
    return j
    
a = input('enter a string')
lenght = string_len(a)
print('lenght is ', lenght)
    
        
    
