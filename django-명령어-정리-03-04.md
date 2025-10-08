1. 가상 환경 만들고 Django 설치: 

   ```bash
   python -m venv venv
   source venv/Scripts/activate
   pip install -r requirements.txt
   # pip freeze > requirements.txt
   ```

2. 프로젝트 생성

   ```bash
   django-admin startproject <프로젝트명> .
   ```

3. 앱 생성

   ```bash
   python manage.py startapp <앱명>
   ```

4. `goods`를 `INSTALLED_APPS`에 추가

   1. settings.py에 앱 등록

      ```
      # product_management/settings.py
      INSTALLED_APPS = [
          # ...
          '<앱명>',
      ]
      ```

5. `models.py`에서 `Product` 모델 정의 

   - 장고는 `<app_name>_<model_name 소문자>` 을 조합해서 기본 테이블 이름을 만듦

   ```python
   # goods/models.py
   from django.db import models  # 원래있음
   
   class Product(models.Model):
       name = models.CharField(max_length=100)     # varchar(100)
       description = models.TextField()            # TEXT
       price = models.IntegerField()               # INTEGER
       is_published = models.BooleanField(default=False)  # bool
   ```

6. 마이그레이션

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

---

7. 관리자 계정 생성

   ```bash
   python manage.py createsuperuser 
   ```

 - 입력 예시

   ```yaml
   Username: admin
   Email address: (엔터로 생략)
   Password: 1234
   Password (again): 1234
   ```

8. admin에 모델 등록

   ```python
   # goods/admin.py
   from django.contrib import admin
   from .models import Product # 이거
   
   admin.site.register(Product) # admin site에 등록하자 product를
   ```

9. 서버 실행 및 접속

   ```bash
   python manage.py runserver
   ```

   - http://127.0.0.1:8000/admin



---

#### 모델을 수정하고 싶다면?

1) 모델 수정

```python
# goods/models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    # 기존
    # price = models.IntegerField()
    # 변경 : 정수+소수 포함 총 10자리, 소수 둘째 자리까지 저장
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    is_published = models.BooleanField(default=False)
	
    api_url = models.URLField()
    documentation_url = models.URLField()
    auth_required = models.BooleanField()
    additional_info = models.JSONField()
    
    # 생성/수정 시간
    # 최초 저장 시 자동 기록
    created_at = models.DateTimeField(auto_now_add=True)
    # 저장될 때마다 자동 갱신
    updated_at = models.DateTimeField(auto_now=True)
    
    from django.core.validators import URLValidator, MinLengthValidator, MaxLengthValidator

    api_url = models.URLField(
        validators=[
            URLValidator(schemes=("http", "https")),
            MinLengthValidator(15),
            MaxLengthValidator(60),
        ]
    )
    
    # 값이 없어도 생성 가능: null/blank True, 기본값 None
    additional_info = models.TextField(null=True, blank=True, default=None)
```

2) 마이그레이션

```
python manage.py makemigrations
python manage.py migrate
```



---

##### shell에서의 DB 조작

0. migration

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

   

1. 외부 라이브러리 설치

   ```BASH
   pip install ipython
   ```

2. Django Shell 접속하기

   ```bash
   python manage.py shell
   # 탈출은 exit()
   ```

3. 쉘 안에서 실행

   **(1) CREATE — 데이터 생성**

   - 방법 1 (인스턴스 생성 후 저장)

     ```python
     article = Article()
     article.title = 'Hello'
     article.content = 'World'
     article.save()  # DB에 저장
     ```

   - 방법 2 (생성 시 즉시 저장)

     ```python
     article = Article(title='Hello', content='World')
     article.save()
     ```

   - 방법 3 (objects.create())

     ```python
     Article.objects.create(title='Hi', content='ORM')
     ```

   

   **(2) READ — 데이터 조회**

   - 전체 조회

     ```python
     <객체>.objects.all()
     ```

   - 단일 조회

     ```python
     Article.objects.get(pk=1)
     ```

   - 조건 조회

     ```python
     Article.objects.filter(title='Hi')
     ```

   

   **(3) UPDATE — 데이터 수정**

   - 조회 후 수정

     ```python
     article = Article.objects.get(pk=1)
     article.title = 'Updated Title'
     article.save()
     ```

   

   **(4) DELETE — 데이터 삭제**

   - 객체 삭제

     ```python
     article = Article.objects.get(pk=1)
     article.delete()
     ```

     

   
