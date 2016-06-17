l = int(input())
h = int(input())
text = input().upper()

art = [input() for i in range(h)]
output = [""] * h

for char in text:
    if ord(char) in range(65, 91):
        for line in range(h):
            output[line] += art[line][(ord(char)-65)*l: ((ord(char)-65)+1)*l]
    else:
        for line in range(h):
            output[line] += art[line][26*l: 27*l]

for row in output:
    print(row)
