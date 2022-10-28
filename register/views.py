from django.shortcuts import render, redirect
from .forms import NewUser
from django.contrib import messages

def register_request(request):
    if request.method == "POST":
        form = NewUser(request.POST)
        if form.is_valid():
            # form.cleaned_data["username"]
            form.save()
            # messages.success(request, "Registration successful!")
            # return redirect('homepage') # Falta definir HOMEPAGE
        # messages.error(request, "Unsuccessful registration. Invalid information")
    else:
        form = NewUser()

    return render(request, template_name='register/register.html', context={"form":form})

def homepage(request):
    return render(request, template_name='register/user_homepage.html')