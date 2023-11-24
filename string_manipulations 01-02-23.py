var = "Marvellous"
character = "o"
index = 1
response = False
for chrr in var:
    if chrr == character:
        response = True
        break
    index += 1
if response:
    print(True, "index=", index)
else:
    print(False)
