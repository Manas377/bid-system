from accounts.models import User
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from django.views.generic import View
# Create your views here.
import time
from datetime import date, datetime, timedelta

from .forms import UserRegisterForm

# from lead.forms import LeadFilterForm


from django.db.models import Avg


def login(request):
    form = UserCreationForm()
    return render(request, 'accounts/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi you are now a member. Please Login with your Credentials.')
            return redirect('accounts:login')
    else:
        form = UserRegisterForm
    return render(request, 'accounts/register.html', {'form': form})