from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from . import models
from .forms import LoginForm
def index(request):
	return render(request, 'index.html', {'title': 'Вход/Кіру'})

def user_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(username=cd['username'], password=cd['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('/lesson1/')
				else:
					return HttpResponse('Disabled account')

		else: 
			return HttpResponse('Invalid login or password.')
	else:
		return HttpResponse('Error')

def view_lesson1(request):
	if request.user.is_authenticated:
		return render(request, 'lesson1.html', {'title': 'Бірінші сабақ'})
	else:
		return redirect('/')

def view_lesson2(request):
	if request.user.is_authenticated:
		return render(request, 'lesson2.html', {'title': 'Екінші сабақ'})
	else:
		return redirect('/')
	

def view_lesson3(request):
	if request.user.is_authenticated:
		return render(request, 'lesson3.html', {'title': 'Үшінші сабақ'})
	else:
		return redirect('/')
	