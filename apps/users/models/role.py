from django.db import models
import uuid
from .permission import Permission


class Role(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, verbose_name='uuid')
    title = models.CharField(max_length=32, verbose_name='角色名称')
    permission_id = models.ForeignKey(Permission, null=True, on_delete=models.SET_NULL, verbose_name='权限')

    class Meta:
        verbose_name_plural = '角色'

    def __str__(self):
        return self.title
