from django.utils.deprecation import MiddlewareMixin
from ..models import LeftMenu


class DefaultRander(MiddlewareMixin):
    def process_template_response(self, request, response):
        ex_context = list(LeftMenu.objects.values())
        ex_context.sort(key=lambda item:int(item['sort']))
        try:
            response.context_data['left_menu'] = ex_context
        except:
            response.context_data = {'left_menu': ex_context}
        return response
