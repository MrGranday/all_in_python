# For loop

even = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

for n in even:
    # print(n)
    print(n, end=" ")


# while Loops
x = 0
while x <= 20:
    print(x, end=" ")
    # if we just print this it will be infinite because
    # 20 will always be bigger then 0
    # and if we give condition to this
    x = x+2
    # this condition will stop till 20
