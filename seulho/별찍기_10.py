def draw_stars(n):
    if n == 3:
        return ['***', '* *', '***']

    Stars = draw_stars(n // 3)  # if Starts 가 ['***', '* *', '***']인 N=3에서 모양이면
    L = []

    for star in Stars:
        up = star * 3  # 여기서 up = ['***' x3, '* *' x3, '***' x3]
        L.append(up)
    for star in Stars:
        # 여기서 mid = ['***' , ' ' x9, '***']
        mid = star + ' ' * (n // 3) + star
        L.append(mid)
    for star in Stars:
        down = star * 3  # 여기서 down = ['***' x3, '* *' x3, '***' x3]
        L.append(down)

    return L


N = int(input())
result = draw_stars(N)  # 리스트의 각 인덱스가 한 row(행)을 뜻함
print('\n'.join(result))
