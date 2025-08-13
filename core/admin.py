from django.contrib import admin

# Register your models here.
# core/admin.py
from .models import Post # Import model Post của bạn

# Đăng ký model Post với trang admin
admin.site.register(Post)