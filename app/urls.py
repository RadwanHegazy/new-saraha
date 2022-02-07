from pathlib import PurePath
from unicodedata import name
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView, PasswordChangeView


urlpatterns = [
    path('',views.home,name='home'),
    path('login/',LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('signup/',views.signup,name='signup'),
    path('profile/',views.profile,name='profile'),
    path('profile/edit/',views.edit_profile,name='edit'),
    path('change-password/',PasswordChangeView.as_view(template_name='change_password.html'),name='password'),
    path('change-password/done',views.Pchange_done,name='password_change_done'),
    path('send/msg/<str:username>/',views.send_msg,name='send_msg'),
    path('del/<int:id>/',views.del_msg,name='del'),
    path('send/voice/msg/<str:username>/',views.upload_voice,name='voice_msg'),
    path('done/',views.done,name='done')
    
]


