from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

#操作数据库的类，前端输入的数据写入数据库。

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(default="nickname",max_length=18)
    email = models.CharField(max_length=32)   # 邮箱

    def __str__(self):
        return "{}_{}".format(self.nickname,self.username,self.email)


class Plate(models.Model): # 多对多新方法
    title = models.CharField(max_length=16)
    users = models.ManyToManyField(to=User, related_name="plates")

    def __str__(self):
        return "板块：{}".format(self.title)

# class Moderator(models.Model): # 多对多老方法
#     user = models.ForeignKey(to=User,related_name="moderators")
#     plate = models.ForeignKey(to=Plate,related_name="moderators")

#     def __str__(self):
#         return "板块：{}，版主：{}".format(self.user,self,plate)

class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    users = models.ForeignKey(to=User,related_name="posts",on_delete=models.CASCADE)
    column = models.ForeignKey(to=Plate,related_name="posts",on_delete=models.CASCADE)
    createtime = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return "帖子：{}".format(self.title,)



class Reply(models.Model):
    user = models.ForeignKey(to=User,related_name="replys",on_delete=models.CASCADE)
    post = models.ForeignKey(to=Post,related_name="replys",on_delete=models.CASCADE)
    content = models.TextField()
    createtime = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return "回复：{}".format(self.content)
