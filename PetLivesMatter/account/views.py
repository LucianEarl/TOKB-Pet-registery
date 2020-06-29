from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from account.forms import SignUpForm


def signup_view(request):
    context = {}
    if request.POST:
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['signup_form'] = form
    else:
        form = SignUpForm()
        context['signup_form'] = form
    return render(request, 'account/signup.html', context)
