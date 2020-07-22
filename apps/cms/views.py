from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from apps.users.models import User


@login_required
def index(request):
    return TemplateResponse(request, 'index.html')


@login_required
def usermanager(request):
    userList = User.objects.values('username', 'group_id__name', 'role_id__title', 'is_active', 'phone', 'email',
                                   'created_on')
    return TemplateResponse(request, 'usermanager.html', context={'usermessages': userList})

# @login_required(login_url=reverse('login'))
# def get_user_info(request):
#     lable_map = {
#         '真实姓名': 'name',
#         '性别': 'gender',
#         '邮箱': 'email',
#         '手机号': 'phone'
#     }
#     page = int(request.GET.get('page'))
#     lable = '-' + lable_map[request.GET.get('lable')]
#     query_set = models.UserInfo.objects.values().order_by(lable)[(page - 1) * 10:page * 10]
#     return JsonResponse(list(query_set), safe=False)
