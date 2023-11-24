num1 = 4
num2 = 6
num3 = 10
min_ =num1
if num1 < min_:
    min_ = num2
if num3 < min_:
    min_ = num3
max_ = num1
if num2 > max_:
    max_ =num2
if num3 > max_:
    max_ = num3
middle_num = num1 + num2 + num3 - min_ - max_
print(min_)
print(middle_num)
print(max_)
