# django basic

## 가상환경설정

1. 가상환경설치 - pip3 install virtualenv
1. 가상환경생성 - virtualenv fcdjango_venv
1. 현재사용할 가상환경설정 - source bin/activate

## django

-   설치 : `pip3 install django`
-   프로젝트 생성 : `django-admin startproject fc_communtiy`
-   app 생성  
    `django-admin startapp board`  
    `django-admin startapp fcuser`

## django app 등록

```python
# setting.py에 app 추가
INSTALLED_APPS = [
    ...,
    'board',
    'fcuser',
]
```

## django Model 생성

```python
from django.db import models

# Create your models here.
class Fcuser(models.Model):
	# filed : username, password, registered_dttm
	username = models.CharField(max_length=64, verbose_name='사용자명')
	password = models.CharField(max_length=64, verbose_name='비밀번호')
	registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

	class Meta:
		# table name 지정
		db_table = 'fastcampus_fcuser'
```

-   `makimigrations`- models.py에서 적용한 변경사항이나 추가된 혹은 삭제된 사항들을 감지하여 파일로 생성
    -   명령어실행 : python3 manage.py makemigrations
-   `migrate` - 적용되지 않은 migrations들을(설정값들을) 적용시키는 역할
    -   명령어실행 : python3 manage.py migrate

## django admin

-   기본적으로 setting.py 에 활성화 되어있음
-   도메인/admin 으로 접속( default urls.py에 설정되어있음)

### 계정생성

-   python3 manage.py createsuperadmin
    1. 명령어 실행
    1. name, email, password 지정 / admin, admin@admin.com, 12qwaszx!@
-   run server
    -   python3 manage.py runserver <0.0.0.0:port>

# Tip

-   django 버전확인 : python3 -m django --version
