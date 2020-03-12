from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def fn_index(request):
    return render(request,'login.html')
def fn_login(request):
    print(request.POST)
    return HttpResponse('success')    