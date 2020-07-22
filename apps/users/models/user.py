import uuid

from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


# Create your models here.
class UserManager(BaseUserManager):
    def _create_user(self, **extra_fields):
        if not extra_fields['username']:
            raise ValueError("请填入用户名！")
        try:
            groups = extra_fields.pop('groups')
            user_permissions = extra_fields.pop('user_permissions')
            user = self.model(**extra_fields)
            user.set_password(extra_fields['password'])
            user.groups.set(groups)
            user.user_permissions.set(user_permissions)
        except:
            user = self.model(**extra_fields)
            user.set_password(extra_fields['password'])
        user.save()
        return user

    def create_user(self, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(**extra_fields)

    def create_superuser(self, **fields):
        fields.setdefault('is_superuser', True)
        return self._create_user(**fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    username = models.CharField(max_length=32, verbose_name='用户名', unique=True)
    email = models.EmailField(verbose_name='邮件')
    phone = models.CharField(max_length=20, verbose_name='电话')
    group_id = models.ForeignKey('users.Group', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='部门')
    role_id = models.ForeignKey('users.Role', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='用户角色')
    is_active = models.BooleanField(default=True, verbose_name='活动状态')
    is_deleted = models.BooleanField(default=False, verbose_name='删除状态')
    created_by = models.CharField(max_length=32, default=username, verbose_name='创建人')
    created_on = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_on = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_staff = models.BooleanField(default=True, verbose_name='是否是员工')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone']
    objects = UserManager()

    class Meta:
        verbose_name_plural = '用户'

    def __str__(self):
        return self.username
