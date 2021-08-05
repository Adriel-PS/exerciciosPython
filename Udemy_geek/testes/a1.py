print("vamos começar")
x = 1
while True:
    if x % 20 == 0 and x % 19 == 0 and x % 18 == 0 and x % 17 == 0 and x % 16 == 0 and x % 15 == 0\
            and x % 14 == 0 and x % 13 == 0 and x % 12 == 0:
        print(x)
        break
    else:
        x += 1

print(x)