from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.views import View


def main(request):
    dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render(request, 'main/index.html', {'dt': dt})
    # return HttpResponse('Hello! You in main page! Coming soon!')


def redirect_main(request):  # Redirect from / => main App
    return redirect('main_page')
