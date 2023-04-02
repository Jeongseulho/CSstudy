import sys
 
def solution():
    K, N = map(int, input().split())
    # sys.stdin.readline() 사용이유는 글 하단 참고
    lan = [int(sys.stdin.readline()) for _ in range(K)] 
    
    min_value = 1 # 랜선의 최소 길이를 1로 설정
    max_value = max(lan) # 랜선중 가장 긴 길이를 max값으로 설정
 
    while min_value <= max_value: # 이분탐색이 완료될때까지 반복
        mid = (min_value + max_value) // 2 # 이분탐색을 위한 중간값 설정
        cnt = 0 # 랜선 수를 카운팅하는 변수 반복될때 마다 초기화 해야 하므로 반복문 안에서 선언
        for i in lan:
            cnt += i // mid # 랜선을 자른 수
 
        if cnt >= N: # 랜선을 자른 수가 만들어야될 랜선의 수보다 클 경우 
            min_value = mid + 1 # 랜선의 최소 길이를 중간값보다 1크게 설정
        else: # 랜선을 자른 수가 만들어야될 랜선의 수보다 작을 경우 
            max_value = mid - 1 # 랜선의 최대 길이를 중간값보다 1작게 설정
 
    return max_value # 랜선을 자룬 수가 만들어야 될 랜선의 수와 같을경우 길이 출력
 
print(solution())