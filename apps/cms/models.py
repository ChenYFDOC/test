from django.db import models


class LeftMenu(models.Model):
    name = models.CharField(max_length=32, verbose_name='菜单名称')
    sort = models.IntegerField(verbose_name='显示顺序')
    _class = models.ForeignKey('MenuClass', default='1', on_delete=models.CASCADE, verbose_name='所属分类')
    url = models.CharField(max_length=256, default='/', verbose_name='地址')

    class Meta:
        verbose_name_plural = '左侧菜单'

    def __str__(self):
        return self.name


class MenuClass(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='分类名称')
    sort = models.IntegerField()

    class Meta:
        verbose_name_plural = '菜单分类'

    def __str__(self):
        return self.name
