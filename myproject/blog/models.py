from django.conf import settings
from django.db import models


class Post(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL)만 사용 시
    # on_delete 속성이 필요하다는 에러를 내보냄)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title