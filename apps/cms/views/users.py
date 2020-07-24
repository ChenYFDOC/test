from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from apps.users.models import User, Role, Permission
import copy


@login_required
def index(request):
    return TemplateResponse(request, 'users/index.html')


@login_required
def usermanager(request):
    userList = User.objects.values('username', 'group_id__name', 'role_id__title', 'is_active', 'phone', 'email',
                                   'created_on')
    return TemplateResponse(request, 'users/usermanager.html',
                            context={'usermessages': userList, 'items': ['姓名', '邮箱', '手机']})


@login_required
def role(request):
    roleList = Role.objects.values('title', 'permission_id__title', 'permission_id__url__name',
                                   'permission_id__menu_id__name')
    list(roleList).sort(key=lambda item: item['title'])
    struct = [1, ]
    flag = 0
    length = len(roleList)
    for index in range(length):
        try:
            if roleList[index]['title'] == roleList[index + 1]['title']:
                struct[flag] += 1
            else:
                struct.append(1)
                flag += 1
        except:
            pass
    roles = []

    def roleAppend(added, add):
        added['permission_id__title'].append(add['permission_id__title'])
        added['permission_id__url__name'].append(add['permission_id__url__name'])
        added['permission_id__menu_id__name'].append(add['permission_id__menu_id__name'])

    sum = 0
    for index, time in enumerate(struct):
        sum += time
        roles.append(roleList[sum - 1])
        roles = copy.deepcopy(roles)
        roles[index]['permission_id__title'] = []
        roles[index]['permission_id__url__name'] = []
        roles[index]['permission_id__menu_id__name'] = []
    count = 0
    i = 0
    time = struct[i]
    for role in roleList:
        if count < time:
            roleAppend(roles[i], role)
            count += 1
        else:
            try:
                roleAppend(roles[i + 1], role)
                count = 1
                i += 1
                time = struct[i]
            except:
                pass
    return TemplateResponse(request, 'users/role.html', context={'roleList': roles})


@login_required
def permissions(request):
    permList = Permission.objects.values('title', 'url__name', 'menu_id__name')
    return TemplateResponse(request, 'users/permissions.html', context={'permList': permList})
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
