def info(name, age):
    print(name + " " + age)

info('Essien', '30')


def func1(*args):
    for i in args:
        print(i)

func1(20, 40, 60)
func1(80, 100)




def calculation(num1, num2):
    return (num1 + num2, num1 - num2)
    
print(calculation(8,4))


def largest_item(X):
    max_num = 0
    for i in X:
        if i > max_num :
            max_num = i
    return max_num

X = [4,6,8,24,12,2]

print(largest_item(X))

  #OR

lists = [4, 6, 8, 24, 12, 2]
print(max(lists))
    
