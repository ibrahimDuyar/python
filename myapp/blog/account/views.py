from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, logout, authenticate,update_session_auth_hash
from account.form import LoginUserForm, UserCreate, UserChange
from account.models import CastomUserModel
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.


def login_user(request):

    if request.method == 'POST':

        form = LoginUserForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            return redirect('index')
    

    else:
        form = LoginUserForm()
    


    return render(request, 'form.html', {
        'form':form,
    })


def logout_user(request):

    logout(request)
    return redirect('index')




def register_user(request):

    if request.method == 'POST':

        form = UserCreate(request.POST)

        if form.is_valid():

            form.save()

            return redirect('index')
    

    else:
        form = UserCreate()
    


    return render(request, 'form.html',{
        'form':form,
    })


def update_user(request):

    if request.method == 'POST':

        form = UserChange(request.POST, request.FILES, instance=request.user)

        if form.is_valid():

            form.save()

            return redirect('index')
    

    else:
        form = UserChange(instance=request.user)
    


    return render(request, 'form.html',{
        'form':form,
    })


def password_change(request):

    if request.method == "POST":

        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():

            kullanici = form.save()

            update_session_auth_hash(request, kullanici)

            return redirect('index')
    
    else:
        form = PasswordChangeForm(request.user)
    

    return render(request, 'form.html',{
        'form':form,
    })