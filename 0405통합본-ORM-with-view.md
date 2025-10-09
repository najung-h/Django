#### 📘 ORM with View 정리노트

------

#### 1. 핵심 흐름

- Django의 **ORM (Object Relational Mapping)**을 **View 함수에서 직접 활용**하는 단계
- **CRUD(생성, 조회, 수정, 삭제)** 중 이번 학습의 핵심은 **조회(READ)**
  - **전체 게시글 조회**
  - **단일 게시글 조회 (상세 페이지)**

------

#### 2. 데이터의 흐름

1. **요청 (Request)** → 사용자가 `/articles/` 또는 `/articles/1/` 요청
2. **URLconf (urls.py)** → 요청을 **View 함수**로 라우팅
3. **View (views.py)** → ORM을 사용해 DB에서 데이터 조회
4. **Template (HTML)** → View가 전달한 데이터를 출력

------

#### 3. 전체 게시글 조회 구현 순서

##### (1) 프로젝트 URL 설정 (`project/urls.py`)

```python
from django.urls import path, include

urlpatterns = [
    path("articles/", include("articles.urls")),
]
```

##### (2) 앱 URL 설정 (`articles/urls.py`)

```python
from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),
]
```

##### (3) View 함수 (`articles/views.py`)

```python
from django.shortcuts import render
from .models import Article

def index(request):
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(request, "articles/index.html", context)
```

##### (4) Template (`articles/templates/articles/index.html`)

```html
<h1>Main Page</h1>

{% for article in articles %}
  <p>{{ article.pk }}. {{ article.title }}</p>
  <p>{{ article.content }}</p>
  <hr>
{% endfor %}
```

✅ **핵심 요약**

- `Article.objects.all()` → QuerySet 전체 조회
- `context` → 템플릿에 전달할 데이터 딕셔너리
- `{% for article in articles %}` → DTL 반복문 사용

------

#### 4. 단일 게시글 조회 구현 순서

##### (1) URLconf (`articles/urls.py`)

```python
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.detail, name="detail"),
]
```

##### (2) View 함수 (`articles/views.py`)

```python
from django.shortcuts import render
from .models import Article

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {"article": article}
    return render(request, "articles/detail.html", context)
```

##### (3) Template (`articles/templates/articles/detail.html`)

```html
<h2>{{ article.pk }}번 글</h2>
<hr>
<p>제목: {{ article.title }}</p>
<p>내용: {{ article.content }}</p>
<p>작성일: {{ article.created_at }}</p>
<p>수정일: {{ article.updated_at }}</p>
<hr>
<a href="{% url 'articles:index' %}">Back</a>
```

✅ **핵심 요약**

- `get(pk=pk)` → 단일 객체 조회 (없으면 오류 발생)
- URL의 `<int:pk>` 값이 View 함수의 매개변수로 전달됨
- `urls.py`와 `views.py`의 매개변수명(pk)은 반드시 일치해야 함

------

#### 5. ORM 핵심 개념 정리

- `objects.all()` → 모든 레코드 조회
- `objects.get(pk=1)` → 단일 레코드 조회
- `objects.filter(title="제목")` → 조건 조회
- `objects.create()` → 새 데이터 생성
- `objects.update()` → 데이터 수정
- `objects.delete()` → 데이터 삭제

------

#### 6. Variable Routing (가변 라우팅)

- URL의 일부를 **변수로 받아 처리**하는 기능

- 문법:

  ```python
  path("<int:pk>/", views.detail)
  ```

- `<int:pk>`의 값이 자동으로 `detail(request, pk)`에 전달됨

- DB 내 특정 객체의 **식별자(pk)** 조회 시 필수

------

#### 7. 실행 명령어 요약

| 명령어                             | 설명               |
| ---------------------------------- | ------------------ |
| `python manage.py runserver`       | 개발 서버 실행     |
| `python manage.py shell`           | Django Shell 진입  |
| `python manage.py makemigrations`  | 모델 변경사항 감지 |
| `python manage.py migrate`         | DB에 모델 반영     |
| `python manage.py createsuperuser` | 관리자 계정 생성   |

------

#### 8. 전체 CRUD의 구조적 사고

| 구분     | 요청 URL              | HTTP 메서드 | View 로직 | ORM           |
| -------- | --------------------- | ----------- | --------- | ------------- |
| 목록조회 | `/articles/`          | GET         | index()   | `.all()`      |
| 단일조회 | `/articles/1/`        | GET         | detail()  | `.get(pk=pk)` |
| 생성     | `/articles/create/`   | POST        | create()  | `.create()`   |
| 수정     | `/articles/1/update/` | POST        | update()  | `.update()`   |
| 삭제     | `/articles/1/delete/` | POST        | delete()  | `.delete()`   |

------

#### 9. 학습 시 주의점

- Django는 **“데이터 흐름”** 중심으로 이해해야 함
- 모든 로직은 **URL → View → Model → Template** 순으로 연결
- 복습 시 **프로젝트 생성부터 index.html까지 직접 타이핑**할 것
- `모래성식 코딩` 금지: 앞 내용이 부족하면 뒤에서 반드시 막힘

------

#### 10. 단답식 퀴즈

1. ORM이란 무엇인가?
    → **객체를 통해 데이터베이스를 조작하는 기술 (Object Relational Mapping)**
2. 전체 게시글을 조회하는 ORM 메서드는?
    → `objects.all()`
3. 단일 게시글을 조회할 때 사용하는 메서드는?
    → `objects.get(pk=pk)`
4. `path("<int:pk>/", views.detail)`의 의미는?
    → URL에 정수형 변수를 전달해 특정 게시글을 조회
5. `context`의 역할은?
    → View에서 템플릿으로 데이터 전달
6. 템플릿에서 DTL 문법으로 반복을 표현하는 구문은?
    → `{% for item in items %} ... {% endfor %}`
7. `render()` 함수의 세 가지 인자는?
    → `request`, `template path`, `context`
8. `app_name`을 지정하는 이유는?
    → URL 네임스페이스 구분을 위해
9. `Article.objects.get(pk=1)` 실행 시 존재하지 않으면 발생하는 예외는?
    → `DoesNotExist`
10. View 함수의 역할은?
     → 클라이언트 요청을 처리하고 적절한 응답을 반환하는 컨트롤러