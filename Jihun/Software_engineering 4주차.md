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
   확장에는 열려 있어야 하고, 변경에는 닫혀 있어야 한다는 원리이며, 기능을 변경하거나 확장할 수 있으면서 그 기능을 사용하는 코드는 수정하지 않음을 뜻한다.

2. 리스코프 치환 원리에대해서 설명하세요
   프로그램에서의 부모 객체는 자식 개체들로 대체가 가능해야 한다는 원리로, 부모 클래스의 기능들이 자식 클래스에서 그대로 동작되어야 한다는 것을 의미한다.

3. 의존 역전 원리에대해서 설명하세요
   구체적인 것들은 수시로 변경되는 반면, 추상적인 것은 자주 변경되지 않기 때문에 추상적인 것이 역전하는 것보다 좋다는 원리다.고수준 모듈(혹은 클래스)이 저수준 모듈(혹은 클래스)에 의존하지 말아야 하고, 둘 다 추상화에 의존해야 한다는 것이다.

4. Design Pattern을 세 타입으로 어떻게 분류할 수 있는지.
   객체를 생성할 때 불필요한 의존성들을 없애는 타입인 Creational Patterns, 클래스들을 어떻게 잘 구성할 것인지에 대한 타입인 Structural Patterns, 객체들이 맡은 역할들과 하는 일을 어떻게 배치할 지 고민하는 패턴인 Behavioral Patterns로 분류할 수 있다.

5. Factory Method Pattern에 대해
   구체적인 클래스 이름을 지정하지 않고 클래스를 만드는 패턴이다. 분기에 따른 객체의 생성( new 연산자로 객체를 생성하는 부분 )을 직접하지 않고, 팩토리라는 클래스에 위임하여 팩토리 클래스가 객체를 생성하도록 하는 방식을 말한다.

6. Abstract Factory Pattern은 어떤 상황에서 권장되는가
   서로 관련이 있는 객체들을 통째로 묶어서 팩토리 클래스로 만들고, 이들 팩토리를 조건에 따라 생성하도록 다시 팩토리를 만들어서 객체를 생성하는 패턴으로, 관련성 있는 여러 종류의 객체를 일관된 방식으로 생성하는 상황에 권장된다.

7. 단계적 분해가 무엇인지 설명하세요.
   내가 작성할 모듈이 한번에 작성하기 복잡한 모듈이라면, 한번에 모든 내용을 설계하지 말고, 가장 대표적인 단계가 무엇인지 찾아보라는 것이다.

8. 추상화의 종류 3가지에 대해 설명하세요.
   자세한 단계를 고려하지 않고 상위 수준에서 수행 흐름만 먼저 설계하는 과정 추상화가 있고, 데이터 구조를 대표할 수 있는 표현으로 대체하는 데이터 추상화가 있고, 프로그램 내의 명령어 실행 순서를 추상화한 제어 추상화가 있다.

9. 결합도, 응집도에 대해 설명하세요.
   2개 이상의 모듈이 있을 때 서로 얼마나 의존하는 가에 대한 것이 결합도이고, 하나의 모듈이 하나의 기능만을 구현해내는 것이 목표인데, 불필요한 기능까지 포함하고 있진 않은지 판단하는 것이 응집도이다.
   결합도는 낮을수록, 응집도는 높을수록 좋다.

10. 단일 객체 패턴에 대해 설명하세요.
    객체를 만들어내는데, 객체의 수가 프로그램이 실행되는 동안에 항상 1개만 되도록 보장하는 패턴으로, 1개의 객체만 실행하더라도 가능한 경우일 때, 메모리를 최소화 하기 위해 사용한다.

11. 어댑터 패턴에 대해 설명하세요.
    어댑터 패턴은 서로 호환 가능하지 않은 클래스들도 함께 일할 수 있도록 해주는 패턴으로, 레거시(예전, 유물코드) 코드나 새로운 코드가 호환되지 않는 인터페이스를 가질 확률이 높은데, 어댑터 패턴은 같은 인터페이스를 통해서 호환이 되게끔 하는 패턴이다.

12. 컴포짓 패턴에 대해 설명하세요.
    그룹 전체와 개별 객체를 동일하게 처리할 수 있는 패턴으로, 트리 형태로 데이터를 표현할 수 있을 때 유용하다. 클라이언트가 복잡한 구조의 오브젝트를 이용할 때 복잡함에 영향을 받지 않고 쉽게 오브젝트를 이용할 수 있도록 도와주는 특징이 있다.
