# 1주차

1. 소프트웨어 공학이란
2. 소프트웨어 공학이 다루는 문제
3. 소프트웨어 공학의 문제 접근방법
4. 일정을 세우기 위한 방
5. 프로젝트 팀 구성원들은 어떻게 이루어지는가
6. 프로젝트 과정 중 리스크가 일어날 수 있는 주요 요인은 어떤게 있는가?
7. 좋은 소프트웨어 절차의 특징에 대해.
8. Waterfall Model에 대해 설명하세요.
9. development life cycle에 대해.
10. RFP와 SOW의 차이점은?
11. 소프트웨어 비용 추정을 하는 이유 ( 잘 맞지도 않는 비용 계산을 굳이 하는 이유)
12. COCOMO2 모델의 3단계에 대해 설명하세요.
13. 애자일 모델과 다른 프로젝트 모델의 차이점
14. RUP 모델이 기존의 워터폴 모델의 단점을 어떻게 없앴는지 서술
15. 프로젝트 모델을 고를 때 고려해야 할 것들

# 2주차

1. 요구사항 명세서에 작성할 기본 목차 및 요소들은 어떤게 있을지
2. use case diagram이란
3. data flow diagram이란
4. 좋은 요구사항의 성질이란
5. User requirements와 System requirements에 대해서
6. 요구사항을 정리하는 것이 어려운 이유
7. Use Case에 대해 설명하세요.
8. Use Case 모델링 과정에서 관계를 구성하는 3가지 요소에 대해 설명하세요.
9. SRS에 대해 설명하세요.
10. 요구사항은 누구로부터 얻을 수 있는가?
11. 요구사항 추출에서 나올 수 있는 문제
12. 요구사항에 우선순위를 매기는 이유

# 3주차

1. 클라이언트-서버 아키텍처란
2. MVC 아키텍처란
3. Facade design이란 무엇인가
4. 클래스간의 포함관계와 합성관계의 차이는
5. 클래스간의 연관관계와 의존관계의 차이는
6. Control Class에 대해
7. Event-driven Control의 장단점은
8. Repository Architecture란
9. Pipe and Filter Architecture의 특징은
10. 아키텍처 설계에 대해 설명하세요.
11. Splitting our reads and write 아키텍처의 특징은?
12. 보안성을 늘리기 위해 사용하는 아키텍처가 무엇인지 설명하세요
13. Activity Diagram의 특징
14. Sequence Diagram의 특징
15. State Diagram의 특징

# 4주차

1. 개방폐쇄 원리에대해서 설명하세요
2. 리스코프 치환 원리에대해서 설명하세요
3. 의존 역전 원리에대해서 설명하세요
4. Design Pattern을 세 타입으로 어떻게 분류할 수있는지.
5. Factory Method Pattern에 대해
6. Abstract Factory Pattern은 어떤 상황에서 권장되는가
7. 단계적 분해가 무엇인지 설명하세요.
8. 추상화의 종류 3가지에 대해 설명하세요.
9. 결합도, 응집도에 대해 설명하세요.
10. 단일 객체 패턴에 대해 설명하세요.
11. 어댑터 패턴에 대해 설명하세요.
12. 컴포짓 패턴에 대해 설명하세요.

# 5주차

1. iterator pattern
   접근기능과 자료구조를 분리시켜서 객체화하고, 서로 다른 구조를 가지고 있는 저장 객체에 대해서 접근하기 위해서 interface를 통일시키고 싶을 때 사용하는 패턴

2. observer pattern
   옵저버들의 목록을 객체에 등록하여 상태 변화가 있을 때마다
   메서드 등을 통해 객체가 직접 목록의 각 옵저버에게 통지하도록 하는 디자인 패턴

3. state pattern
   객체가 상태에 따라 행위를 다르게 할 때, 직접 상태를 체크하여 상태에 따른 행위를 호출하는 것이 아니라 상태를 객체화하여 필요에 따라 다르게 행동하도록 위임하는 디자인 패턴

4. 화이트박스 테스트란
   코드가 주어진 상태에서, 코드를 들여다보면서 코드 기반으로 테스트하는 기법으로, 코드가 제대로 동작하도록 하는 것에 목적이 있다.test suites 간의 비교를 통해 보다 경제적인 suites를 선택할 수 있다는 장점과(a suites에 b suites가 포함되어있으면 비용이 같더라도 a를 택함) 객관적인 테스트를 통해 객관적인 결과를 확인할 수 있고 테스트의 자동화가 가능한다는 장점이 있다.

5. branch coverage와 condition coverage를 비교하시오.
   Branch Coverage는 조건문의 분기를 확인하고 Condition Coverage는 조건문 내의 개별 조건식의 커버리지를 확인한다는 차이가 있다.

6. MC/DC coverage
   MC/DC는 소프트웨어의 특정 조건과 결정의 독립성을 확인하는 데 중점을 둔다.
   각 조건식과 결정문을 독립적으로 테스트하고, 모든 조건식과 결정문이 최소한 한 번은 참과 거짓으로 평가될 수 있도록 테스트 케이스를 작성하는 것이 목표다.
   이런 MC/DC 커버리지를 달성하면 소프트웨어의 신뢰성을 높일 수 있고 잠재적인 오류를 발견할 수 있다.

7. 인스펙션에 대해서 설명하세요.
   그룹 단위로 코드를 다 같이 읽으면서 버그를 탐색하는 방법.

8. 테스트 드라이버와 테스트 스텁에 대해서.
   스텁은 하향식 테스트로, 상위 모듈에서 하위 모듈로의 테스트를 진행하는 것이고,테스트를 위해 만든 가상의 클라이언트가 바로 스텁이고,

   드라이버는 상향식 테스트로, 하위 모듈에서 상위 모듈로의 테스트를 진행하는 것으로, 접속 인증 등의 간단한 기능만 하는(뼈대만 있는) 가상의 서버를 만든 것이 드라이버다.

9. 테스팅과 디버깅의 차이는?
   테스팅은 디펙트가 어디에 있는 지 확인하는 것이고,디버깅은 실제로 어떤 위치에서 일어나는 지를 확인하고 고치는 것

10. 블랙박스 테스팅과 화이트 박스 테스팅의 특징과 차이에 대해 설명하세요.
    블랙박스는 내부구조를 모르는 상황에서 테스팅하겠다는 것이고, (단, 명세는 가지고 있음) 화이트박스는 코드를 하나 하나 다 들여다볼수있는 상황에서 테스팅하겠다는 것이다. (단, 명세가 없음)

11. 블랙박스 테스팅의 장점에 대해 설명하세요.
    도메인에 집중해서 테스트 케이스를 설계하고 테스트한다는 장점이 있고,
    코드가 필요없다는 장점이 있다. 또, IUT가 클래스 한 개인지 함수 한 개인지 그런 건 중요치 않으므로, 코드의 규모에 상관없이 테스트 할 수 있다.

12. create/select test case의 3종류에 대해 설명하세요.
    Equivalence class partitioning가 있는데, test case에 그룹을 나눔, 각 그룹의 하나의 케이스만 뽑아내는 특징이 있다.

    Boundary value analysis는 위에서 정한 그룹의 경계 데이터(1, 49, 52, 99 등)만 뽑아서 테스트하는 것이고,

    Model-based testing는 state diagram에서 모든 state를 커버하도록 테스트하는 것이다.(이것도 그룹을 나누어서 대표 case를 하나 선별하는 것과 비슷한 느낌)
