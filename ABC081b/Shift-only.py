a = input()
b = list(map(int, input().split()))
c =[]
n = 0
while True:

    if all(x % 2 == 0 for x in b):
        b = [x // 2 for x in b]
        n += 1
    else:
        break

print(n)
