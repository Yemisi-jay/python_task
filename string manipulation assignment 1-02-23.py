user_input = input('Type in any Words of your choice\n')

character_search = input('Type in a Character to search\n')

index = 1
response = False
for character in user_input:
    if character == character_search:
        response = True
        break

    index +=1
if response:
    print(True, "index=", index)
else:
    print(False)
    
word_search = input('Type in Words to search\n')
if word_search in user_input:
    response = True                           

if response:
    print(True)
else:
    print(False)

replace_character = input('Input a character you want to replace with\n')
index_to_replace = int(input('What is the index of character you want to replace\n'))
replace_word = input('Input word to replace with\n')
index_of_word = int(input('What is the index of word you want to replace\n'))
print(user_input.replace(user_input[index_to_replace], replace_character))
print(user_input.replace(user_input[index_of_word], replace_word))
print(user_input[0:5])
print(user_input[-5: ])
print(user_input[2:8])
print(user_input[::-1])



