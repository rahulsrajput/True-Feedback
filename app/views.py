from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from usermanage.models import Customer
from django.contrib.auth.models import User
from .models import Comment

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/dashboard/')
    else:
        return render(request, 'app/home.html')



def dashboard(request):
    if request.user.is_authenticated:
        user = request.user
        obj = Customer.objects.get(user=user)

        comment_objects = Comment.objects.filter(customer=obj)
        # print(comment_objects)

        if request.method == 'POST':
            data = request.POST
            status = data['status']
            # print(status)

            if status.lower() == 'true':
                obj.status = True
                obj.save()
            elif status.lower() == 'false':
                obj.status = False
                obj.save()
            else:
                messages.success(request, "You can only type 'True' & 'False'")

        
        context = {
            'user':user,
            'status':obj.status,
            'comment_objects':comment_objects
        }
        return render(request, 'app/dashboard.html',context)

    else:
        return HttpResponseRedirect('/')



def anonymous(request, user):

    if request.method == 'POST':
        try:
            username_obj = User.objects.get(username=user)
            obj = Customer.objects.get(user=username_obj)
        except:
            messages.success(request, 'User not found')
            return render(request, 'app/anonymous.html',context={'user':user})

        
        if obj is not None:
            if obj.status is True:
                data = request.POST
                message = data['message']
                Comment.objects.create(customer = obj, message=message).save()
                # print(obj)
            else:
                messages.success(request, 'User not accepting feedback')


    context = {
        'user':user
    }
    return render(request, 'app/anonymous.html',context)




def deleteFeedback(request, comment):
    if request.method == 'POST':
        obj = Comment.objects.get(uid=comment)
        # print(obj)
        obj.delete()
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/dashboard/')
    



def error_404_view(request, exception):
    return render(request, 'error404.html')