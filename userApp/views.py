from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.views import View

from userApp.models import Xodim


class XodimView(View):
    def get(self, request):
        xodimlar = Xodim.objects.all()
        context = {
            'xodimlar': xodimlar
        }
        return render(request, 'xodim.html', context=context)
