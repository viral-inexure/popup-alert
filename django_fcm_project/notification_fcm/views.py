import firebase_admin
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

from fcm_django.models import FCMDevice
from firebase_admin import auth, credentials
from firebase_admin.messaging import Message, Notification
from .form import RegisterUserForm, Login_Form


class RegisterPage(CreateView):
    model = User
    template_name = 'notification_fcm/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return redirect('index')


class Login(LoginView):
    model = User
    template_name = 'notification_fcm/login.html'
    form_class = Login_Form
    success_url = reverse_lazy('index')


def sign_in(request):
    return render(request, 'notification_fcm/register.html')


def login(request):
    return render(request, 'notification_fcm/login.html')


def index(request):
    title = 'app is ready'
    body = 'notification body......'
    # device = FCMDevice.objects.all().first()
    # device.send_message(Message(
    #     notification=Notification(title=title, body=body),
    # ))

    return render(request, 'notification_fcm/index.html')


