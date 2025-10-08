### Django Model 총정리 노트

#### 1. 모델(Model)의 역할

- **MTV 패턴의 M(Model)**
  - 데이터베이스(DB)와의 **중간 다리 역할**
  - SQL을 직접 쓰지 않고 **Python 코드(클래스)** 로 테이블을 정의하고 조작함
- **모델과 DB의 관계**
  - 모델은 **DB를 표현하는 설계도(Blueprint)**
  - 실제 DB는 물리적 데이터 저장소, 모델은 이를 **추상화한 Python 코드**

------

#### 2. 모델 생성의 전체 구조

- 모델은 Django 앱 내부의 `models.py` 파일에 작성함

- **기본 코드 구조**

  ```
  from django.db import models
  
  class Article(models.Model):   # models.Model을 반드시 상속받음
      title = models.CharField(max_length=10)
      content = models.TextField()
  ```

- **핵심 포인트**

  - `Article` → DB에 생성될 **테이블명(article 테이블)** 을 정의하는 클래스
  - `models.Model` → Django가 제공하는 **2000줄 이상의 핵심 기능 클래스**
  - `title`, `content` → 각각 **열(Column, 필드)** 을 정의
  - Django는 자동으로 `id`(PK)를 추가함

------

#### 3. 모델 클래스 문법 해석

- **클래스 상속**

  - `class Article(models.Model)` → `models.Model`의 모든 기능 상속

- **클래스 변수**

  - 테이블의 **필드(컬럼)** 이 됨
  - 필드는 모두 **`models` 모듈 내의 클래스 인스턴스** 로 구성됨

- **예시**

  ```
  title = models.CharField(max_length=10)  # 문자열(길이 제한 有)
  content = models.TextField()             # 문자열(길이 제한 無)
  ```

------

#### 4. 필드(Field)의 개념

- 데이터베이스의 **열(Column)** 을 정의하는 속성
- Django에서는 각 필드를 **Field 클래스의 인스턴스** 로 표현
- 대표적인 필드:
  - `CharField(max_length=n)` : 문자열, 반드시 길이 제한 지정
  - `TextField()` : 긴 문자열, 길이 제한 없음
  - `IntegerField()` : 정수형
  - `FloatField()` : 실수형
  - `DateField()`, `DateTimeField()` : 날짜·시간 데이터
  - `ImageField()`, `FileField()` : 파일/이미지 업로드용

------

#### 5. 필드 옵션(Field Options)

- 필드의 **제약 조건(Constraints)** 을 설정

- 대표적인 옵션:

  | 옵션명       | 설명                   | 기본값            |
  | ------------ | ---------------------- | ----------------- |
  | `max_length` | 문자열 최대 길이       | 필수(`CharField`) |
  | `null`       | DB에 null 허용 여부    | False             |
  | `blank`      | 입력 시 공백 허용 여부 | False             |
  | `default`    | 기본값 지정            | 없음              |

- **예시**

  ```
  title = models.CharField(max_length=10, null=False, blank=False)
  content = models.TextField(blank=True, default='내용 없음')
  ```

------

#### 6. 모델 정의 후 실행 순서

1. **모델 작성**

   ```
   class Article(models.Model):
       title = models.CharField(max_length=10)
       content = models.TextField()
   ```

2. **모델을 DB에 반영**

   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

   - `makemigrations` : 모델 설계도를 **migration 파일**로 변환
   - `migrate` : DB에 실제 **테이블 생성**

3. **결과 확인**

   ```
   python manage.py showmigrations
   python manage.py sqlmigrate app_name 0001
   ```

   - SQL 명령어로 변환된 결과 확인 가능

------

#### 7. Admin 사이트 등록

- 관리자 페이지에서 데이터 관리 가능하도록 설정

  ```
  # articles/admin.py
  from django.contrib import admin
  from .models import Article
  
  admin.site.register(Article)
  ```

- **명령어**

  ```
  python manage.py createsuperuser
  python manage.py runserver
  ```

  - `/admin/` 접속 후 로그인 → 데이터 CRUD 가능

------

#### 8. 모델의 핵심 개념 정리

- **모델 = 설계도**
  - `models.py`에 Python 문법으로 DB 구조 정의
- **Field = 컬럼(Column)**
  - 데이터 타입 및 제약조건 지정
- **Instance = 레코드(Row)**
  - DB의 한 줄 데이터 (ex. 게시글 1개)
- **Migration = 모델 → DB 반영 과정**
  - ORM(Object Relational Mapping) 기능으로 SQL 없이 DB 생성

------

#### 9. ORM(Object Relational Mapping)

- **정의**
   : 객체(Object, Python 클래스)와 관계형 데이터(Relational Data)를 자동 매핑하는 기술

- **장점**

  - SQL을 몰라도 DB 조작 가능
  - 유지보수 용이
  - 코드 일관성 보장

- **예시**

  ```
  article = Article(title='첫 글', content='Django Model')
  article.save()           # 데이터 저장
  Article.objects.all()    # 전체 조회
  Article.objects.get(pk=1)  # 특정 데이터 조회
  ```

------

#### 10. 명령어 정리표

| 구분          | 명령어                             | 설명              |
| ------------- | ---------------------------------- | ----------------- |
| 가상환경 실행 | `source venv/Scripts/activate`     | 가상환경 활성화   |
| 패키지 설치   | `pip install -r requirements.txt`  | 의존성 설치       |
| 모델 반영     | `python manage.py makemigrations`  | 마이그레이션 생성 |
| DB 적용       | `python manage.py migrate`         | 실제 DB에 반영    |
| 슈퍼유저 생성 | `python manage.py createsuperuser` | 관리자 계정 생성  |
| 서버 실행     | `python manage.py runserver`       | 로컬서버 실행     |

------

#### 11. 학습 시 반드시 암기할 것

- `models.Model` → **모든 모델 클래스의 부모**
- `makemigrations` → 설계도 생성
- `migrate` → 설계도 반영(DB 생성)
- `CharField(max_length=n)` ↔ `TextField()`
- `null`, `blank`, `default`의 차이
- ORM의 개념: **클래스와 DB를 자동 매핑**

------

#### 12. 시험 대비 단답식 퀴즈

1. Django에서 데이터베이스 구조를 정의하는 파일은?
    → `models.py`
2. 모델 클래스는 어떤 클래스를 상속받는가?
    → `models.Model`
3. `makemigrations` 명령어의 역할은?
    → 모델 변경사항을 migration 파일로 생성
4. `migrate` 명령어의 역할은?
    → migration 파일을 실제 DB에 반영
5. `CharField`와 `TextField`의 차이점은?
    → `CharField`: 길이 제한 있음 / `TextField`: 길이 제한 없음
6. 필드 제약 조건을 설정하는 매개변수 세 가지는?
    → `null`, `blank`, `default`
7. Django에서 ORM이란 무엇을 의미하는가?
    → 객체와 관계형 데이터를 매핑해 SQL 없이 DB 조작 가능하게 하는 기술
8. 모델에서 자동 생성되는 기본 필드는?
    → `id` (Primary Key)
9. Admin 사이트에 모델을 등록하는 함수는?
    → `admin.site.register(ModelName)`
10. 모델 클래스를 변경한 뒤 반드시 실행해야 하는 두 명령어는?
     → `python manage.py makemigrations`
     `python manage.py migrate`