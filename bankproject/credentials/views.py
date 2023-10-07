from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Form


# Create your views here.
def index():
    return redirect('/')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid credentials")
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email Taken")
                return redirect('register')
            user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                            last_name=last_name, email=email)

            user.save()
            return redirect('login')
        else:
            messages.info(request, "password not matching")
            return redirect('register')
            return redirect('/')
    return render(request, "register.html")


def form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        age = request.POST.get('age')
        number = request.POST.get('number')
        male = request.POST.get('name')
        female = request.POST.get('female')
        genre = request.POST.get('genre')
        address = request.POST.get('address')
        parent_selection = request.POST.get('parent_selection')
        child_selection = request.POST.get('child_selection')
        savingaccount = request.POST.get('savingaccount')
        currentaccount = request.POST.get('currentaccount')
        joinaccount = request.POST.get('joinaccount')
        demataccount = request.POST.get('demataccount')
        debitcard = request.POST.get('debitcard')
        creditcard = request.POST.get('creditcard')
        chequebook = request.POST.get('chequebook')
        forms = Form(name=name, email=email, dob=dob, age=age, number=number, male=male, female=female, genre=genre,
                     address=address, parent_selection=parent_selection, child_selection=child_selection,
                     savingaccount=savingaccount, currentaccount=currentaccount, joinaccount=joinaccount,
                     demataccount=demataccount, debitcard=debitcard, creditcard=creditcard, chequebook=chequebook)
        forms.save()
    return render(request, "form.html")


def button(request):
    return render(request, "button.html")
