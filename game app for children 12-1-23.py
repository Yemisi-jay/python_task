import random

user_age = int(input('What is your age?\n'))
if user_age >6:
    print('Game not applicable for your age')
else:
    print('welcome player')
    random_sum = []
    user_score = 0
    rounds = 10
    while rounds !=0:
        print(f"round {rounds}:")
        num1 = random.randint(1,5)
        print(num1)    
        num2 = random.randint(1,5)
        print(num2)
        correct_guess = num1 + num2
        user_input = int(input('What is the sum of the numbers?\n '))
        #random_sum.append(num1+num2)
        if correct_guess == user_input:
            user_score +=1
        rounds -=1

    print(f"user score = {user_score}/10")

    if user_score >= 7:
        print('Congratulations, You are an excellent player')
    elif user_score >= 4 and user_score <= 6:
        print('You have tried, please try harder next time')
    else:
        print('Sorry, you need to buck up next time')



                     
                     
                     
                     
    

