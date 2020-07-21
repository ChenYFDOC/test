from django.db import models


class LeftMenu(models.Model):
    name = models.CharField(max_length=32, verbose_name='菜单名称')
    sort = models.IntegerField(verbose_name='显示顺序')
    icon = models.CharField(max_length=256, blank=True, null=True, verbose_name='图标')
    url = models.CharField(max_length=256, default='/', verbose_name='地址')

    class Meta:
        verbose_name_plural = '左侧菜单'

    def __str__(self):
        return self.name
