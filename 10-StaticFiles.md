# 10 StaticFiles 총정리 요약본

[TOC]

## 1. Static files

------

### 웹 서버와 정적 파일

- **Static(정적)**: ‘고정된’이라는 뜻으로, 서버에 미리 준비되어 있으며 요청에 따라 그대로 전달되는 파일.

  → 반대 개념: **Dynamic(동적)** (예: DB에서 데이터를 불러와 즉시 생성하는 페이지)

- **정적 파일의 예시**

  - 이미지(`.png`, `.jpg`)
  - CSS 파일
  - JavaScript 파일
  - 폰트 파일 등

- **정적 파일의 특징**

  - 서버 측에 고정되어 있으며, 사용자가 직접 변경하지 않음.
  - 요청 시 항상 동일한 형태로 제공됨.
  - 예시 비유: **식당의 인쇄된 메뉴판** — 손님이 바뀌어도 내용은 동일.

- **정적 파일 요청 과정**

  1. 사용자가 특정 URL로 요청 (예: `/static/images/logo.png`)
  2. 서버는 해당 경로에 있는 파일을 찾아서 응답으로 보냄.
  3. 브라우저는 응답받은 파일을 해석해 화면에 표시함.

- **핵심 포인트**

  서버가 **정적 파일을 제공하려면**, 그 파일의 **고유한 URL 주소**가 반드시 필요하다.

------

### Static files 기본 경로

1. **기본 경로 약속**

   - Django는 각 앱(App)의 폴더 안에 `static` 폴더가 있으면 이를 자동으로 정적 파일 경로로 인식함.

     ```
     app_name/
       ├── static/
           ├── css/
           ├── js/
           └── images/
     ```

2. **실습 예시**

   ```bash
   # 폴더 구조
   articles/
     ├── static/
         └── stylesheets/
             └── style.css
   ```

   ```css
   /* style.css */
   h1 {
       color: crimson;
   }
   ```

3. **템플릿(index.html)에서 적용하기**

   ```html
   <!-- articles/index.html -->
   {% load static %}
   <head>
       <link rel="stylesheet" href="{% static 'stylesheets/style.css' %}">
   </head>
   ```

   - `load static`: static 태그를 사용하기 위해 불러오는 명령
   - `{% static %}`: `STATIC_URL`과 결합해 실제 URL을 만들어줌
   - `<link>` 태그의 `href`에는 `{% static '파일경로' %}`를 반드시 사용해야 함.

4. **주의사항**

   - `load` 태그는 템플릿 상단에 한 번만 작성 (단, `{% extends %}`보다 위에는 올 수 없음)

   - 브라우저 캐시로 인해 적용이 안 될 경우:

     → **개발자도구 > 새로고침 버튼 > 캐시 비우기 및 강력 새로고침**

5. **STATIC_URL 설정**

   - `settings.py`에 기본적으로 포함되어 있음:

     ```python
     STATIC_URL = '/static/'
     ```

   - 이는 정적 파일 URL의 접두사(prefix)를 의미함.

   - 실제 물리적 경로는 아니며, 브라우저 요청 시 참조용으로만 사용됨.

------

### Static files 추가 경로

1. **기본 경로 외의 추가 경로 설정**

   - 여러 앱에서 공통으로 사용하는 CSS, JS 등을 관리하기 위해 별도의 정적 폴더를 추가할 수 있음.

2. **설정 방법**

   ```python
   # settings.py
   STATICFILES_DIRS = [
       BASE_DIR / "static",  # 프로젝트 루트(static/) 폴더를 추가 경로로 설정
   ]
   ```

   - `BASE_DIR`: settings.py에 기본적으로 정의된 프로젝트 최상단 경로
   - 리스트 형태로 여러 경로를 지정 가능

3. **폴더 구조 예시**

   ```
   project_root/
   ├── static/             ← 추가 경로
   │    ├── images/
   │    │     └── python.png
   │    └── css/
   ├── articles/
   │    └── static/        ← 기본 경로
   │          └── stylesheets/
   └── templates/
   ```

4. **템플릿에서 불러오기**

   ```html
   {% load static %}
   <img src="{% static 'images/python.png' %}" alt="python logo">
   ```

   - Django는 `STATICFILES_DIRS` → 각 앱의 static 폴더 순서로 탐색하며 파일을 찾음.

5. **핵심 요약**

   - **기본 경로:** `app_name/static/`
   - **추가 경로:** `STATICFILES_DIRS`로 등록한 폴더
   - 모든 정적 파일은 `{% static %}` 태그로 접근해야 한다.
   - `STATIC_URL`은 웹상 주소의 시작점(`/static/`), 물리 경로와 다름.

------

### 핵심 명령어 요약

| 구분               | 명령어 / 설정                                | 설명                               |
| ------------------ | -------------------------------------------- | ---------------------------------- |
| 가상환경 생성      | `python -m venv venv`                        | 프로젝트용 독립 환경 생성          |
| 가상환경 활성화    | `source venv/bin/activate`                   | 가상환경 실행                      |
| 패키지 설치        | `pip install -r requirements.txt`            | 필요한 라이브러리 일괄 설치        |
| DB 반영            | `python manage.py migrate`                   | 마이그레이션 실행                  |
| 서버 실행          | `python manage.py runserver`                 | 개발용 서버 실행                   |
| 정적파일 경로 설정 | `STATIC_URL = '/static/'`                    | 웹상에서 접근할 기본 주소          |
| 추가 정적파일 경로 | `STATICFILES_DIRS = [ BASE_DIR / 'static' ]` | 프로젝트 공통 static 디렉토리 지정 |

------

### 필수 개념 요약표

| 개념                 | 설명                                   |
| -------------------- | -------------------------------------- |
| **Static files**     | 고정된 파일(CSS, JS, 이미지 등)        |
| **STATIC_URL**       | 정적 파일 URL 접두사 (`/static/`)      |
| **STATICFILES_DIRS** | 추가 정적 파일 탐색 경로 리스트        |
| **load static**      | static 태그 불러오기                   |
| **{% static %}**     | 정적 파일의 URL 생성용 템플릿 태그     |
| **기본 경로**        | 앱 내부 `app/static/`                  |
| **추가 경로**        | 프로젝트 루트 `static/`                |
| **주의사항**         | 캐시 문제 발생 시 ‘강력 새로고침’ 필요 |

------

### 핵심 단답식 퀴즈

1. Django에서 정적 파일은 주로 어떤 파일들을 의미하는가?

   → **CSS, JS, 이미지, 폰트 파일**

2. 정적 파일을 불러오기 위해 템플릿에서 반드시 사용하는 태그는?

   → **`{% static %}`**

3. `load static`은 어디에 작성해야 하는가?

   → **템플릿 최상단(단, `{% extends %}` 위에는 불가)**

4. 기본 정적 파일 경로는?

   → **`app_name/static/`**

5. 공통 정적 파일을 사용하기 위한 설정 변수는?

   → **`STATICFILES_DIRS`**

6. 정적 파일의 웹 주소 접두사는 어떤 변수로 정의되는가?

   → **`STATIC_URL`**

7. 브라우저 캐시로 인해 CSS 변경이 반영되지 않을 때 해결 방법은?

   → **“캐시 비우기 및 강력 새로고침”**

------

## 2. Media files

------

### 이미지 업로드

- **Media files란?**

  사용자가 직접 업로드하는 파일을 의미함.

  예: 프로필 사진, 게시글 첨부 이미지, 동영상, 첨부 문서 등.

  → Static files은 *개발자가 제공한 고정 자원*, Media files은 *사용자가 업로드한 데이터*.

- **핵심 차이점**

  | 구분      | Static files         | Media files                |
  | --------- | -------------------- | -------------------------- |
  | 관리 주체 | 개발자 (코드에 포함) | 사용자 (업로드)            |
  | 변경 여부 | 고정                 | 변경 가능                  |
  | 대표 예시 | CSS, JS, logo 이미지 | 게시글 이미지, 프로필 사진 |
  | 제공 방식 | `{% static %}` 태그  | `MEDIA_URL` 기반 경로      |

- **환경 설정**

  ```python
  # settings.py
  MEDIA_URL = '/media/'
  MEDIA_ROOT = BASE_DIR / 'media'
  ```

  - `MEDIA_URL`: 업로드 파일에 접근하기 위한 웹상의 주소(prefix)
  - `MEDIA_ROOT`: 실제 파일이 저장될 물리적 경로

- **업로드 경로 구조 예시**

  ```
  project_root/
  ├── media/
  │    ├── uploads/
  │    │    └── post_img.png
  │    └── profile/
  │         └── user1.jpg
  ├── static/
  └── templates/
  ```

- **모델(Model) 설정**

  ```python
  # models.py
  class Article(models.Model):
      # title = models.CharField(max_length=100)
      # content = models.TextField()
      image = models.ImageField(upload_to='uploads/', blank=True, null=True)
  ```

  - `ImageField`: 이미지 업로드 전용 필드
  - `upload_to`: `MEDIA_ROOT` 하위에 생성될 폴더 지정 (예: `media/uploads/`)
  - `blank=True, null=True`: 선택 업로드 가능 설정

- **[forms.py](http://forms.py)**

  ```python
  class ArticleForm(forms.ModelForm):
      class Meta:
          model = Article
          fields = ['title', 'content', 'image']
  ```

- **[view.py](http://view.py)**

  ```python
  def create(request):
     # if request.method == 'POST':
          form = ArticleForm(request.POST, request.FILES)
          #if form.is_valid():
          #    form.save()
          #    return redirect('articles:index')
     # else:
     #     form = ArticleForm()
     # return render(request, 'articles/create.html', {'form': form})
  ```

  - `request.FILES`: 업로드된 파일을 함께 전달하기 위한 필수 인자

- **템플릿 (form 태그)**

  ```html
  <!-- articles/create.html -->
  <form action="{% url 'articles:create' %}" method="POST" enctype="multipart/form-data">
      {% csrf_token %}
      {{ form }}
      <input type="submit" value="저장">
  </form>
  ```

  - `enctype="multipart/form-data"`: 파일 업로드 필수 설정
  - 빠뜨리면 `request.FILES`가 비어 있음!

------

### 업로드 이미지 제공

1. **개발 서버에서 업로드 파일 제공하기**

   ```python
   # urls.py (project-level)
   from django.conf import settings
   from django.conf.urls.static import static
   
   # urlpatterns = [
       # path('admin/', admin.site.urls),
       # path('articles/', include('articles.urls')),
   ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   ```

   - 개발 환경에서만 사용 (`DEBUG=True`일 때만 작동)
   - 실제 배포 환경에서는 Nginx, S3, CloudFront 등에서 처리

2. **템플릿에서 출력하기**

   ```html
   <!-- articles/detail.html -->
   {% if article.image %}
   	<img src="{{ article.image.url }}" alt="이미지">
   {% endif %}
   ```

   - `.url`: 업로드된 이미지의 접근 가능한 웹 경로 반환
   - `.path`: 이미지의 실제 물리 경로 반환 (서버 내부용)

3. **업로드 후 파일 접근 경로**

   - 브라우저에서는 `/media/uploads/파일명` 형태로 접근 가능
   - 예: `http://localhost:8000/media/uploads/post_img.png`

------

### 업로드 이미지 수정

1. **수정 시 기존 이미지 유지**

   ```python
   def update(request, pk):
       article = get_object_or_404(Article, pk=pk)
       if request.method == 'POST':
           form = ArticleForm(request.POST, request.FILES, instance=article)
           if form.is_valid():
               form.save()
               return redirect('articles:detail', article.pk)
       else:
           form = ArticleForm(instance=article)
       return render(request, 'articles/update.html', {'form': form})
   ```

   - `instance=article`: 기존 데이터 불러오기
   - `request.FILES` 포함해야 기존 파일 교체 가능

2. **템플릿에서 출력하기**

   ```html
   <!-- articles/update.html -->
   
     <h1>Update</h1>
     <form action="{% url "articles:update" article.pk %}" method="POST" enctype="multipart/form-data">
       {% csrf_token %}
       {{ form }}
       <input type="submit">
     </form>
   ```

3. **이미지 삭제 옵션**

   ```html
   {% if article.image %}
       <img src="{{ article.image.url }}" alt="기존 이미지">
       <input type="checkbox" name="image-clear"> 기존 이미지 삭제
   {% endif %}
   ```

   - `ClearableFileInput` 위젯이 자동 제공됨 (`forms.FileInput`의 확장형)

4. **주의사항**

   - `MEDIA_ROOT` 내부 파일은 DB 삭제 시 자동으로 지워지지 않음

     → 필요 시 signals(`post_delete`)로 수동 삭제 로직 추가

   - 대용량 이미지 업로드 시 Pillow 설치 필요:

     ```bash
     pip install Pillow
     ```

------

### 핵심 명령어 요약

| 명령어 / 설정                     | 설명                                            |
| --------------------------------- | ----------------------------------------------- |
| `MEDIA_URL`                       | 업로드된 파일 접근용 URL 접두사 (ex. `/media/`) |
| `MEDIA_ROOT`                      | 업로드 파일이 저장될 실제 경로                  |
| `upload_to`                       | ImageField 내 저장될 폴더 이름                  |
| `request.FILES`                   | 업로드 파일 데이터를 받는 객체                  |
| `enctype="multipart/form-data"`   | form 태그에 필수                                |
| `static(settings.MEDIA_URL, ...)` | 개발 환경에서 media 파일 제공용 설정            |
| `.url`                            | 업로드 파일의 웹 경로                           |
| `.path`                           | 업로드 파일의 실제 물리 경로                    |

------

### 핵심 개념 요약표

| 개념                       | 설명                                             |
| -------------------------- | ------------------------------------------------ |
| **Media files**            | 사용자가 업로드한 파일 (이미지, 동영상, 문서 등) |
| **STATICFILES_DIRS**       | 개발자가 제공하는 정적 자원 경로                 |
| **MEDIA_URL / MEDIA_ROOT** | 업로드된 파일의 가상주소 / 물리경로              |
| **ImageField**             | 이미지 업로드 전용 필드                          |
| **upload_to**              | MEDIA_ROOT 하위 폴더 지정                        |
| **request.FILES**          | 업로드된 파일 데이터를 전달받는 객체             |
| **.url / .path**           | 웹상 URL / 서버 내부 경로                        |
| **signals (post_delete)**  | 파일 삭제 후 실제 파일 정리용                    |

------

### 핵심 단답식 퀴즈

1. 업로드된 파일이 저장되는 실제 경로를 지정하는 변수는?

   → **`MEDIA_ROOT`**

2. 업로드 파일의 웹 주소 접두사를 지정하는 변수는?

   → **`MEDIA_URL`**

3. `ImageField(upload_to='profile/')`의 결과 저장 경로는?

   → **`media/profile/` 하위**

4. `request.FILES`가 비어 있는 이유는?

   → **form 태그에 `enctype="multipart/form-data"` 누락**

5. 개발 서버에서 업로드 파일을 제공하려면 어떤 설정을 추가해야 하는가?

   → **`urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)`**

6. 업로드된 이미지의 웹 주소를 출력할 때 사용하는 속성은?

   → **`{{ article.image.url }}`**

7. 이미지 수정 시 기존 파일을 유지하려면 어떤 인자를 추가해야 하는가?

   → **`instance=article`**

------

## 3. 참고

------

### upload_to 활용

- **개념 요약**

  `ImageField`나 `FileField`에서 파일이 업로드될 **하위 경로를 지정**하는 속성.

  ```python
  image = models.ImageField(upload_to='images/')
  ```

  → 실제 저장 위치: `MEDIA_ROOT/images/`

- **폴더를 날짜별로 자동 분류하기**

  ```python
  from datetime import datetime
  
  def today_path(instance, filename):
      return f'uploads/{datetime.now().strftime("%Y/%m/%d")}/{filename}'
  
  class Article(models.Model):
      image = models.ImageField(upload_to=today_path)
  ```

  → 업로드 시 자동으로 `uploads/2025/10/10/파일명` 형태로 저장됨.

- **사용자별 폴더 분류**

  ```python
  def user_directory_path(instance, filename):
      return f'user_{instance.user.id}/{filename}'
  
  class Profile(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE)
      profile_img = models.ImageField(upload_to=user_directory_path)
  ```

  → 각 사용자별 폴더에 업로드 (`media/user_1/프로필.png`)

- **upload_to의 장점**

  - 폴더 정리 자동화 (날짜, 유저별, 타입별)
  - 코드 레벨에서 경로 제어 가능 (복잡한 구조 지원)
  - 파일명 충돌 방지 로직과 함께 사용 가능

- **주의사항**

  - `upload_to`는 `MEDIA_ROOT` 기준 경로만 지정 가능
  - `MEDIA_ROOT` 외부 경로 지정은 불가
  - lambda 표현식 사용 가능하지만 함수로 명시하는 게 유지보수에 유리

------

### AWS 인프라 이해하기 (S3 & CloudFront 중심)

- **배경**

  로컬 개발환경에서는 `MEDIA_ROOT`로 파일을 저장하지만,

  배포 환경에서는 AWS S3와 같은 **클라우드 스토리지**를 활용해야 함.

- **S3와 Django 연결 개념**

  | 구성요소                        | 설명                                                         |
  | ------------------------------- | ------------------------------------------------------------ |
  | **S3 (Simple Storage Service)** | 이미지, 파일 등을 저장하는 클라우드 버킷 서비스              |
  | **CloudFront**                  | S3 파일을 빠르게 전송하기 위한 CDN(Content Delivery Network) |
  | **boto3**                       | AWS SDK for Python — S3와 Django를 연결하는 라이브러리       |
  | **django-storages**             | Django용 S3 저장 백엔드 제공 패키지                          |

- **환경 설정 예시**

  ```bash
  pip install boto3 django-storages
  ```

  ```python
  # settings.py
  INSTALLED_APPS += ['storages']
  
  AWS_ACCESS_KEY_ID = 'your-access-key'
  AWS_SECRET_ACCESS_KEY = 'your-secret-key'
  AWS_STORAGE_BUCKET_NAME = 'your-bucket-name'
  AWS_S3_REGION_NAME = 'ap-northeast-2'  # 서울 리전
  AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
  
  DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
  MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
  ```

- **작동 원리**

  1. 사용자가 이미지를 업로드하면 Django가 S3에 직접 저장.
  2. S3는 업로드된 파일의 URL을 반환.
  3. 해당 URL을 CloudFront가 캐싱하여 빠르게 전송.

- **이점**

  - 서버 부하 감소
  - 파일 유실 위험 감소
  - 이미지 전송 속도 향상
  - 확장성 높은 구조

- **추가 팁**

  - CloudFront 도메인을 `MEDIA_URL`에 직접 연결하면 HTTPS 통신 가능.
  - 프라이빗 버킷 사용 시 signed URL 방식으로 접근 제어 가능.

------

### BaseModelForm

- **개념 요약**

  ModelForm을 상속받아 여러 앱에서 공통적으로 쓰이는 **기본 폼 구조를 재사용**하기 위한 추상 클래스.

- **기존 방식의 한계**

  - 앱마다 유사한 폼 구조를 반복 작성
  - 예: `created_at`, `updated_at`, `author` 등 공통 필드 중복 발생

- **BaseModelForm 활용 예시**

  ```python
  # forms.py
  from django import forms
  from django.forms import ModelForm
  
  class BaseModelForm(ModelForm):
      class Meta:
          abstract = True
  
      def save(self, commit=True):
          instance = super().save(commit=False)
          # 공통 로직 예: created_by 자동 지정
          if hasattr(instance, 'created_by') and not instance.created_by:
              instance.created_by = self.initial.get('user')
          if commit:
              instance.save()
          return instance
  ```

- **활용 예시 (상속 구조)**

  ```python
  class ArticleForm(BaseModelForm):
      class Meta(BaseModelForm.Meta):
          model = Article
          fields = ['title', 'content', 'image']
  ```

  - `BaseModelForm.Meta`를 상속받아 중복 제거
  - `save()` 오버라이딩을 통해 모든 하위 폼의 로직 통합

- **장점**

  - 폼 로직 일관성 유지 (특히 `save()` 시점 로직)
  - 유지보수 용이
  - 대규모 프로젝트(SSAFY, 기업 인프라형 프로젝트 등)에서 효율적

------

### 핵심 명령어 / 설정 요약

| 항목                   | 설정 / 명령                                  | 설명                                |
| ---------------------- | -------------------------------------------- | ----------------------------------- |
| `upload_to`            | `'uploads/'`, 함수 기반 경로                 | 업로드 파일의 하위 디렉토리 지정    |
| `MEDIA_URL`            | `/media/`                                    | 웹에서 접근할 URL 접두사            |
| `MEDIA_ROOT`           | `BASE_DIR / 'media'`                         | 실제 저장 폴더                      |
| `django-storages`      | pip 설치 필요                                | S3 파일 스토리지 관리용             |
| `DEFAULT_FILE_STORAGE` | `'storages.backends.s3boto3.S3Boto3Storage'` | 파일 저장소를 S3로 지정             |
| `BaseModelForm`        | ModelForm 확장                               | 폼의 공통 로직을 상속 구조로 재사용 |

------

### 핵심 개념 요약표

| 개념                       | 설명                                               |
| -------------------------- | -------------------------------------------------- |
| **upload_to**              | 업로드 파일의 하위 저장 경로 지정                  |
| **MEDIA_URL / MEDIA_ROOT** | 업로드 파일의 접근 URL과 실제 물리 저장소          |
| **AWS S3**                 | 대규모 파일 저장용 클라우드 서비스                 |
| **django-storages**        | S3와 Django를 연결하는 패키지                      |
| **BaseModelForm**          | 공통 로직을 상속 구조로 묶은 ModelForm 기반 클래스 |
| **boto3**                  | AWS API를 호출하기 위한 Python SDK                 |

------

### 핵심 단답식 퀴즈

1. `upload_to`의 경로는 어떤 설정을 기준으로 지정되는가?

   → **`MEDIA_ROOT`**

2. 사용자별 폴더로 이미지가 저장되게 하려면 어떤 함수를 사용해야 하는가?

   → **함수형 `upload_to` (ex. `user_directory_path`)**

3. AWS S3와 Django를 연결하기 위해 필요한 패키지는?

   → **`django-storages` + `boto3`**

4. `DEFAULT_FILE_STORAGE` 설정의 역할은?

   → **Django가 파일을 저장할 기본 백엔드를 지정**

5. `BaseModelForm`을 사용하는 가장 큰 목적은?

   → **공통 로직 재사용 및 일관된 폼 처리**

6. S3와 함께 사용하여 전송속도를 높여주는 AWS 서비스는?

   → **CloudFront**

------