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

### Model 등록

* `blog/admin.py`에서 관리자 페이지 관리
* 위에서 만든 `Post` 모델을 관리자 페이지를 통해 사용하려면 `blog/admin.py` 에 등록해야함

- - -

## 뷰

### View 만들기

* `blog/views.py`에 뷰 만들기
* 뷰는 함수 형태로 작성되며 `request`를 인자로 받아 `response`를 반환함
* 사용자들이 `request`를 보낼 수 있도록 `URL`를 할당해주어야 함

### URL 설정

* `config/urls.py`에 `url` 객체를 만들어 할당하여 원하는 주소에 내용을 표시함
* `url(정규표현식, 뷰)`

- - -

## 템플릿

### Template 생성

* `templates`폴더 안에 모든 템플릿을 모아두고 각 앱이 사용할 템플릿들을 모아두는 폴더를 생성
* 그 이유는 규모가 커졌을 때 템플릿 파일들을 분류해서 수월하게 관리하기 위함

- - -

## ORM

### 객체 관계 매핑(Object Realtional Mapping)

* 정의 : 데이터베이스와 객체지향 프로그래밍 언어 간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법

### shell_plus 설치

* django 전용 shell로 `config/settings.py`의 `INSTALLED_APPS`에 `django_extensions` 추가
* `django_extensions`를 통해 필요한 패키지와 모듈을 자동으로 import 해주는 `shell_plus` 사용

### QuerySet 다루기

* `Post.objects.all()`로 `Post` 모델의 모든 객체 확인하기
* `Users.objects.all()`로 `Users` 모델의 모든 객체 확인하기
* 위 ORM은 내부적으로 `SQL`을 담고 있으며 이를 통해 데이터를 객체처럼 다룰 수 있음

### 객체 생성하기

```python
author = User.objects.get(username='example_id')
create(author=author, title='title', content='content')
```

### 객체 필터링하기

* `filter()`를 통해 쿼리셋의 객체 필터링
* 필터는 여러 개를 중복으로 적용 가능
* `Post.objects.filter(content__contains='blog')`로 `content`에 `blog`라는 문자열이 포함된 객체 조회
* `Post.objects.filter(title__contains='ORM')`로 `title`에 `ORM`이라는 문자열이 포함된 객체 조회

### 객체 정렬하기

* `order_by()`를 사용해 기준을 지정하여 객체를 정렬

### 쿼리셋 필터 중복 적용

* `Post.objects.filter(title__contains='django').order_by('published_date')` 처럼 여러 필터를 중복 적용 가능

### 객체 삭제

* `delete()`로 객체 삭제 가능

```python
post = Post.objects.get(title='ORM Test')
post.delete()
```

