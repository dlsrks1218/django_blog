# 장고를 활용한 블로그 서비스 배포

## 프로젝트 구조

```bash
myproject   # 프로젝트 폴더
    ├── README.md
    ├── blog    # 앱 폴더
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── config  # 설정 폴더
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── db.sqlite3
    └── manage.py
```

- - -

## 모델 생성

### MVC 패턴

* 모델 : 데이터베이스나 파일 등의 데이터 소스를 제어함
* 뷰 : 모델로부터 제공된 데이터를 반영하여 사용자에게 보여주게 되는 부분을 담당함
* 컨트롤러 : 사용자의 요청을 파악하여 그에 맞는 데이터를 모델에 의뢰하고, 그것을 뷰에 반영하여 사용자에게 제공함

### MTV 패턴

* 모델 : 데이터를 표현하는데 사용되며, Python 클래스 형식으로 정의함. 하나의 모델 클래스는 데이터베이스에서 하나의 테이블로 표현함
* 템플릿 : 사용자에게 보여지는 부분을 담당
* 뷰 : HTTP Request를 받아 HTTP Response를 리턴하는 컴포넌트로, 모델로부터 데이터를 읽거나 저장함

### Model

* 글 객체 -> 클래스

```bash
[글]
 ├─ 글쓴이  
 ├─ 글 제목  
 ├─ 글 내용
 ├─ 글 생성 시간
 └─ 글 발행 시간
```

* blog/models.py에 글 객체(모델) 생성
  * 각 속성이 데이터베이스의 필드가 됨
  
```python
from django.conf import settings
from django.db import models

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
```

- - -

## 데이터베이스

### Migrations

* 정의
Django의 모델에서 설정한 데이터베이스의 테이블 구조를 데이터베이스에 적용시키기 위한 기록한 것
* config/settings.py의 INSTALLED_APPS의 앱들이 필요로 하는 테이블을 데이터베이스에 생성 -> db.sqlite3 파일 생성
* `./manage.py makemigrations 앱이름` 결과 `migrations` 폴더에 데이터베이스 변경사항 정보가 기록됨
* `./manage.py migrate`로 전체 앱에 변경사항 적용

- - -

## 관리자 페이지

### 모델 등록

* `admin.py`에서 관리자 페이지 관리
* 위에서 만든 `Post` 모델을 관리자 페이지를 통해 사용하려면 `admin.py` 에 등록해야함

