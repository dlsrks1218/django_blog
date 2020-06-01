# 장고를 활용한 블로그 서비스 배포

## 프로젝트 구조

\`
myproject   # 프로젝트 폴더
    ├── README.md
    ├── blog    # 앱 폴더
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── config  # 설정 폴더
    │   ├── __init__.py
    │   ├── __pycache__
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── db.sqlite3
    └── manage.py
\`

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
\`
[글]
 ├─ 글쓴이  
 ├─ 글 제목  
 ├─ 글 내용
 ├─ 글 생성 시간
 └─ 글 발행 시간
\`

* blog/modls.py에 글 객체(모델) 생성
\`
from django.conf import settings
from django.db import models

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
\`
    * 각 속성이 데이터베이스의 필드가 됨
