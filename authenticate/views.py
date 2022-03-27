from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.shortcuts import render, redirect
from .forms import SignUpForm, EditProfileForm, ChangePasswordForm


def authentication_home(request):
    return render(request, 'authenticate/home.html')


def login_user(request):
    sender = request.session.get('sender')
    if request.user.is_authenticated:
        if sender == "website":
            if request.user.is_authenticated:
                return redirect('member_area')
        else:
            if request.user.is_authenticated:
                return redirect('laws')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if sender == "website":
                login(request, user)
                # messages.success(request, 'You have been logged in successfully')
                request.session['login_status'] = True
                return redirect('member_area')
            else:
                login(request, user)
                # messages.success(request, 'You have been logged in successfully')
                request.session['login_status'] = True
                return redirect('laws')
        else:
            messages.warning(request, "Username or Password is incorrect !!")
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html')


def login_user_quicksearch(request):
    print(request.session.get('searchstring'))
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request, 'You have been logged in successfully')
            request.session['login_status'] = True
            return redirect('getlaw')
        else:
            messages.warning(request, "Username or Password is incorrect !!")
            return redirect('login_user_quicksearch')
    else:
        return render(request, 'authenticate/login_quicksearch.html')


def logout_user(request):
    logout(request)
    # messages.success(request, "Logged out successfully")
    request.session['login_status'] = False
    return redirect('home')


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            form = SignUpForm(request.POST)
    else:
        form = SignUpForm()
    context = {
        'form': form,
    }
    return render(request, 'authenticate/register.html', context)


def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile Updated Successfully")
            return redirect('home')
    else:
        form = EditProfileForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'authenticate/edit_profile.html', context)


def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password Changed Successfully")
            return redirect('home')
    else:
        form = ChangePasswordForm(user=request.user)
        print(form)
    context = {
        'form': form,
    }
    return render(request, 'authenticate/change_password.html', context)
