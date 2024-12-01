from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)
    title = models.CharField(max_length = 100)
    description = models.TextField(null = True, blank = True)
    completed = models.BooleanField(default = False)
    createdDate = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title
    # このクラスのオブジェクトを使えばこれが自動的に呼ばれて、このオブジェクトのタイトルが見れる！
    # 慣習的なもの　定義しておく

    class Meta:
        ordering = ["completed"]
    # メタ情報　情報に関する情報　だからそれとしてオーダーを定義する