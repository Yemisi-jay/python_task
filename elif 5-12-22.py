score = int(input("What is the score?"))
grade = ""
if score >= 70 and score <= 100:
    grade = 'A'
elif score >= 60 and score <= 69:
    grade = 'B'
elif score < 45:
    grade = 'F'
else:
    grade = "worng input"
print(f"{score} = {grade}")
    
