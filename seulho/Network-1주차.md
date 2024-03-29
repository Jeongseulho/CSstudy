1. 패킷이란?

   - 네트워크 상에서 전달되는 데이터를 통칭하는 말
   - 헤더 / 페이로드 / 풋터로 구성되어 있으며 헤더에는 전송에 필요한 정보가 담겨있고, 페이로드에는 실제 데이터가 담겨있고, 풋터에는 오류검출에 필요한 정보가 담겨있다.

2. 캡슐화와 디캡슐화란 무엇인가?

   - 캡슐화 : 데이터를 전송할때, 기존의 데이터를 페이로드에 담고 헤더를 추가하여 새로운 데이터를 만드는 과정
   - 이전과정의 전체 패킷이 다음 과정의 페이로드가 된다.
   - 디캡슐화 : 데이터를 수신할때, 헤더를 제거하여 기존의 데이터를 복원하는 과정

3. TCP/IP(4계층)의 각 계층에 대해 설명하시오

   - 1계층 : 네트워크 인터페이스
     - 데이터를 물리적인 매체를 통해 전송하는 계층, 물리적인 MAC 주소를 사용한다.
   - 2계층 : 인터넷 계층
     - 단말 구분을 위해 논리적인 IP 주소를 부여하고 연결을 관리하는 계층, IP 프로토콜을 사용한다.
   - 3계층 : 전송 계층
     - 데이터를 전송하는 계층, TCP와 UDP가 있다.
   - 4계층 : 응용 계층

     - 사용자가 application과 소통할 수 있도록 하는 계층, HTTP가 이에 해당한다.

   - 실제 데이터 송신 예시
     1. 데이터는 어플리케이션 계층에서 생성(브라우저와 서버의 소프트웨어)
     2. 전송 계층에서 패킷 단위로 데이터를 분할, 포트 번호 사용, TCP프로토콜에서 수행(일반적으로 운영체제에서 내장된 소프트웨어가 수행)
     3. 인터넷 계층에서 각 장치에 IP 주소가 부여(공유기에서 수행)
     4. 네트워크 인터페이스 계층에서 물리적인 매체를 통해 전송(랜카드에서 수행, 실제 랜선을 통해 전송)
   - 실제 데이터 수신 예시
     1. 물리적인 매체를 통해 데이터가 수신(랜카드에서 수행, 실제 랜선을 통해 수신)
     2. 인터넷 계층에서 IP 주소를 확인(공유기에서 수행)
     3. 전송 계층에서 포트 번호를 이용해 데이터를재조립(일반적으로 운영체제에서 내장된 소프트웨어가 수행)
     4. 어플리케이션 계층에서 데이터를 수신(브라우저와 서버의 소프트웨어)
   - 이렇게 각 계층에서 수행되는 역할에 따라 데이터를 송수신하고, 전송 중 발생하는 오류나 문제를 해결하여 신뢰성과 안정성을 제공하는 것이 TCP/IP 모델의 역할입니다.

4. TCP/IP 모델과 OSI 모델의 차이점은?
   - OSI 모델은 역할 기반으로 계층을 나누었고, TCP/IP 모델은 프로토콜 기반으로 계층을 나누었다.
5. 패킷을 이용한 통신과정에 대해 설명해보세요.
   - 캡슐화, 디캡슐화 과정을 통해 데이터를 전송한다.
6. OSI 계층 중, 2계층의 역할은?

   - 데이터링크 계층으로, 물리적인 매체를 통해 데이터를 전송하는 역할을 한다.

7. 현재는 IP주소를 어떤 방식으로 사용하는 지 서술하시오
   - IP주소는 IPv4와 IPv6가 있고, 한국에서는 주로 IPv4를 사용한다.
8. TCP/IP 모델에서 3계층이 하는 일을 서술하시오 (2계층과의 차이점과 같이)
   - 3계층 : 전송 계층에서는 데이터 패킷단위로 분할 또는 재조립하는 역할을 한다, TCP와 UDP 프로토콜을 사용한다.
   - 2계층 : 인터넷 계층에서는 단말 구분을 위해 논리적인 IP 주소를 부여하고 연결을 관리하는 역할을 한다.
9. 네이버 내 IP주소 찾기를 하면 나오는 주소가 내 컴퓨터의 주소인지 서술하시오
   - 공인 IP 주소가 나온다.
   - 사설 IP : 네트워크 대역내에서 사용하는 IP, 같은 공유기(네트워크)내에서 장비마다 부여되는 IP
   - 공인 IP : 같은 네트워크 대역의 장비들이 사용하는 IP, 같은 공유기를 통해 인터넷에 연결된 장비들은 모두 공유기의 공인 IP를 사용한다.
