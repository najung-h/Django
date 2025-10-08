django의 sqlite에서 none, blank, null은 무슨 차이가 있어?



Django의 **SQLite** 데이터베이스에서 모델 필드를 정의할 때 사용되는 `None`, `blank`, `null`은 다음과 같은 차이가 있습니다.



## 주요 차이점



| 속성             | Django 모델에서의 의미                                       | 데이터베이스 (SQLite)에서의 의미                             |
| ---------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **`null=True`**  | 필드에 값이 없을 때 **데이터베이스**에 **`NULL`**로 저장되도록 허용 | 데이터베이스 테이블 컬럼에 **`NULL`** 값 저장을 허용 (기본값: `False`) |
| **`blank=True`** | 필드에 값이 없을 때 **폼(Form)** 유효성 검사를 통과하도록 허용 | 데이터베이스 스키마에 직접적인 영향을 주지 않음 (기본값: `False`) |
| **`None`**       | Python에서 **값의 부재**를 나타내는 값                       | `null=True`일 때 데이터베이스에 **`NULL`**로 저장되는 실제 값 |

<hr>



## 상세 설명





### 1. `null` (데이터베이스 관련)



- **`null=True`**로 설정하면, 해당 필드에 값이 없을 때 **SQLite 데이터베이스**에 **`NULL`** 값으로 저장될 수 있도록 허용합니다.
- **Django의 기본값은 `False`**입니다. 즉, 기본적으로 모든 필드는 `NOT NULL` 제약 조건을 가집니다.
- 문자열 기반 필드 (`CharField`, `TextField`)에서는 데이터 일관성을 위해 보통 `null=False`를 유지하고 대신 **`blank=True`**와 빈 문자열 `''`을 사용하는 것이 Django의 관례입니다. 하지만 다른 필드 타입 (예: 숫자, 날짜, 외래 키)에서는 `null=True`를 자주 사용합니다.



### 2. `blank` (유효성 검사 관련)



- **`blank=True`**로 설정하면, 해당 필드가 **Django의 관리자 페이지나 폼**을 통해 데이터를 입력받을 때 **빈 채로 제출되는 것을 허용**합니다. 즉, 폼 유효성 검사를 통과시킵니다.
- **Django의 기본값은 `False`**입니다.
- `blank` 속성은 데이터베이스의 제약 조건과는 **무관**하며, 오직 데이터 유효성 검사(Validation) 단계에서만 작동합니다.



### 3. `None` (Python 값)



- **Python 자체에서 '값이 없음'**을 나타내는 상수입니다.
- Django 모델 인스턴스에서 필드에 아무 값도 할당되지 않았음을 나타낼 때 사용됩니다.
- 모델 인스턴스를 저장할 때, 만약 필드에 **`null=True`**가 설정되어 있고 그 필드의 값이 Python의 **`None`**이라면, SQLite 데이터베이스에는 **`NULL`**이라는 특수한 값으로 기록됩니다.

<hr>



## 예시 비교



Python

```
from django.db import models

class MyModel(models.Model):
    # 1. 필수 입력 필드 (기본값)
    # 데이터베이스: NOT NULL, 폼: 반드시 입력 필요
    field_a = models.CharField(max_length=10)

    # 2. 폼에서만 선택 사항인 필드
    # 데이터베이스: NOT NULL (빈 문자열 ''로 저장), 폼: 입력하지 않아도 됨
    field_b = models.CharField(max_length=10, blank=True)

    # 3. 데이터베이스에서 선택 사항인 필드 (숫자형 예시)
    # 데이터베이스: NULL 허용, 폼: 반드시 입력 필요
    field_c = models.IntegerField(null=True)

    # 4. 폼과 데이터베이스 모두에서 선택 사항인 필드 (문자열형 예시)
    # 데이터베이스: NULL 허용, 폼: 입력하지 않아도 됨
    # 문자열 필드에서는 null=True와 blank=True를 함께 설정하는 것이 권장되지 않음 (혼란 야기 가능성 때문)
    field_d = models.CharField(max_length=10, null=True, blank=True)

    # 5. 폼과 데이터베이스 모두에서 선택 사항인 필드 (숫자형 예시)
    # 데이터베이스: NULL 허용, 폼: 입력하지 않아도 됨
    field_e = models.IntegerField(null=True, blank=True)
```

만약 `field_e`에 값이 입력되지 않고 저장되면,

- Python 모델 인스턴스에서는 `field_e`의 값이 **`None`**이 됩니다.
- SQLite 데이터베이스 테이블에는 **`NULL`** 값으로 저장됩니다.