from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
#from .forms import LoginForm,UserRegistrationForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import UserEditForm,ProfileEditForm,UserRegistrationForm,LoginForm
from posts.models import Post
# Create your views here.
def user_login(request):
    if request.method == "POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            data=form.cleaned_data
            user=authenticate(request,username=data['username'],password=data['password'])
            if user is not None:
                login(request,user)
                return redirect('feed')
            else:
                return HttpResponse("invalid credentials")    

    else:
        
        form=LoginForm
        return render(request,'users/login.html',{'form':form})
@login_required
def index(request):
    # to access currently logged in user
    current_user=request.user
    posts=Post.objects.filter(user=current_user)
    profile=Profile.objects.filter(user=current_user).first()
    return render(request,'users/index.html',{'posts':posts,'profile':profile})

def register(request):
    if request.method =="POST":
        user_form=UserRegistrationForm(request.POST)
        if user_form.is_valid():
            newuser=user_form.save(commit=False)
            newuser.set_password(user_form.cleaned_data['password'])
            newuser.save()
            Profile.objects.create(user=newuser)
            return redirect('login')
            #return redirect('login')
    else:
        user_form = UserRegistrationForm()
    return render(request,'users/register.html',{'user_form':user_form})

@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,'users/edit.html',{'user_form': user_form, 'profile_form': profile_form})





def user_logout(request):
   
    logout(request)
   
    return render(request, 'users/logout.html')
