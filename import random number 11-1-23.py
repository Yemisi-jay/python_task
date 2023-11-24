import random

another_round = True 
while another_round:
    user_guess = int(input('Guess a number from 1 to 5\n'))
    if user_guess >= 5:
        print('error')
    else:
        random_num = random.randint(1, 5)
        print(f"user guess is, {user_guess}")
        print(f"random number is, {random_num}")
        if random_num == user_guess:
            print('Congratulations')
        else:
            print('Sorry you missed it')
        stop_program = input("Want another round?")
        exit_words = ["exit", "stop", "no", "end", '0']
        if stop_program.lower() in exit_words:
            another_round = False
        4
        
