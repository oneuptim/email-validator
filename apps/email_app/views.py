from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Email
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

def index(request):

	return render(request, 'email_app/index.html')

def process(request):

	if request.method == 'POST':
		email = request.POST['email']

		if len(email) < 1:
 			messages.add_message(request, messages.WARNING, 'Email cannont be blank!')

		elif  not EMAIL_REGEX.match(email):
			messages.add_message(request, messages.WARNING, 'Please enter valid email')


		else:
			Email.objects.create(email = request.POST['email'])
			return redirect('/success')

		return redirect('/')

def success(request):
	messages.add_message(request, messages.SUCCESS, 'Email added successfully.')
	emails = Email.objects.all().order_by('-created_at')
	context = {
		'emails': emails
		}
	print emails, "******************************************"
	print emails.count()
	return render(request, 'email_app/success.html' , context)

# Create your views here.
