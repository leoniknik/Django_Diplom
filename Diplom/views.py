from django.shortcuts import render, HttpResponseRedirect
from Diplom.models import User
from Diplom.authorization import Auth


def home(request):
    try:
        return render(request, 'main.html')
    except Exception as e:
        print(e)
        return render(request, 'main.html')


def signin(request):
    try:
        if request.method == 'GET':
            return render(request, 'signin.html')
        elif request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            user = Auth().authenticate(email, password)
            if user is not None:
                return render(request, "temp.html")
            else:
                return render(request, 'signin.html')
    except Exception as e:
        print(e)
        return render(request, 'signin.html')


def signup(request):
    try:
        if request.method == 'GET':
            return render(request, 'signup.html')
        elif request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            repeat_password = request.POST['repeat_password']
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            phone = request.POST['phone']
            position = request.POST['position']
            if password != repeat_password:
                return render(request, 'signup.html')
            else:
                User.objects.create_user(email, password, firstname, lastname, phone, position)
                return render(request, 'signin.html')
    except Exception as e:
        print(e)
        return render(request, 'signup.html')
