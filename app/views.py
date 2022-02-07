from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.views import auth_login
from .forms import SignupForm
from .models import Profile, Message
import os
from django.contrib import messages

# Create your views here.

def home (request) :
    if request.user.is_authenticated :
        return redirect('profile')
    else :
        return render(request,'home.html')


def signup (request) :
    form = SignupForm()
    
    if request.method == "POST" :
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user=user)
            Profile.objects.create(user=user).save()
            return redirect('home')

    return render(request,'signup.html',{'form':form})




def profile (request) :
    prof = Profile.objects.get(user=request.user)
    get_msgs = Message.objects.filter(to_user=prof).order_by('-date')
    return render(request,'profile.html',{'msgs':get_msgs})



def edit_profile (request) :
    user = request.user
    if request.method == "POST" :
        if request.FILES :
            image = request.FILES['image']
            Profile.edit_user_image(user,image)

        new_name = request.POST['name']
        new_email = request.POST['email']
        Profile.edit_name_email(user=user
        ,new_name=new_name,new_email=new_email)

        return redirect('home')

    return render(request,'edit_profile.html')


def Pchange_done (request) :
    return redirect('logout')


def send_msg (request,username) :
    if request.user.username == username :
        return HttpResponse('Sorry, but you can not send messages to your self !')
    
    send_to = User.objects.get(username=username)
    
    if request.method == "POST" :
        msg = request.POST['msg']
        Message.create_one(user=send_to,msg=msg)
        messages.add_message(request,messages.SUCCESS,'Done, Your Message Has Been sent Successfully !')
        return redirect('done')

    return render(request,'send_msg.html',{'user':send_to})

def del_msg (request,id) :
    Message.objects.get(id=id).delete()
    return redirect('home')


def SaveFileAsOgg (old_name,) :
    os.rename('.'+old_name,'.'+old_name+'.ogg')


def upload_voice(request,username) :
    get_user = User.objects.get(username=username)
    get_prof = Profile.objects.get(user=get_user)
    audio = request.FILES['audio']
    msg = Message.objects.create(to_user=get_prof,voice=audio)
    get_name = Message.objects.get(id=msg.id)
    SaveFileAsOgg(old_name=get_name.voice.url)
    return HttpResponse('Done')


def done (request) :
    return render(request,'done.html')