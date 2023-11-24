import random

user_age = int(input('How old are you?\n'))
if user_age >6:
    print("You're not allowed to use this program")
else:
    user_score = 0
    for _round in range(1, 11):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        computer_sum = num1 + num2
        print(f"round {_round}:")
        user_sum = int(input(f"What is the sum of {num1} and {num2}?\n"))
        if computer_sum ==user_sum:
            user_score +=1

    print(f"user score = {user_score}/10")
    if user_score >= 7:
        print('Congratulations, You are an excellent player')
    elif user_score >= 4 and user_score <= 6:
        print('You have tried, please try harder next time')
    else:
        print('Sorry, you need to buck up next time')
