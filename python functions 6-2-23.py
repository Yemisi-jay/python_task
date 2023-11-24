def my_func():
	resp = "ello world"
	return resp
    
print(my_func())

def func_2(name, age, sex):
	resp = f"my name is {name} {age} {sex}"
	print(resp)
name = 'Ade'
sex = 'female'
age = '12'
func_2(sex=sex, name=name, age=age)

def addition(num1, num2, num3=5):
    return num1 + num2 + num3
    
    
print(addition(5, 7, 2))
