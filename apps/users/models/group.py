import uuid

from django.db import models


class Group(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, verbose_name='uuid')
    name = models.CharField(max_length=32, verbose_name='部门名称')
    comment = models.CharField(max_length=200, verbose_name='备注')
    created_by = models.CharField(max_length=32, verbose_name='创建人')
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_on = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        verbose_name_plural = '部门'

    def __str__(self):
        return self.name
