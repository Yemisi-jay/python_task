def vowel_print(string):
    for char in string:
        if char in "aeiouAEIOU":
            print(char, )
    return char

string = input('Type in any word: ')

vowel_print(string)



def common_elements(list1, list2):
    common_num = [num for num in list1 if num in list2]
    return common_num

list1 = [8, 5, 9, 14, 56, 3,79]
list2 = [4, 56, 34, 9, 8, 14, 5]
list3 = common_elements(list1, list2)
print(list3)

common_elements(list1, list2)


def is_palindrome(word):
    
    return word == word[::-1]

word = input('Enter word here ')
print(is_palindrome(word))


def word_lenght(Word):
    word_count = 0
    for i in Word:
        word_count +=1
    return word_count

Word = input('Type in word ')
print(word_lenght(Word))


def ascending_order(num):
    num_list = []
    for i in range(1, num +1):
        value = int(input('Enter the value of %d element:'%i))
        num_list.append(value)
    num_list.sort()
    return num_list


num = int(input('Enter the number of list element:'))
print(ascending_order(num))
    

def cap_letter(word):
    return (word.upper())

word = input('Type in the word ')
print(cap_letter(word))



def unique_value(num):
    unique = []
    for i in num:
        if i not in unique:
            unique.append(i)
        
    return unique

num = [1, 2, 2, 3, 4, 5, 3, 5, 6]
print(unique_value(num))
    
        
        
