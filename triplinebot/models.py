from django.db import models


class Location(models.Model):
    area = models.CharField(max_length=20)  # 地區
    name = models.CharField(max_length=100)  # 景點名稱
    address = models.CharField(max_length=500)  # 地址
