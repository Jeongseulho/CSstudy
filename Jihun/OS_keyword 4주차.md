# 1,2주차

1. **쓰레드와 프로세스의 관계 및 개념** : 
   프로세스는 메모리 상에서 실행중인 프로그램을 뜻하고, 스레드는 프로세스 안에서
   실행되는 여러가지 흐름을 뜻합니다. 프로세스는 OS로부터 주소공간, 프로세서, 메모리 등의
   자원을 할당받는데, 스레드는 프로세스 내의 자원들을 같은 프로세스 내에 스레드끼리 공유합니다.

2. **선점(preemptive)스케줄링과 비선점(non-preemptive)스케줄링 이란** : 먼저 스케줄링은 프로세스가 실행될 때, 필요 자원을 프로세스에 할당하는 작업을 말합니다.
   스케줄링은 preemption 가능여부에 따라 구분되는데,
   
   먼저 비선점 스케줄링은 이미 할당된 CPU를 다른 프로세스가 
   빼앗을 수 없는 스케줄링 기법을 말하고, 프로세스가 CPU를 할당 받으면, 완료될 때까지 CPU를 사용합니다. 그래서 모든 프로세서에 대해 공정한 처리가 가능하고, 응답시간 예측이 용이합니다. 예시로는 FCFS, SJF, 우선순위, HRN 등이 있습니다.
   
   선점은 반대로 강제로 빼앗을 수 있는 기법을 말합니다.
   우선 순위가 높은 프로세스를 빠르게 처리할 수 있지만, 선점으로 인한 많은 오버헤드를 초래하기도 합니다. 예시로는 SRT, 선점 우선순위, RR, 다단계 큐, 다단계 피드백 큐 등이 있습니다.

3. **프로세스 스케줄링에서 aging기법이란** : 에이징 기법은 시스템에서 특정 프로세스의 우선순위가 낮으면 해당 프로세스가 무한정 기다리는 경우가 발생하는데, 이를 방지하기 위해 기다린 시간에 비례하여 우선순위를 한 단계식 높여주는 방법입니다.

4. **운영 체제의 주요 역할은?** : 시스템 자원 (HW) 관리, 사용자와 컴퓨터 사이의 커뮤니케이션 지원, 응용 프로그램 관리 등의 역할을 합니다. 사용자가 사용하는 응용 프로그램을 보다 쉽고 효율적으로 동작하도록 지원하는 소프트웨어라고 할 수 있습니다.

5. **커널이란 무엇인지.** : 커널은 운영체제의 심장부로, 운영체제의 다른 부분 및 응용 프로그램 수행에 필요한 여러 가지 서비스를 제공하는 역할을 하며, 메모리나 저장장치 내에서 운영체계의 주소공간을 관리합니다.

6. **프로세스 간 동기화가 필요한 이유에 대해** : 병행 수행중인 비동기적 프로세스들이 공유 자원에 동시 접근할 때 데이터 불일치 등의 문제가 발생할 수 있는데, 이를 방지하기 위해 동기화가 필요합니다.

7. **Mutual Exclusion이 무엇을 뜻하는 지** : 특정 프로세스가 공유 자원을 사용 중일 때 다른 프로세스가 이 자원에 접근하지 못하도록 막는 것을 의미합니다. ME를 소프트웨어 적으로 해결하는 알고리즘으로 Dekker, Peterson, Semaphore 등이 있습니다.

8. **Spinlock이 어떤 식으로 동작을 하고, 무엇을 위한 건지 서술** :  스핀락(SpinLock)은 상호배제를 실현하기 위한 방법 중 하나로, 다른 스레드가 Lock을 소유하고 있다면, 그 Lock이 반환될 때까지 계속 확인하며 기다리는 방법이다.

9. **Spinlock과 Semaphore의 차이점이 무엇인지** : 스핀락은 비지웨이팅 기반의 알고리즘으로, 상태가 획득과 해제 만이 존재하며 획득과 해제의 주체가 같아야 하지만, 세마포는 해제의 주체가 획득과 같지 않아도 된다. 즉, 어떤 프로세스가 세마포어의 값을 감소시켜도 다른 프로세스가 풀어줄 수 있다.

10. **캐시가 무엇인지 설명하세요.** : 주기억장치에서 자주 사용하는 프로그램과 데이터를 저장해두어 속도를 빠르게 하는 메모리를 말합니다. 속도가 빠른 장치와 느린 장치간의 속도 차에 따른 병목현상을 줄이는 역할을 합니다.

11. **가상 메모리가 무엇인지 설명하세요.** : 물리 메모리 크기의 한계를 극복하기 위해 나온 기술로, 메모리 관리를 단순화 하고, 메모리의 용량 및 안정성을 보장하는 역할을 합니다.

12. **모니터에 대해 설명하세요.** : 프로세스 동기화 도구 중 하나로, 공유 데이터와 임계영역의 집합 입니다. 하나의 프로세스 내의 다른 스레드 간 동기화에 사용됩니다. 사용이 쉽고, Deadlock 등의 에러 발생 가능성이 낮다는 장점이 있지만 지원하는 언어에서만 사용 가능하다는 단점이 있습니다.

# 3주차

1. address binding과 address mapping의 개념 및 차이
   :
   
   **Address binding** CPU가 프로세스의 작업을 실행하기 위해서는 논리적 주소만으로는 실제 메모리의 주소를 알 수 없기 때문에 논리 주소와 위에서 언급했던 물리적 주소를 매핑해주는 작업이 필요한데 이 작업을 주소 바인딩이라고 한다.
   
   **Address mapping**
   
   유저 프로세스가 연속된 메모리 공간이라 가정하고, 내가 원하는 게 있으면 버추얼 어드레스 상의 주소에 액세스하려고 할텐데, 버추얼 어드레스가 실제로 실려있는 위치가 다를 것이고, 그것을 실제 위치로 옮겨주는 작업을 어드레스 매핑이다.

2. external fragmentation과 internal fragmentation이란
   : partition에서 한 작업이 차지하고 남은 영역은 사용할 수 없는데 이 부분을  **internal fragmentation**이라고 함
   
   한 partition 영역보다 프로그램이 커서 할당 자체를 할 수 없어, 영역 전체가 낭비될 때 이 부분을**external fragmentation** 이라고 함

3. fixed partition multi-programming과 variable partition multi-programming이란
   :
   
   [fixed partition multi-programming]
   메모리 공간을 고정된 크기로 분할하는 프로그래밍 방식으로, 메모리 관리가 간편하다는 특징이 있다. 또 각 프로세스는 하나의 partition에 적재 하고. partition의 경계마다 boundary register를 배치하여 다른 프로세스 침범 방지한다.

        [variable partition multi-programming]
        필요하다고 할 때 필요한 만큼 메모리 공간을 잘라서 나누어 주는 개념으로,
        프로세스를 처리하는 과정에서 메모리 공간이 동적으로 분할되는 특징이 있다.
        

4. BMT에서 residence bit가 의미하는 것
   : 실제로 메모리에 올라갔는지 여부를 알려주는 변수이다.
   

5. Hybrid Direct/Associative mapping의 장점
   : 이 방법은 Direct mapping과 associative mapping의 장점을 취하고 단점은 버리는 방식으로 하드웨어의 비용은 줄이고, TLB는 여전히 사용하게 하여 overhead를 줄이고 속도를 높일 수 있다.
   

6. page fault는 어떤 상황에서 발생되고 어떻게 처리되는가.
   :  운영체제의 스와퍼는 물리 메모리에 동작하고 있는 모든 프로세스를 로드하지 않는다. 게다가 운영체제의 페이저는 효율적 사용을 위해 프로세스의 모든 페이지를 물리메모리에 로드하지 않는다.그러므로 프로그램의 페이지가 물리 메모리에 부재할 수 있는데, 이것을 페이지 폴트(Page Fault)라고 한다.
   

7. Deadlock의 개념
   : 어떤 프로세스도 하고자 하는 일을 못 하는 상태
   

8. Deadlock의 발생조건 4가지에 대해 말해보시오.
   :
   
   - **상호 배제**
     - **한 번에 프로세스 하나만 해당 자원을 사용할 수 있다**. 사용 중인 자원을 다른 프로세스가 사용하려면 요청한 자원이 해제될 때까지 기다려야 한다.
   - **점유 대기**
     - 자원을 최소한 하나 보유하고, 다른 프로세스에 할당된 자원을 점유하기 위해 대기하는 프로세스가 존재해야 한다.
   - **비선점**
     - 이미 할당된 자원을 강제로 빼앗을 수 없다(비선점).
   - **순환 대기
     **

9. Deadlock의 처리방법 4가지를 말해보시오.
   : 데드락(Deadlock)은 멀티프로세스 환경에서 발생하는 상황으로, 각 프로세스가 서로가 가진 자원을 점유하고 있어 서로가 필요로 하는 자원을 얻지 못하여 작업이 진행되지 않는 상태를 말한다. 이 때, 데드락을 처리하기 위한 대표적인 방법으로는 다음과 같은 4가지가 있다.
   
   1. 예방(Prevention)
   - 데드락이 발생하지 않도록 사전에 예방하는 방법
   - 자원할당 순서 변경, 자원유지, 자원요청 제한 등을 통해 구현 가능
   2. 회피(Avoidance)
   - 데드락이 발생할 가능성이 있는 상황을 피하는 방법
   - 은행원 알고리즘(Banker's Algorithm) 등의 알고리즘을 통해 구현 가능
   3. 탐지(Detection)
   - 데드락이 발생하였을 때, 데드락을 탐지하고 그에 대한 대처를 하는 방법
   - 자원할당 그래프(Resource Allocation Graph) 등의 알고리즘을 통해 데드락을 탐지하고, 프로세스 중 하나를 선택하여 중단시키는 등의 대처를 취함
   4. 회복(Recovery)
   - 데드락이 발생한 후, 복구하는 방법
   - 프로세스를 중단시키거나, 자원을 선점하여 해결하는 등의 방법을 사용하여 데드락 상태를 해제함
     

10. 뱅커스 알고리즘을 간략히 설명하시오
    :
    
    뱅커스 알고리즘은 운영체제에서 프로세스에게 자원을 할당하기 전에 안전성을 검사하는 방법 중 하나로, 다음과 같은 단계로 이루어진다.
    
    1. 시스템에서 사용 가능한 모든 자원의 최대 수를 계산
    2. 각 프로세스가 필요로 하는 자원의 수를 정의
    3. 시스템은 현재 사용되지 않은 자원으로 모든 요청을 충족할 수 있는지 여부를 확인
    4. 요청된 자원을 할당하여 시뮬레이션
    5. 시스템이 안정적인 상태인 경우 프로세스에게 자원을 할당
    6. 안정적인 상태가 아닌 경우 할당을 보류하고 다른 프로세스에게 자원을 할당

```
안정적인 상태가 아니면 뱅커스 알고리즘은 보류하고 자원을 할당하지 않는다.. 안정적인 상태는 모든 프로세스가 필요로 하는 모든 자원을 얻을 수 있는 경우다. 이 알고리즘은 교착 상태를 방지하고 안전성을 보장하는 데 사용된다.
```

11. Deadlock avoidance 와 Deadlock detection의 차이
    : 데드락 회피는 가능성 상황을 피하는것이고, 탐지는 무시하지않고 탐지를 한 뒤 대처를 하는 처리방법이다.
    

12. Checkpoint-restart method 에서 checkpoint가 어떻게 활용되는 지
    : Checkpoint-restart method 에선 프로세스의 수행 중 특정 지점(checkpoint)마다 context를 저장하는데, 여기서 체크 포인트는 Rollback을 위해 사용한다. 예를 들어 프로세스 강제 종료 하면, 가장 최근의 checkpoint에서 재시작하게 되는 것이다.
    

# 4주차

1. software를 사용한 가상 메모리 전략의 종류들
   각 프로세스에 얼마만큼의 메모리를 할당해 줄 것인지에 대한 전략인 Allocation Strategies,
   가상 메모리의 swap device에 있는 데이터를 언제 메인 메모리에 적재할 것인지에 대한 전략인 Fetch Strategies,
   세그먼트, 또는 페이지를 메모리 상의 어디에 적재할 것인가에 대한 전략인 Placement Strategies,
   할당된 메모리 공간을 모두 사용하고 있는 상황에서 새로운 페이지나 데이터를 올려야 할 때 어떤 페이지와 교체할 것인지 선택하는 전략인 Replacement Strategies,
   비트를 언제 청소할 것인가에 대한 전략인 Cleaning Strategies,
   멀티프로그래밍 디그리 발생을 적정 수준으로 유지하는 전략인 Load Control Strategies이 있다.

2. paging 시스템에서 reference bit와 update bit
   reference bit는 해당 페이지 프레임이 최근에 참조되었는지의 여부를 나타내는 비트이고,
   update bit는 데이터가 갱신되었는지의 여부를 나타내는 비트이다.

3. 메모리 관리 성능 향상을 위해 page fault를 최소화 해야 하는 이유, page fault시 일어나는 과정들
   운영체제의 스와퍼(Swapper)는 물리 메모리에 동작하고 있는 모든 프로세스를 로드하지 않는다. 또운영체제의 페이저(Pager)는 프로세스의 모든 페이지를 물리메모리에 로드하지 않기 때문에 page fault가 발생할 수 있다. CPU가 참조할 메모리가 없으므로, I/O 작업이 필요하게 되고, 프로세스를 변경하는 과정에서 커널이 개입하게 되는데, 이때 overhead가 커지므로, 시스템 성능에 저하가 발생할 수 있다. 때문에 page fault를 최소화 해야한다.

4. Segmentation system에서 일어날 수 있는 단편화와 이유
   Segmentation system은 세그먼트 크기에 따라 메모리를 나누는 특징 때문에 내부 단편화는 발생하지 않지만 외부 단편화는 발생할 수 있다.

5. Hybrid paging/segmentation system이란 무엇인지.
   Hybrid paging/segmentation system은 paging과 segmentation. 이 둘의 장점을 융합한 것으로, 
   
   논리적 분할과 고정된 크기 분할을 결합해 페이지 공유와 보호를 용이하게 하면서 실제 메모리 관리는 프레임 단위로 해서 관리의 오버헤드는 줄였고, 외부 단편화도 발생하지 않는다는 장점을 갖는 시스템이다.

6. Paging system과 Segmentation system 각각의 장단점.
   페이징 시스템은 같은 크기로 분할해 오버헤드가 적지만 공유나 보호가 복잡한 반면, 세그멘테이션 시스템은 논리적으로 분할하기 때문에 오버헤드가 생기지만 세그먼트의 공유나 보호가 용이하다는 각각의 장단점이 있다.

7. Locality(지역성)의 개념과 종류별 특징에 대해 설명하세요.
   프로세스가 프로그램이나 데이터의 특정 영역을 집중적으로 참조하는 현상으로, 시간적 지역성 (가까운 시간 이내를 기준으로 참조), 공간적 지역성 (근처에 존재하는 데이터를 참조)이 있다. 

8. FIFO 알고리즘의 벨레이디의 모순(Belady's Anomaly)에 대해 설명하세요.
   페이지 프레임을 더 할당하더라도 성능이 떨어지는 (자원 증가에도 불구하고 성능은 낮아지는 현상)으로 그 원인은 지역성을 고려하지 않기 때문이다.

9. LFU 알고리즘에 대해 설명하세요.
   가장 사용하는 빈도가 낮은 페이지를 교체하는 알고리즘으로 사용 빈도 정보를 저장해야 한다.
   시간이 아닌 빈도만 저장하면 되기 때문에 LRU 알고리즘 대비 오버헤드는 적다는 특징을 가지지만,빈도 수를 따지기 때문에 최근에 참조된 페이지가 교체되어버릴 위험이 있고, 참조 횟수 누적에 따른 오버헤드도 발생할 수 있다.

10. Working Set 알고리즘을 간단히 서술하시오
    프로세스는 **일정시간동안 특정 주소를 집중적으로 참조**하는 경향이 있다. 집중적으로 참조되는 페이지들의 집합을 지역성 집합이라하는데,  이런 집중 참조 페이지들을 동시에 메모리에 올릴 수 있도록 보장하는 것을 워킹셋 알고리즘이라 한다.

11. Page Fault Frequency 알고리즘을 간단히 서술하시오
    WS는 페이지 폴트가 없어도 관리를 해야 한다면, PFF는 페이지 폴트가 생겼을 때 관리하는 알고리즘으로, 얼마나 자주 페이지 폴트가 발생하는가에 따라 몇 개의 페이지 프레임을 할당할지 결정하는 알고리즘이다. 페이지 폴트가 자주 발생한다면, 할당된 페이지 프레임 개수 조절해서 메모리를 늘려주고 반대라면 메모리를 줄여주는 방식으로 구현한다.

12. 실현 불가능한 Variable MIN 알고리즘을 어디에 사용할 수 있는지 서술
    앞으로 가장 오랫동안 참조되지 않을 page 교체하는 방식인데, Page reference string을 미리 알고 있어야 하므로 실현이 불가능하다. 대신 교체 기법의 **성능 평가 도구**로 사용된다.
