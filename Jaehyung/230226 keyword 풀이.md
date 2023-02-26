1. address binding과 address mapping의 개념 및 차이
   
   - address binding : 프로그램의 논리 주소를 실제 메모리에 매핑
   
   - address mapping : 가상 주소를 부여하고 실제 올라간 메모리는 real address를 받음

2. external fragmentation과 internal fragmentation이란
   
   - 메모리 allocation에서 프로그램이 메모리보다 용량이 커서 들아가지 못할 때 exteranal fragmentation  메모리가 프로그램보다 커서 사용되지 않아 낭비되는 문제가 internal fragmentation

3. fixed partition multi-programming과 variable partition multi-programming이란
   
   - fixed는 고정된 크기로 메모리를 분할해서 프로그램에 적재 > 관리 편함
   
   - variable은 원하는 크기로 나누어서 메모리 공간 활용도가 좋다

4. BMT에서 residence bit가 의미하는 것
   
   - 메모리에 해당 프로그램이 적재되어 있는 지 여부를 알린다.

5. Hybrid Direct/Associative mapping의 장점
   
   - HW비용은 줄이고, Associative mapping의 장점은 활용한다.

6. page fault는 어떤 상황에서 발생되고 어떻게 처리되는가.
   
   - 프로그램이 자신의 주소 공간에는 존재하지만 메모리에는 존재하지 않는데 접근을 시도했을 때 생긴다.

7. Deadlock의 개념
   
   - 프로세스가 발생 가능성이 없는 이벤트를 기다리는 경우

8. Deadlock의 발생조건 4가지에 대해 말해보시오.
   
   - Mutual Exclusion 한번에 한 프로세스만 자원 사용 가능
   
   - Non-preemptible resources 비선점 자원
   
   - Hold and wait 자원을 가진채로 다른 프로그램을 기다림
   
   - circular wait 

9. Deadlock의 처리방법 4가지를 말해보시오.
   
   - 예방, 회피, 탐지, 회복

10. 뱅커스 알고리즘을 간략히 설명하시오
    
    - 자원 할당 결정 전에 예상되는 모든 자원의 최대 할당량을 가지고 safe state에 들 수 있는지 여부를 검사하여 데드락 가능성을 미리 조사

11. Deadlock avoidance 와 Deadlock detection의 차이
    
    - avoid는 데드락이 생길만한 상황을 미리 예측해서 생기지 않도록 하는 것
    
    - detect는 데드락이 생겼는지 탐색하고 회복하는 

12. Checkpoint-restart method 에서 checkpoint가 어떻게 활용되는 지
    
    - 데드락이 생겼을 때 데드락이 생기기전 checkpoint로 돌리는 것


