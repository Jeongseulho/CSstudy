T = int(input())
for tc in range(1,T+1):
    N = int(input())
    stop = [0]*1001
    
    for _ in range(N):                 
        bus,a,b = map(int,input().split())

        if bus ==1:
            for i in range(a,b+1):
                stop[i] +=1

        elif bus ==2:
            if a % 2 == 0:
                for m in range(a,b+1):
                    if m % 2 ==0:
                        stop[m] += 1

            elif a% 2 == 1:
                for m in range(a,b+1):
                    if m % 2 == 1:
                        stop[m] += 1

        elif bus == 3:
            if a % 2 == 0:
                for n in range(a,b+1):
                    if n % 4 == 0:
                        stop[n] += 1

            elif a % 2 ==1:
                for n in range(a,b+1):
                    if n % 3== 0 and n % 10 != 0:
                        stop[n] += 1

    max_value = stop[0]    
    for ele in stop:        
        if max_value  < ele:
            max_value = ele

    print(f'#{tc} {max_value}')
      


