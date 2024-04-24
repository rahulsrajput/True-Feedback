from django.shortcuts import render
from .forms import signIn_form, signUp_form
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Customer

# Create your views here.
def signIn(request):
    form  = signIn_form()
    
    if request.user.is_authenticated:
        return HttpResponseRedirect('/dashboard/')
    else:
        if request.method == 'POST':
            form = signIn_form(request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']

                user_object = authenticate(username=uname, password=upass)
                if user_object is not None:
                    login(request, user_object)
                    return HttpResponseRedirect('/dashboard/')
            

    context = {
        'form':form
    }
    return render(request, 'usermanage/signIn.html',context)




def logoutHandle(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')




def signUp(request):
    form = signUp_form()
    if request.user.is_authenticated:
        return HttpResponseRedirect('/dashboard/')
    
    else:
        if request.method == 'POST':
            form = signUp_form(request.POST)
            if form.is_valid():
                user = form.save()
                Customer.objects.create(user=user)
                return HttpResponseRedirect('/sign-in/')


    context = {
        'form':form
    }
    return render(request, 'usermanage/signUp.html',context)