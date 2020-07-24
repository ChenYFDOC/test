from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse


@login_required
def key_type(request):
    if request.method == 'GET':
        return TemplateResponse(request, 'license/key_type.html', context={'items': ['asddas', 'asdase', 'dfgdfg']})
