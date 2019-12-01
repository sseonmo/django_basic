from django.contrib import admin
from .models import Fcuser

# Register your models here.
class FcuserAdmin(admin.ModelAdmin):
	# 보여줄 항목
	list_display = ('username', 'password')

admin.site.register(Fcuser, FcuserAdmin)
