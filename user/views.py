from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
from django.contrib import messages
"""
1.In order to use our newly created UserForm, we need to import it in our views.py file
2.Within our register view, first, we check if the form method is a POST request.
If it is, we then create an instance of the imported RegisterForm, pass it the values inputted into the form and store it in a variable called form. 
3.Next, we check if the form is valid. If it is, we then save the form and redirect to the Home page.
4.However, if the request is not a POST request, we just create an instance of the empty RegisterForm.
5.Finally, we pass in the form variable as a context dictionary in order to render our RegisterForm within our template.
"""

def registerUser(request):
    form = RegisterForm()
    context = {'form':form}

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            user.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)            
            messages.success(request, 'User Created successfully')
            return redirect('home')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
        form = RegisterForm()
    return render(request, 'user/register.html', context)




def home(request):
    return render(request, 'user/home.html')