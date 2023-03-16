N = int(input())
tmp = cnt = 0
while True:
    s = str(tmp)

    if s.find('666') != -1:
        cnt += 1

    if cnt == N:
        break

    tmp += 1

print(tmp)