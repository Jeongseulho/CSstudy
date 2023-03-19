def add_star(num):
    if num == 1:
        return ['*']

    stars = add_star(num//3)
    data = []

    for star in stars:
        data.append(star*3)
    for star in stars:
        data.append(star + ' ' * (num//3) + star)
    for star in stars:
        data.append(star*3)

    return data

N = int(input())
result = add_star(N)
for i in result:
    print(i)