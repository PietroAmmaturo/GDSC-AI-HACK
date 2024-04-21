from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages 
from .forms import SignUpForm, EditProfileForm 
from django.core.files.storage import FileSystemStorage
from .models import Course
import uuid
from api import settings

# Create your views here.
def home(request):
    folder = settings.MEDIA_ROOT
    if request.method == 'POST' and request.FILES['file']:
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage(location=folder) #defaults to   MEDIA_ROOT
        file_uuid = uuid.uuid4()
        file_name = f"{file_uuid}.pdf"
        actual_file_name = fs.save(file_name, uploaded_file)
        course_dict = {
			"title": "Test title",
			"description": "Test description",
			"chapters": [
				{
					"title": "Chapter 1",
					"description": "breve frase per introdurre il capitolo",
					"concepts": [
						{
							"name": "Concept 1",
							"description": "breve frase per introdurre il concetto, tipo bullet point"
						},
						{
							"name": "Concept 2",
							"description": "breve frase per introdurre il concetto, tipo bullet point"
						}
					],
					"questions": [
						{
							"question": "Question 1",
							"options": ["Option 1", "Option 2", "Option 3", "Option 4"],
							"answer": "Option 1",
       						"explanation": "explanation example"
						},
						{
							"question": "Question 2",
							"options": ["Option 1", "Option 2", "Option 3", "Option 4"],
							"answer": "Option 1",
       						"explanation": "explanation example"
						},
						{
							"question": "Question 3",
							"options": ["Option 1", "Option 2", "Option 3", "Option 4"],
							"answer": "Option 3",
       						"explanation": "explanation example"
						}
					]
				},
				{
					"title": "Chapter 2",
					"description": "breve frase per introdurre il capitolo",
					"concepts": [
						{
							"name": "Concept 1",
							"description": "breve frase per introdurre il concetto, tipo bullet point"
						},
						{
							"name": "Concept 2",
							"description": "breve frase per introdurre il concetto, tipo bullet point"
						}
					],
					"questions": [
						{
							"question": "Question 1",
							"options": ["Option 1", "Option 2", "Option 3", "Option 4"],
							"answer": "Option 1",
							"explanation": "explanation example"
						}
					]
				},
				{
					"title": "Chapter 3",
					"description": "breve frase per introdurre il capitolo",
					"concepts": [
						{
							"name": "Concept 1",
							"description": "breve frase per introdurre il concetto, tipo bullet point"
						},
						{
							"name": "Concept 2",
							"description": "breve frase per introdurre il concetto, tipo bullet point"
						}
					],
					"questions": [
						{
							"question": "Question 1",
							"options": ["Option 1", "Option 2", "Option 3", "Option 4"],
							"answer": "Option 1",
       						"explanation": "explanation example"
						}
					]
				}
			],
			"source_file": actual_file_name
		}
        new_course = Course.objects.create(
			title=course_dict['title'],
			description=course_dict['description'],
   			chapters=course_dict['chapters'],
			source_file=course_dict['source_file']
		)
        # call function to create course
        return redirect('course/?course_id=' + str(new_course.id))
    else:
        return render(request, 'home.html', {})

def course (request):
    # Retrieve parameters from request.GET
    course_id = request.GET.get('course_id')
    course = Course.objects.get(id=course_id)
    context = {'course': course}
    return render(request, 'course.html', context)

def dashboard (request):
    # Retrieve parameters from request.GET
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'dashboard.html', context)

def login_user (request):
	if request.method == 'POST': #if someone fills out form , Post it 
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:# if user exist
			login(request, user)
			messages.success(request,('Youre logged in'))
			return redirect('home') #routes to 'home' on successful login  
		else:
			messages.success(request,('Error logging in'))
			return redirect('login') #re routes to login page upon unsucessful login
	else:
		return render(request, 'login.html', {})

def logout_user(request):
	logout(request)
	messages.success(request,('Youre now logged out'))
	return redirect('home')

def register_user(request):
	if request.method =='POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request,user)
			messages.success(request, ('Youre now registered'))
			return redirect('home')
	else: 
		form = SignUpForm() 

	context = {'form': form}
	return render(request, 'register.html', context)

def edit_profile(request):
	if request.method =='POST':
		form = EditProfileForm(request.POST, instance= request.user)
		if form.is_valid():
			form.save()
			messages.success(request, ('You have edited your profile'))
			return redirect('home')
	else: 		#passes in user information 
		form = EditProfileForm(instance= request.user) 

	context = {'form': form}
	return render(request, 'edit_profile.html', context)



def change_password(request):
	if request.method =='POST':
		form = PasswordChangeForm(data=request.POST, user= request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.success(request, ('You have edited your password'))
			return redirect('home')
	else: 		#passes in user information 
		form = PasswordChangeForm(user= request.user) 

	context = {'form': form}
	return render(request, 'change_password.html', context)