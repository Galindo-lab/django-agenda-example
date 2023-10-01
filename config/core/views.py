from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404

from django.views import View


def index(request: any) -> HttpResponse:
    return render(
        request=request,
        template_name='index.html'
    )


def monitor(request: any) -> HttpResponse:
    return render(
        request=request,
        template_name='monitor.html'
    )

def clinic(request: any) -> HttpResponse:
    return render(
        request=request,
        template_name='doctor/clinic.html'
    )

# class Login(View):
#     template_name = 'login.html'

#     def get(self, request, *args, **kwargs) -> HttpResponse:
#         print("a")
#         return render(request, self.template_name, {
#             'form': UserLoginForm()
#         })

#     def post(self, request, *args, **kwargs) -> HttpResponse:

#         print(request.user)

#         form = UserLoginForm(request.POST)

#         if form.is_valid():
#             print('c')
#             return HttpResponseRedirect('index')

#         # mostrar los errores en el form
#         print('d')
#         return render(request, self.template_name, {
#             'form': form
#         })
