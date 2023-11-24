import math
data =[]

_round = True
while _round:
    user_num = int(input('Enter a number\n'))
    if user_num <0:
        break
    data.append(user_num)

rounds_num = (len(data))
_sum = sum(data)
mean = _sum / rounds_num
deviation = [(number - mean)**2 for number in data]
_sum_deviation = sum(deviation)
standard_deviation = _sum_deviation / mean
print(math.sqrt(standard_deviation))
    
