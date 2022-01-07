from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
"""
1.We are importing the following dependencies from Django. They include the Django forms, the default User model and the UserCreation form.
2.Next create a class that inherits from the UserCreationForm. We will name our class RegisterForm.
3.Note that the default UserCreationForm provides just three parameters, the username, password1 and password2.
However we can modify this to include more fields.
4.To do this, let's assume we want to add three new fields. A first name, last name and an email address which do not originally come included.
All we need to do is to add more form fields, which bear similar attributes to the model fields.
5.Next, we add a Meta class to which has two functions:
1) To indicate which model we are using which in this case is the default user model
2) To show which fields we want to include in our final form and what order they should be rendered on our page.
6.After which we then include the default three(3) fields that come with the user creation form which are named as 'username', 'password1' and 'password2'
"""
class RegisterForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']