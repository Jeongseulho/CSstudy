# 1. address binding과 address mapping의 개념 및 차이

- address binding: 프로그램의 논리주소를 메모리의 물리주소와 연결하는 것, 시행하는 시점에 따라 3가지로 나뉨

  - compile time binding: 컴파일 시에 논리주소와 물리주소를 연결
  - load time binding: 프로그램이 메모리에 적재될 때 논리주소와 물리주소를 연결
  - run time binding: 프로그램이 실행될 때 논리주소와 물리주소를 연결

- address mapping: 프로그램의 논리주소를 물리주소로 해석하는 방법

# 2. external fragmentation과 internal fragmentation이란

- internal fragmentation: 메모리에 프로세스를 적재하는데, partition된 메모리 공간이 실제 프로세스 사용하는 메모리보다 큰 경우, 남는 메모리 공간
- external fragmentation: internal fragmentation이 발생하면서 남는 메모리 공간들이 분산되어 있어서, 메모리 공간이 충분하지만 프로세스를 적재할 수 없는 경우

# 3. fixed partition multi-programming과 variable partition multi-programming이란

- fixed partition multi-programming: 메모리를 고정된 크기의 partition으로 나누어, 각 partition에 하나의 프로세스만 적재하는 방식
- variable partition multi-programming: 프로세스의 크기에 따라 메모리를 동적으로 partition하는 방식

# 4. BMT에서 residence bit가 의미하는 것

- residence bit: 해당 프로세스가 메모리에 적재되어 있는지를 나타내는 bit

# 5. Hybrid Direct/Associative mapping의 장점

- Hybrid Direct/Associative mapping: 메모리를 direct mapping과 associative mapping을 혼합한 방식, PMT중 일부만 TLB에 저장하여, 빠르게 메모리에 적재된 프로세스를 찾는 방식(지역성을 이용)
  - direct mapping: paging 기법과 PMT를 이용하여 메모리의 각 partition에 하나의 프로세스만 적재하는 방식
  - associative mapping: PMT를 TLB에 저장하여, 빠르게 메모리에 적재된 프로세스를 찾는 방식

# 6. page fault는 어떤 상황에서 발생되고 어떻게 처리되는가.

- page fault: 프로세스가 메모리에 적재되어 있지 않은 페이지를 참조할 때 발생하는 interrupt

# 7. Deadlock의 개념

- Deadlock: 두 개 이상의 프로세스가 서로 상대방의 자원을 점유하고 있어서, 더 이상 진행할 수 없는 상태

# 8. Deadlock의 발생조건 4가지에 대해 말해보시오.

- 자원의 특성
  - exclusive use of resources: 자원은 한 번에 한 프로세스만 사용할 수 있음
  - non preemptive resource allocation: 자원을 점유한 프로세스는 스스로 자원을 반납하지 않으면 빼앗을 수 없음
- 프로세스의 특성
  - hold and wait: 프로세스가 자원을 점유한 상태에서 다른 자원을 기다림
  - circular wait: 프로세스가 자원을 요청하는 순서가 순환적임

# 9. Deadlock의 처리방법 4가지를 말해보시오.

1. 모든 자원을 공유자원으로 만들어서 deadlock을 방지 - exclusive use of resources를 방지
2. 모든 자원을 선점 가능한 자원으로 만들어서 deadlock을 방지 - non preemptive resource allocation을 방지
3. 필요한 자원들을 모두 한번에 할당받아서 deadlock을 방지 - hold and wait를 방지
4. 자원들에 순서를 부여하여 deadlock을 방지 - circular wait를 방지

# 10. 뱅커스 알고리즘을 간략히 설명하시오

- deadlock avoidance의 방법 중 하나로 자원을 빌려주기전에 빌려주고난 상태가 safe state인지를 확인하는 방법
- safe state : 자원을 할당해도 deadlock이 발생하지 않는 상태, safe sequence가 존재하는 상태
- safe sequence : 프로세스가 정상적을 종료되는 순서

# 11. Deadlock avoidance 와 Deadlock detection의 차이

- deadlock avoidance: 시스템의 상태를 계속해서 모니터링하여 deadlock이 발생하지 않도록 하는 방법, deadlock 상태가 될 가능성이 있는 경우에는 자원을 할당하지 않음
- deadlock detection: deadlock 발생 여부를 계속해서 모니터링하여(RAG 사용) deadlock이 발생하면 deadlock recovery를 수행하는 방법
  - deadlock recovery: deadlock을 해결하기 위해 프로세스를 종료하거나 자원을 할당해제하는 방법, 강제종료된 프로세스는 rollback을 수행하여 원래 상태로 복구

# 12. Checkpoint-restart method 에서 checkpoint가 어떻게 활용되는 지

- checkpoint: 프로세스가 실행되는 도중에 특정 지점마다 프로세스의 상태(context)를 저장하는 방법
- rollback: 저장된 context로 프로세스를 복구하는 방법
- deadlock recovery이후 프로세스를 rollback하기 위해 checkpoint를 활용
