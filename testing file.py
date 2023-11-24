import os
print(os.getcwd())


f = open("text files/demofile.txt", "r")
print(f.read())

print(f.readline())
print("got")
print(f.readline())

for x in f:
    print(x)
f.close()
