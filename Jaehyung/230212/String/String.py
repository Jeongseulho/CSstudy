# import sys
# sys.stdin = open("test_input.txt", "r")

# 비교 시작 인덱스 j를 두 문자열을 비교했을 때
# 틀리면 다시 0으로 초기화
for _ in range(10):
    tc = int(input())
    a = input()
    b = input()
    i = 0 # 비교 시작 인덱스
    j = 0 # 찾을 문장 인덱스
    count = 0
    while i < len(b):
        if b[i] == a[j]:
            i += 1
            j += 1

            if j == len(a):
                count += 1
                j = 0
        else:
            i = i - j + 1
            j = 0
    print(f'#{tc} {count}')