from django.shortcuts import render


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ApplicationForm

def send_application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ваша заявка успешно отправлена!")
            # Можно вернуть редирект на ту же страницу или на другую
            return redirect('services')
        else:
            messages.error(request, "Пожалуйста, проверьте введённые данные.")
    else:
        form = ApplicationForm()
    # Если требуется отдельная страница для обработки, можно вернуть шаблон,
    # но в данном случае форма находится в модальном окне, поэтому мы редиректим.
    return redirect('services')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')  # Создайте шаблон about.html

def services(request):
    return render(request, 'services.html')  # Создайте шаблон services.html

def contact(request):
    return render(request, 'contact.html')  # Создайте шаблон contact.html

def profile(request):
    return render(request, 'profile.html')  # Создайте шаблон profile.html

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout_user(request):
    logout(request)
    return redirect('home')




def send_application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Ваша заявка успешно отправлена!")
            # Можно вернуть редирект на ту же страницу или на другую
            return redirect('services')
        else:
            messages.error(request, "Пожалуйста, проверьте введённые данные.")
    else:
        form = ApplicationForm()
    # Если требуется отдельная страница для обработки, можно вернуть шаблон,
    # но в данном случае форма находится в модальном окне, поэтому мы редиректим.
    return redirect('services')

