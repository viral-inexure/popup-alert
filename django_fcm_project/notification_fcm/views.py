# from django.shortcuts import render
# from firebase_admin.messaging import Message, Notification
# from fcm_django.models import FCMDevice
import firebase_admin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from firebase_admin import credentials, auth
from .form import RegisterUserForm

# Create your views here.


class RegisterPage(CreateView):
    model = User
    template_name = 'demo_app/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return redirect('login')



def index(request):
    pass
#     title = 'app is ready'
#     body = 'notification body......'
#     cred = credentials.Certificate("/home/viral/pycharm/projects/django-fcm_practice/django_fcm_project/serviceAccount.json")
#     firebase_admin.initialize_app(cred)
#     uid = 'some-uid'
#     custom_token = auth.create_custom_token(uid)
#     print(custom_token)
#     device = FCMDevice.objects.all().first()
#     device.send_message(notification=Notification(title=title, body=body),
#         topic="Optional topic parameter: Whatever you want")
#     return render(request, 'notification_fcm/index.html')


cred = credentials.Certificate("../django_fcm_project/serviceAccount.json")
firebase_admin.initialize_app(cred)
uid = 'some-uid'
custom_token = auth.create_custom_token(uid)

print(custom_token)