1. software를 사용한 가상 메모리 전략의 종류들

   - allocation strategy : 각 프로세스에게 메모리를 어떻게 할당할 것인가?
     - variable allocation : 프로세스가 실행동안 유동적으로(필요한 만큼) 메모리를 할당
     - fixed allocation : 프로세스가 실행동안 고정된 메모리를 할당
   - fetch strategy : 특정 page를 언제 메모리에 적재할 것인가?
   - placement strategy : page/segment를 어디에 적재 할 것인가?(paging system에서는 page frame으로 일정하므로 불필요)
   - replacement stratrgy : 새로운 들어올 page가 있을때 어떤 page와 교체할 것인가?
   - cleaning strategy : 변경된 page를 언제 write-back 할 것인가?
   - load control strategy : 메모리에 얼마나 많은 프로세스를 올릴 것인가?

2. paging 시스템에서 reference bit와 update bit
   - reference bit : 해당 페이지가 참조되었는지를 나타내는 비트
   - update bit : 해당 페이지가 수정되었는지를 나타내는 비트, 수정되었으면 disk에 write해야 함
3. 메모리 관리 성능 향상을 위해 page fault를 최소화 해야 하는 이유, page fault시 일어나는 과정들

   - page fault가 일어나면 해당 페이지를 disk에서 메모리로 가져와야 한다. 이때, 프로세스 실행 중지 -> block 상태 -> ready -> run 즉, context switch가 일어나기 때문에 성능 저하가 발생한다.

4. Segmentation system에서 일어날 수 있는 단편화와 이유
   - external fragmentation : 프로세스가 실행되기 위해 필요한 메모리 공간이 연속적으로 남아있지 않아서 프로세스를 메모리에 올릴 수 없는 현상
   - 메모리를 미리 분할해 놓지 않으므로 internal fragmentation이 발생하지 않고, external fragmentation만 발생한다.
5. Hybrid paging/segmentation system이란 무엇인지.
   - paging system과 segmentation system을 결합한 시스템
   - 먼저 논리적 주소로 segmentation을 하고, 각 segment는 다시 page로 분할된다.
6. Paging system과 Segmentation system 각각의 장단점.
   - paging system
     - 장점 : simple, low overhead, no external fragmentation
     - 단점 : complex page sharing, internal fragmentation 발생
7. Locality(지역성)의 개념과 종류별 특징에 대해 설명하세요.
   - Locality : 프로세스가 참조하는 메모리의 특성
   - Temporal Locality : 최근에 참조된 페이지는 미래에도 참조될 가능성이 높다.
   - Spatial Locality : 최근에 참조된 페이지와 인접한 페이지는 미래에도 참조될 가능성이 높다.
8. FIFO 알고리즘의 벨레이디의 모순(Belady's Anomaly)에 대해 설명하세요.
   - 더많은 page frame을 사용함에도 불구하고 page fault가 증가하는 현상(더 많은 메모리 할당하였는데 오히려 성능 저하)
9. LFU 알고리즘에 대해 설명하세요.
   - least frequently used 알고리즘으로, 최근 간격 동안 빈도수가 가장 적게 참조된 페이지를 교체한다.
10. Working Set 알고리즘을 간단히 서술하시오
    - working set size(window size) : 최근 일정 시간 동안 참조된 페이지들의 집합의 크기
    - working set : 최근 일정 시간 동안 참조된 페이지들의 집합
    - working set에 속하지 않은 페이지는 교체 대상이 된다.
11. Page Fault Frequency 알고리즘을 간단히 서술하시오
    - residence set size : 사실상 working set size와 같은 개념
    - page fault rate가 높으면 residence set size를 증가시키고 page fault rate가 낮으면 residence set size를 감소시킨다.
    - page fault가 발생후
      - page fault 간격(IFT)가 기준간격 보다 크면(low page fault rate) 일정한 간격(IFT)동안 참조된 페이지만 residence set에 유지, 나머지는 내보낸다.
      - page fault 간격(IFT)가 기준간격 보다 작으면(high page fault rate) residence set에 현재 참조된 page를 residence set에 추가한다.
    - page fault 발생시에만 메모리 상태를 갱신하므로 overhead가 적다.
12. 실현 불가능한 Variable MIN 알고리즘을 어디에 사용할 수 있는지 서술
    - page R이 t시간에 참조되면 (t, t + delta]사이에 다시 참조되는지 확인 후 참조되면 page 유지, 참조 안되면 내림, 성능평가의 척도로 사용
