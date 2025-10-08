### Django ORM 총정리 노트

---

#### 1. ORM의 개념과 목적

- **ORM (Object Relational Mapping)**
  - “객체(Object)”와 “관계형 데이터(Relational Data)”를 **자동으로 매핑**하는 기술
  - 즉, **SQL을 직접 작성하지 않고** Python 코드로 DB를 조작할 수 있게 함
- **핵심 목적**
  - SQL 없이 DB를 제어
  - 코드 일관성 유지
  - *데이터베이스 독립성 확보 (DB 교체에도 코드 변경 최소화)*
- **ORM의 장점**
  - SQL 몰라도 CRUD 가능
  - 유지보수 용이
  - 재사용성 높음
  - DB 변경 시 코드 최소 수정

------

#### 2. ORM의 실제 동작 흐름

1. 모델 정의 (`models.py`)

   ```bash
   class Article(models.Model):
       title = models.CharField(max_length=10)
       content = models.TextField()
   ```

2. 마이그레이션 생성 및 반영

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. ORM을 이용한 데이터 생성/조회/수정/삭제

   ```bash
   article = Article(title='첫 글', content='Django ORM')
   article.save()  # INSERT 문 실행됨
   ```

- Django 내부에서는 위 코드가 아래 SQL로 변환됨:

  ```bash
  INSERT INTO article (title, content) VALUES ('첫 글', 'Django ORM');
  ```

------

#### 3. Django Shell을 이용한 ORM 실습

- **Shell 실행 명령어**

  ```bash
  python manage.py shell
  # 탈출은 exit()
  ```

- **모델 import**

  ```bash
  # 장고가 자동으로 해줌
  # from articles.models import Article
  ```

------

#### 4. ORM 기본 CRUD 조작 정리

##### (1) CREATE — 데이터 생성

- **방법 1 (인스턴스 생성 후 저장)**

  ```bash
  article = Article()
  article.title = 'Hello'
  article.content = 'World'
  article.save()  # DB에 저장
  ```

- **방법 2 (생성 시 즉시 저장)**

  ```bash
  article = Article(title='Hello', content='World')
  article.save()
  ```

- **방법 3 (objects.create())**

  ```bash
  Article.objects.create(title='Hi', content='ORM')
  ```

------

##### (2) READ — 데이터 조회

- **전체 조회**

  ```
  Article.objects.all()
  ```

  → SQL: `SELECT * FROM article;`

- **단일 조회**

  ```
  Article.objects.get(pk=1)
  ```

  → SQL: `SELECT * FROM article WHERE id=1;`

- **조건 조회**

  ```
  Article.objects.filter(title='Hi')
  ```

  → SQL: `SELECT * FROM article WHERE title='Hi';`

- **정렬 조회**

  ```
  Article.objects.order_by('-id')
  ```

  → SQL: `SELECT * FROM article ORDER BY id DESC;`

------

##### (3) UPDATE — 데이터 수정

- **조회 후 수정**

  ```
  article = Article.objects.get(pk=1)
  article.title = 'Updated Title'
  article.save()
  ```

------

##### (4) DELETE — 데이터 삭제

- **객체 삭제**

  ```
  article = Article.objects.get(pk=1)
  article.delete()
  ```

  → SQL: `DELETE FROM article WHERE id=1;`

------

#### 5. ORM 주요 메서드 정리표

| 메서드          | 설명                         | 예시 코드                                     |
| --------------- | ---------------------------- | --------------------------------------------- |
| **`.all()`**    | 전체 데이터 조회             | `Article.objects.all()`                       |
| **`.get()`**    | 특정 조건 1개 조회           | `Article.objects.get(pk=1)`                   |
| **`.filter()`** | 조건에 맞는 데이터 다수 조회 | `Article.objects.filter(title='Hi')`          |
| `.exclude()`    | 특정 조건 제외               | `Article.objects.exclude(pk=2)`               |
| `.order_by()`   | 정렬                         | `Article.objects.order_by('-id')`             |
| `.create()`     | 데이터 생성 및 저장          | `Article.objects.create(title='Hi')`          |
| `.count()`      | 개수 반환                    | `Article.objects.count()`                     |
| `.exists()`     | 데이터 존재 여부 확인        | `Article.objects.filter(title='Hi').exists()` |
| `.delete()`     | 데이터 삭제                  | `Article.objects.get(pk=1).delete()`          |

------

#### 6. QuerySet의 개념

- ORM이 반환하는 객체는 **QuerySet** 형태

- SQL 결과 집합과 유사

- 실제 DB 접근은 **지연 평가(Lazy Evaluation)** 방식으로 이루어짐
   → 즉, **필요할 때만 쿼리를 전송**

- **예시**

  ```
  queryset = Article.objects.all()   # 아직 SQL 실행 안 됨
  for a in queryset:                 # 이 시점에 실제 쿼리 실행
      print(a.title)
  ```

------

#### 7. 필터링과 체이닝

- ORM에서는 여러 조건을 **연속으로 연결(Chaining)** 가능

  ```
  Article.objects.filter(title__contains='Hi').exclude(pk=2).order_by('id')
  ```

  → SQL로는

  ```
  SELECT * FROM article
  WHERE title LIKE '%Hi%' AND id != 2
  ORDER BY id ASC;
  ```

------

#### 8. 데이터베이스 초기화 관련 명령어

- **DB 초기화**

  ```bash
  python manage.py flush
  ```

  → 모든 데이터 삭제 후 마이그레이션 상태 유지

- **테이블 재생성**

  ```bash
  python manage.py migrate --run-syncdb
  ```

------

#### 9. ORM 주의사항

- `.get()`은 반드시 **단일 결과만 존재**해야 함
   (없으면 `DoesNotExist`, 여러 개면 `MultipleObjectsReturned` 오류)
- `.filter()`는 **결과가 없어도 빈 QuerySet 반환**
- `save()` 후 반드시 DB 반영이 이루어짐
- `.create()`는 save() 생략 가능

------

#### 10. ORM 예제 코드 종합

```
from articles.models import Article

# CREATE
Article.objects.create(title='Django', content='ORM Example')

# READ
articles = Article.objects.filter(title__startswith='D')

# UPDATE
article = Article.objects.get(pk=1)
article.content = 'Updated Content'
article.save()

# DELETE
Article.objects.get(pk=1).delete()
```

------

#### 11. 명령어 요약표

| 구분              | 명령어                     | 설명             |
| ----------------- | -------------------------- | ---------------- |
| Django Shell 실행 | `python manage.py shell`   | ORM 테스트용     |
| 데이터 생성       | `Model.objects.create()`   | INSERT           |
| 데이터 조회       | `Model.objects.all()`      | SELECT           |
| 데이터 수정       | `Model.save()`             | UPDATE           |
| 데이터 삭제       | `Model.delete()`           | DELETE           |
| DB 초기화         | `python manage.py flush`   | 데이터 전체 삭제 |
| 마이그레이션 반영 | `python manage.py migrate` | 테이블 구조 생성 |

------

#### 12. 꼭 알아야 할 핵심 포인트

- ORM = **Python 객체 ↔ SQL 데이터 자동 변환**
- `.get()`은 단일 데이터 / `.filter()`는 다중 데이터
- `save()` : 새로운 행 추가 또는 기존 행 수정
- `delete()` : 특정 행 제거
- QuerySet은 지연 평가 (실제 쿼리 전송 시점 구분!)
- CRUD 각각에 해당하는 Python 코드와 SQL 문장을 연결 지어 기억할 것

------

#### 13. 시험 대비 단답식 퀴즈

1. ORM이란 무엇의 약자이며, 어떤 역할을 하는가?
    → Object Relational Mapping / 객체와 관계형 DB 간 자동 매핑
2. Django에서 ORM을 사용할 때 실행하는 셸 명령어는?
    → `python manage.py shell`
3. ORM에서 데이터를 생성할 수 있는 3가지 방법은?
    → 인스턴스 생성 후 `save()`, 생성자 `Article(...) + save()`, `objects.create()`
4. `.get()`과 `.filter()`의 차이점은?
    → `.get()`은 단일 객체 반환, `.filter()`는 QuerySet(복수) 반환
5. QuerySet은 실제 SQL 쿼리가 언제 실행되는가?
    → 데이터가 **평가되는 시점(예: 반복문, 리스트 변환)**
6. ORM의 장점 3가지를 말하시오.
    → SQL 몰라도 가능 / 유지보수 용이 / DB 독립성
7. `.exists()` 메서드의 반환값은?
    → 조건 만족 데이터의 존재 여부 (`True` / `False`)