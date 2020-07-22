from django.utils.deprecation import MiddlewareMixin
from ..models import LeftMenu, MenuClass


class DefaultRander(MiddlewareMixin):
    def process_template_response(self, request, response):
        leftMenu = list(LeftMenu.objects.values())
        leftMenu.sort(key=lambda item: int(item['sort']))
        menuClass = list(MenuClass.objects.values())
        menuClass.sort(key=lambda item: int(item['sort']))
        for mclass in menuClass:
            mclass['menu'] = []
            for menu in leftMenu:
                if mclass['id'] == menu['_class_id']:
                    mclass['menu'].append(menu)
        try:
            response.context_data['left_menu'] = menuClass
        except:
            response.context_data = {'left_menu': menuClass}
        return response
