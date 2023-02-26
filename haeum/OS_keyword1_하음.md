# 1, 2주차
1. 쓰레드와 프로세스의 관계 및 개념
- 프로세스는 커널에 등록되어 실행중인 프로그램으로, 스레드는 이 프로세스 안에서 리소스를 할당 받아 제어하여 다른 리소스를 만든다.
2. 선점(preemptive)스케줄링과 비선점(non-preemptive)스케줄링 이란
- 선점 스케줄링은 한 번 자원을 할당 받으면 프로세스가 끝날 때까지 사용하므로 응답 시간이 길다. 비선점 스케줄링은 언제든 할당받은 자원을 빼앗길 수 있으며, 시분할 시스템에 적합하나 context switch 부하가 발생할 수 있다.
3. 프로세스 스케줄링에서 aging기법이란
- 지정된 대기 시간을 초과한 프로세스를 상위 큐로 이동시켜 무한 대기를 방지한다.
4. 운영 체제의 주요 역할은?
- 프로세스와 프로세서, 메모리, HW SW 리소스를 관리한다. 프로그램의 실행을 관리하는 주체이기도 하며, 시스템을 보호하기도 한다.
5. 커널이란 무엇인지.
- 운영체제의 핵심을 모아둔 것으로, 메모리에 상주하며 빈번히 사용되는 기능을 담당한다.
6. 프로세스 간 동기화가 필요한 이유에 대해.
- 여러개의 프로세스들이 동시에 시스템에 존재하고, 한 공유 리소스에 접근 할 때에 일어나는 문제를 해결하기 위해 필요하다.
7. Mutual Exclusion이 무엇을 뜻하는 지
- 둘 이상의 프로세스가 critical section에 동시에 접근하는 것을 막는 방법이다.
8. Spinlock이 어떤 식으로 동작을 하고, 무엇을 위한 건지 서술
- 프로세스 동기화의 HW 적인 해결법 중 하나로, critical section에 진입하지 못할 때, 진입할 수 있을 때까지 루프를 반복하여 진입을 시도한다. 
9. Spinlock과 Semaphore의 차이점이 무엇인지
- Spinlock은 critical seciton에 진입하지 못하면 진입 할 수 있을 때까지 루프를 무한히 반복하나, Semaphore는 같은 상황에서 대기 큐에서 진입할 수 있다는 신호를 받을 때까지 대기한다.
10. 캐시가 무엇인지 설명하세요.
- 프로세서 내부에 위치한, 메인 메모리보다 용량은 작지만 빠른 메모리. 병목현상을 해결하기 위해 존재한다.
11. 가상 메모리가 무엇인지 설명하세요.
- 프로세스의 크기가 실제 메모리의 크기에 제약을 받지 않게 하기 위하여, 각 프로그램에 실제 메모리 주소가 아닌 가상의 메모리 주소를 부여한다. 다수의 프로그램을 동시에 수행할 때 메모리를 효율적으로 공유할 수 있는 장점이 있다.
12. 모니터에 대해 설명하세요.
- critical data와 critical seciton을 모아둔 곳으로, 한 번에 한 프로세스만 접근할 수 있다. low level construct이기 때문에 error의 가능성은 낮으나 컴파일러가 OS를 이해해야 사용할 수 있다.


# 3주차

1. address binding과 address mapping의 개념 및 차이
- Address Binding은 프로그램의 논리 주소를 실제 메모리의 물리 주소로 mapping한다.
- Address mapping은 물리적 주소로 논리 주소를 찾거나 또는 그 반대의 작업이다.
- binding은 주소를 mapping하여 할당한다.
2. external fragmentation과 internal fragmentation이란
- 각각 외부 단편화와 내부 단편화로 불리며, External fragmentation은 남은 메모리 크기가 프로세스 크기가 크지만 연속된 공간이 아니라서 메모리가 낭비되는 것, Internal fragmentation이란 파티션의 크기가 프로세스 크기보다 커서 메모리가 낭비되는 상황을 의미한다.
3. fixed partition multi-programming과 variable partition multi-programming이란
- Fixed partition multiprogramming은 메모리를 고정된 크기로 미리 분할하여 한 파티션에 한 프로세스만 적재한다. 때문에 메모리 관리가 간편하나 시스템 자원이 낭비될 수 있다.
- Variable partition multi-programming이란 프로세스가 공간을 요청시 메모리 공간을 동적으로 분할하여 internal fragmention을 막을 수 있다.
4. BMT에서 residence bit가 의미하는 것
- 해당 블록이 메모리에 적재되어있는지 여부를 0과 1로 나타낸다.
5. Hybrid Direct/Associative mapping의 장점
- Associative mapping의 장점이었던 적은 부하와 빠른 속도를 활용하면서도 그의 단점이었던 비싼 HW 비용을 극복했다.
6. page fault는 어떤 상황에서 발생되고 어떻게 처리되는가.
- Residence bit == 0, 즉 메모리에 블록이 올라가지 않았다면 읽어오는 데에 실패하여 page fault가 발생한다. 이때 swap device에서 해당 페이지를 메모리에 적재하여 PMT를 갱신하여 극복한다.
7. Deadlock의 개념
- 발생 가능성이 없는 이벤트를 기다리는 상태. 두 개 이상의 프로세스가 서로가 끝나기만을 기다려 영원히 끝나지 않는 상태이다.
8. Deadlock의 발생조건 4가지에 대해 말해보시오.
- Mutual exclusion : 한 리소스는 한 번에 한 프로세스만 사용할 수 있다.
- Hold and wait : 하나 이상의 자원을 가진 프로세스가 다른 프로세스가 가진 자원을 기다린다.
- No preemption : 프로세스가 일을 마친 후 자원을 자발적으로 반환한다.
- Circular wait : Hold and wait 관계의 프로세스 들이 circle로 이어져있다.
9. Deadlock의 처리방법 4가지를 말해보시오.
- Deadlock Prevention : Deadlock이 발생할 수 있는 요구조건은 하나만 없애면 deadlock이 발생하지 않을 것이니 이 요구조건을 예방한다.
- Deadlock Avoidance : 시스템을 계속 감시하여 Deadlock이 발생할 가능성이 있는 자원 할당 요청을 보류한다.
- Deadlock Detection : 교착상태를 탐지하여 발생시 Recovery 한다.
- Deadlock Recovery : Deadlock이 발생하면 해결한다.
10. 뱅커스 알고리즘을 간략히 설명하시오.
- 한 종류의 자원이 여러개 있음을 가정하고, 시스템을 항상 safe state로 유지한다. 이 때, 일단 자원을 할당했다고 가정하고 safe sequence를 찾을 수 있다면 자원을 할당하고, 그렇지 못하다면 할당을 거절한다.
11. Deadlock avoidance 와 Deadlock detection의 차이
-Deadlock avoidance는 앞 일을 고려하여 Deadlock이 발생하지 않게 하는 것이고 Deadlock detection은 현재 상태만 고려하여 Deadlock이 발생했을 때 Recovery를 필요로 하는 것이다.
12. Checkpoint-restart method 에서 checkpoint가 어떻게 활용되는 지
- 프로세스의 수행 중 특정 지점마다 context를 저장하고 추후 Rollback에서 활용한다.
