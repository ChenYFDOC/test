import uuid
from django.db import models


class Permission(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, verbose_name='uuid')
    title = models.CharField(max_length=32, verbose_name='标题')
    url = models.CharField(max_length=128, verbose_name='路径')
    name = models.CharField(max_length=32, unique=True, verbose_name='URL别名')
    menu_id = models.ForeignKey('cms.LeftMenu', null=True, on_delete=models.SET_NULL, verbose_name='所属一级菜单')
    pid = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='关联的权限')

    class Meta:
        verbose_name_plural = '权限'

    def __str__(self):
        return self.title
