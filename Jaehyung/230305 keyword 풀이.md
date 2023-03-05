1. software를 사용한 가상 메모리 전략의 종류들
   
   - Allocation Strategies : 각 프로세스에 메모리를 얼마 만큼 줄 것 인가
   
   - Fetch Strategies : 특정 페이지를 언제 적재할 것 인가
   
   - Placement Strategies : 어디에 적재할 것 인가
   
   - Replacement Strategies : 새로운 페이지를 어떤 페이지와 교체 할 것 인가
   
   - Cleaning Strategies : 변경된 페이지를 언제 write-back할 것 인가
   
   - Load Control Strategies : 적정 수준의 부하를 유지

2. paging 시스템에서 reference bit와 update bit
   
   - reference bit : 캐시나 페이지에서 최근에 참조되었는지 여부를 나타내는 bit
   
   - update bit : 캐시나 페이지에서 갱신되었는지 여부를 나타내는 bit

3. 메모리 관리 성능 향상을 위해 page fault를 최소화 해야 하는 이유, page fault시 일어나는 과정들
   
   - 프로세스는 데이터를 메모리로 가져와서 마치 page fault가 일어나지 않은 것 처럼 작동함
   
   - 시스템 성능 저하

4. Segmentation system에서 일어날 수 있는 단편화와 이유
   
   - 프로그램 논리적 block으로 분할
   
   - 메모리를 동적으로 분할하기 때문

5. Hybrid paging/segmentation system이란 무엇인지.
   
   - paging system과 Segmentation system의 장점 결합
   
   - 프로그램을 논리적 단위로 분할하고 각 segment를 고정된 크기의 페이지로 분할

6. Paging system과 Segmentation system 각각의 장단점.
   
   - Paging system
     
     - 고정된 블락으로 나눠서 관리가 편하지만 공유나 보안 부분에서 문제가 생긴다.
   
   - Segmentaition system
     
     - 공유나 보안 부분에서 용이하지만 메모리 관리 overhead가 크

7. Locality(지역성)의 개념과 종류별 특징에 대해 설명하세요.
   
   - 특정 주소로 찾아가서 데이터를 쓰는 행위를 지역성을 활용해 빠르게 접근할 수 있도록 도움을 준다
   
   - Temporal Locality : 최근에 접근했던 주소값을 다시 접근하는 경향
   
   - Spartial Locality : 최근 접근했던 주소값 근처의 주소들을 접근하는 경

8. FIFO 알고리즘의 벨레이디의 모순(Belady's Anomaly)에 대해 설명하세요.
   
   - FIFO는 먼저 들어와서 오래 있던 페이지를 교체하는 기법인데,
   
   - 벨레이디의 모순은 페이즈 프레임 수를 늘려도 페이지 fault가 더 많이 일어나는 현상을 말한다.

9. LFU 알고리즘에 대해 설명하세요.
   
   - 가장 참조 횟수가 적은 페이지를 교체하는 기법

10. Working Set 알고리즘을 간단히 서술하시오
    
    - working set : 프로세스가 특정 시점에 자주 참조하는 페이지들의 집합
    
    - 프로세스가 특정 시간 일정 장소만 참조하는데 working set을 참조하게 만

11. Page Fault Frequency 알고리즘을 간단히 서술하시오
    
    - page fault를 계산하고 page fault를 많이 일으키는 프로그램에 더 많은 페이지를 부

12. 실현 불가능한 Variable MIN 알고리즘을 어디에 사용할 수 있는지 서술
    
    - optimal solution이기 때문에 교체 기법의 성능 평가 도구로 사용
