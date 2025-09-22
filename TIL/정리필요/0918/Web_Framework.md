## Frontend & Backend

### 개발에서의 Frontend와 Backend

- **Frontend (프론트엔드)**
  - 사용자 인터페이스(UI)를 구성하고, 사용자가 애플리케이션과 상호작용할 수 있도록 함
  - ➤ HTML, CSS, JavaScript, 프론트엔드 프레임워크 등
- **Backend (백엔드)**
  - 서버 측에서 동작하며, 클라이언트의 요청에 대한 처리와 데이터베이스와의 상호작용 등을 담당
  - ➤ 서버 언어(Python, Java 등) 및 백엔드 프레임워크, 데이터베이스, API, 보안 등

> 💡 HTML: 웹 페이지의 의미와 구조를 정의하는 언어
>
>
> 💡 **CSS**: 웹 페이지의 디자인과 레이아웃을 구성하는 언어

### Frontend & Backend

![image.png](images\image 5.png)

- **Frontend**: HTML, CSS, JavaScript를 이용해 UI를 구성
  - Vue.js: 프론트엔드로 활용되는 대표적인 프레임워크
  - **흐름**
    - Client ↔ Front-end Framework ↔ Server

![image.png](images\\image 6.png)

- **Backend**: 클라이언트의 요청에 대한 처리와 데이터베이스 상호작용

  - Django는 백엔드로 활용되는 대표적인 프레임워크

  - **흐름**

    - Client ↔ Front-end Framework ↔ Server (Django, Backend)

    - Frontend & Backend + Database 연결

      1. **Client (사용자 브라우저)**

         - 사용자가 프론트엔드(HTML, CSS, JS 기반 UI)에서 어떤 동작을 수행
         - 예: 로그인 버튼 클릭, 게시글 작성 요청

      2. **Frontend Framework (Vue.js 등)**

         - 사용자의 입력을 받아 **Server(백엔드)** 로 전달
         - → 요청(request) 발생

      3. **Backend (Django 서버)**

         - 클라이언트 요청을 받아 로직을 처리
         - 필요한 경우 **Database(DB)** 와 연결해 데이터 조회/저장 수행
         - 처리 결과를 정리해 응답(response) 생성

      4. **Database(DB)**

         - 서버 요청에 따라 데이터 제공 또는 저장
         - 예: 사용자 계정 조회, 게시글 저장

      5. **응답 흐름**

         - DB → Backend → Frontend → Client
         - 최종적으로 사용자 브라우저 화면에 결과 반영

         👉 따라서 **요청(Request)** 은 Client → Frontend → Backend → DB 로 흐르고,

         **응답(Response)** 은 DB → Backend → Frontend → Client 로 되돌아옵니다.

---

## Framework

### ‘웹 서비스 개발’에는 무엇이 필요할까?

### Web Framework

- 웹 애플리케이션을 빠르게 개발할 수 있도록 도와주는 도구
- 개발에 필요한 기본 구조, 규칙, 라이브러리 등을 제공
  (로그인/로그아웃, 회원관리, 데이터베이스, 보안 등)

> 일반적인 ‘웹 서비스’에 필요한 다양한 보편적인 기능들이 존재합니다.
>
>
> 이런 기능을 전부 혼자 개발하기 보다는 이미 만들어진 도구를
>
> 효과적으로 활용하는 능력은 현대 웹 개발의 **핵심**이라고 볼 수 있습니다.

### Django Framework

Python 기반의 대표적인 웹 프레임워크

> **클라이언트 - 서버** 구조의 **서버**를 구현하는 것이
>
>
> Django를 배우는 목적입니다!

### 왜 Django를 사용할까?

- **다양성**
  Python 기반으로 웹, 모바일 앱 백엔드, API 서버 및 빅데이터 관리 등 광범위한 서비스 개발에 적합
- **확장성**
  대량의 데이터에 대해 빠르고 유연하게 확장할 수 있는 기능을 제공
- **보안**
  취약점으로부터 보호하는 보안 기능이 기본적으로 내장되어 있음
- **커뮤니티 지원**
  개발자를 위한 지원, 문서 및 업데이트를 제공하는 활성화 된 커뮤니티
- **검증된 웹 프레임워크**
  - 대규모 트래픽 서비스에서도 안정적인 서비스 제공
    - Spotify | Instagram | Dropbox | Delivery Hero

### 웹 개발 시장을 주도하는 백엔드 프레임워크 (2024 ~ 2025)

1. **Django (Python)**
2. Spring Boot (Java)
3. [ASP.NET](http://asp.net/) Core (C#)
4. Laravel (PHP)
5. Express.js (Node.js)