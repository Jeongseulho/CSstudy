def BruteForce(pattern, text):
    i = 0 # text의 인덱스
    j = 0 # pattern의 인덱스
    result = 0
    while i < len(text):  #1 패턴 바꿔야됨
        if text[i] == pattern[j]: # 문자가 같으면
            i += 1 # 다음 문자로
            j += 1 # 다음 문자로
            if j == len(pattern):  # 패턴의 끝까지 다 비교했으면
                result += 1
                j = 0  # 찾은 패턴의 시작 위치 반환
        else: # 문자가 다르면
            i = i - j + 1  # i는 온만큼 되돌아가고, 다음 문자로
            j = 0 # j는 처음부터 다시 비교
    return  result



for _ in range(10):
    tc = input()
    pattern = input()
    text = input()


    count = BruteForce(pattern,text)
    print(f'#{tc} {count}')