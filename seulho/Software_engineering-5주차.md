1. iterator pattern
   - 서로 다른 구조의 반복객체(array, linked list, tree 등)를 동일한 인터페이스로 접근할 수 있도록 하는 패턴
   - 내부 자료구조가 달라도 동일한 인터페이스를 사용할 수 있도록 한다.
2. observer pattern
   - subject와 observer로 구성되어 있으며, subject의 상태가 변경되면 observer에게 알려주는 패턴
   - observer는 subject의 상태를 관찰하고 있다가 상태가 변경되면 알림을 받아서 처리한다.
3. state pattern
   - state에따라 동일한 메소드가 다르게 동작하도록 하는 패턴
   - state가 추가되어도 기존의 코드를 수정하지 않아도 된다.
4. 화이트박스 테스트란
   - 소스코드를 보고 테스트 케이스를 작성하는 테스트
5. branch coverage와 condition coverage를 비교하시오
   - branch coverage : 조건문의 모든 각 branch들을 1번이상 지나가도록 테스트하는 것
   - condition coverage : 조건문의 각 조건을 모두 테스트하는 것, 각 조건이 true, false인 경우가 모두 나오도록 테스트하는 것
6. MC/DC coverage
   - MC/DC pair : TC1 = T,T,T => outcome = T, TC2 = T,T,F => outcome = F인 경우 마지막 인자만 바뀌었는데, 결과가 변했으므로 마지막 인자에대한 MC/DC pair
   - MC/DC coverage : 모든 MC/DC pair를 테스트하는 것
7. 인스펙션에 대해서 설명하세요.
   - 그룹이 모여 코드를 한줄씩 모두 읽어보면서 버그를 찾는 것
   - 코드 리뷰의 한 종류
8. 테스트 드라이버와 테스트 스텁에 대해서.
   - 테스트 드라이버 : 테스트를 실행하는 러너, 프로그램
   - 테스트 스텁 : 함수A를 테스트하고 싶은데, 해당 함수안에 다른 함수 B가 존재한다면, B의 역할을 하는 임의의 보조 함수를 지칭
9. 테스팅과 디버깅의 차이는?
   - 테스팅 : 결함을 찾는 과정
   - 디버깅 : 결함을 수정하는 과정
10. 블랙박스 테스팅과 화이트 박스 테스팅의 특징과 차이에 대해 설명하세요.
    - 블랙박스 테스팅 : 소스코드를 보지 않고, 명세서를 보면서 테스트 케이스를 작성하는 테스트
    - 화이트박스 테스팅 : 소스코드를 보고 테스트 케이스를 작성하는 테스트
11. 블랙박스 테스팅의 장점에 대해 설명하세요.
    - test case 디자인을 미리 할 수 있다.
    - 도메인에 집중할 수 있다.
    - 명세서의 논리적 오류를 찾을 수 있다.
12. create/select test case의 3종류에 대해 설명하세요.
    - Equivalence class partitioning : 입력값의 동일한 특성을 가진 값들을 하나의 클래스로 묶어서 테스트 케이스를 작성하는 것, 그룹을 나누어 대표 값을 하나만 테스트
    - Boundary value analysis : 입력값의 경계값을 테스트하는 것, 경계값을 포함하는 테스트 케이스를 작성
    - Model-based testing : state diagram에서 모든 state를 커버하도록 테스트하는 것
