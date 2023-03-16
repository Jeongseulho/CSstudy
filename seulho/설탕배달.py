num = int(input())  # 총 kg
count = 0  # answer

while num >= 0:
    if num % 5 == 0:
        count += num // 5
        print(count)
        break

    num -= 3
    count += 1

else:
    print(-1)
