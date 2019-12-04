from django.db import models

# Create your models here.


class Fcuser(models.Model):
    # filed : username, password, registered_dttm
    DoesNotExist = None
    objects = None
    username = models.CharField(max_length=32, verbose_name='사용자명')
    # email validation check 포함되어있다.
    usermail = models.EmailField(max_length=128, verbose_name='사용자이메일')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name='등록시간')

    def __str__(self):
        return self.username

    class Meta:
        # table name 지정
        db_table = 'fastcampus_fcuser'
        verbose_name = '패스트캠퍼스 사용자'
        verbose_name_plural = '패스트캠퍼스 사용자들'
