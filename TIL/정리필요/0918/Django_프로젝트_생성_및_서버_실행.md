## Django 프로젝트 생성 및 서버 실행

### Django 프로젝트 생성 및 서버 실행 과정

1. Django 설치
2. 프로젝트 생성
3. 서버 실행

### 1. 장고 설치

`pip install django`

- Django 버전을 명시하지 않을 경우 python 3.11 기준 최신 버전인 5.2.x 버전이 설치됨
- `pip list` 로 현재 환경에 장고 설치된 것 확인

### 2. 프로젝트 생성

`django-admin startproject firstpjt .`

== 장고야 → 프로젝트 시작할게 → 이 이름으로 → 현재 디렉토리에

- `firstpjt` 라는 이름의 django 프로젝트 생성

  ![image.png](images\image 10.png)

### 3. 서버 실행

`python manage.py runserver`

- “manage.py”랑 동일한 위치에서 명령어 진행해야한다는 사실 유의

앞으로도 마지막 단어만 바뀌며 코드 입력할 것임. 

### 4. 서버 확인

`http://127.0.0.1:8000/` 접속 후 확인

![image.png](images\image_r.png)

- 장고가 우리에게 로켓 페이지를 준 것!
  - Client(웹 브라우저)에서 `127.0.0.1:8000` 주소를 입력
  - 이 주소는 **내 컴퓨터(로컬 서버)** 를 의미 → 장고 서버에 요청 전송
  - Server(장고)가 응답하여 기본 로켓 페이지를 보여줌
- `Ctrl + C` 로 서버 강제 종료 가능