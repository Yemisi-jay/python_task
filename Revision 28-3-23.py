
def func1(*args):
    print("args", args)
    for arg in args:
        print(arg)

age1 = 23
age2 = 21
age3 = 20
#func1(age1, age2, age3)


def even_numbers():
    for i in range(1, 50):
        if i % 2 == 0:
            print(i)


#even_numbers()



def palindrome(word):
    if word == word[::-1]:
        print(True)
    else:
        print(False)

#word = input('enter any word ')
#palindrome(word)


def ascending_num(numbers):
    for i in range(len(numbers)):
        print(range(i+1,len(numbers)+1))
        for j in range(i+1,len(numbers)+1):
            print(numbers, i, j)
            if j < len(numbers):
                if numbers[j] < numbers[i]:
                    temp = numbers[i]
                    numbers[i] =numbers[j]
                    numbers[j] = temp

                    
                

numbers = [5, 8, 6, 4, 1, 9, 2]
ascending_num(numbers)


def num(lists):
    unique = []
    for i in lists:
        if i not in unique:
            unique.append(i)
    #print(unique)

lists = {1, 2, 2, 4, 5, 6, 4, 3, 3, 5}
num(lists)

#print(list(set(lists)))
#print(set(lists))



    
