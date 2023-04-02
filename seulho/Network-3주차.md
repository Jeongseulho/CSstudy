1. NAT란?
   - network address translation
   - TCP/UDP 포트 숫자와 소스, 목적지 IP주소등을 재기록(변경) 하는 기술
   - 이때, checksum도 재계산 해야함
2. NAT가 쓰일 수 있는 예시
   - LAN에서 벗어나 WAN으로 나갈 때, 사설 IP를 공인 IP로 변환해야함
3. 포트 포워딩이란?
   - 공유기의 NAT 기능을 이용하여 외부에서 내부의 특정 서버에 접속할 수 있도록 하는 기능
   - 공유기에서 특정 포트로 들어오는 요청을 정해진 IP와 포트로 전달하는 기능
4. HTTP 프로토콜에 대해서.
   - Hyper Text Transfer Protocol
   - 웹 표준 파일인 HTML, CSS, JS, 이미지 등을 웹서버와 브라우저가 주고받는 프로토콜
5. GET과 POST 메소드의 차이는?
   - GET : 데이터를 URL에 포함해서 전송, 서버로부터 데이터를 읽을 때 사용
   - POST : 데이터를 HTTP 메시지의 body에 포함해서 전송, 서버에 데이터를 쓸 때 사용
6. HTTP 1.0의 문제점은?
   - TCP 연결을 맺고 끊는 과정(3-way handshake)에서 오버헤드 발생
   - HTTP 1.0은 요청마다 TCP 연결을 새로 만들어야 하기 때문에, 매번 요청마다 3-way handshake가 발생
7. 요청 프로토콜과 응답 프로토콜의 차이
   - 요청 프로토콜
     - 서버가 클라이언트에게 요청을 보내는 프로토콜
     - request line, request header, request body로 구성
   - 응답 프로토콜
     - 서버가 클라이언트에게 응답을 보내는 프로토콜
     - status line, response header, response body로 구성
8. 400번, 500번대 상태코드의 차이
   - 400번대 : 클라이언트의 요청이 잘못된 경우
     - 서버에 없는 페이지 요청
     - 권한이 없는 페이지 요청
   - 500번대 : 서버의 문제로 인해 요청이 처리되지 않은 경우
     - 서버가 과부하 되어 요청 처리가 불가능한 경우
     - 최대 연결 수를 초과한 경우
9. 요청 헤더의 종류
   - Cookie : 클라이언트가 서버에게 보내는 쿠키
   - Host : URL의 호스트명과 포트번호
   - User-Agent : 클라이언트의 브라우저, 운영체제, PC or 모바일 등의 정보
10. 웹 통신을 할 때 URI의 scheme에 들어갈 것은?

    - 프로토콜의 종류, 웹에서는 http, https, ftp 등이 들어감

11. www.naver.com/webtoon/detail.nhn 에서 webtoon과 detail.nhn이 무엇을 의미하는 지
    - webtoon : 원하는 파일의 경로
    - detail.nhn : 원하는 파일의 이름
12. 주소창에서 ? 이후에 값은 무엇을 의미하는
    - 쿼리스트링, 쿼리 파라미터 등으로 불리는데, 웹서버에게 추가적인 정보를 전달하는 방법
