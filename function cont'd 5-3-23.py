def show_employee(name, salary):
    print(name, salary)

name = input('What is your name?\n')
salary = int(input('Input your salary?\n'))

show_employee(name =name, salary =salary)



def even_numbers():       
    num = 2
    while num <= 50:
        print(num)
        num = num + 2
    
even_numbers()

    #OR

def numbers(even):
    for i in range(1, 50 +1):
        if i % 2 ==0:
            print(i)
even = ()       
numbers(even)

def largest_item(numbers):
    largest = 0
    for i in numbers:
        if i > largest:
                largest = i
    return largest

numbers = [40, 65, 34, 98, 306, 80]
print('The largest number is :',largest_item(numbers))


def smallest_item(num):
    mini_num = num[0]
    for i in num:
        if i < mini_num:
                mini_num = i
    return mini_num

num = [65, 34, 98, 4, 306, 80]
print('The smallest number is :',smallest_item(num))
