from pyexpat import model
from pyexpat.errors import messages
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile (models.Model) :
    user = models.OneToOneField(User,related_name='profile',on_delete=models.CASCADE)
    image = models.FileField(upload_to='static/profile-images/',default='static/website-images/profile.svg',blank=True)
    email = models.EmailField(max_length=50,null=True,blank=True)


    def edit_user_image (user,image) :
        get_prof = Profile.objects.get(user=user)
        get_prof.image = image
        get_prof.save()

    def edit_name_email(user,new_name,new_email) :
        get_prof = Profile.objects.get(user=user)
        get_prof.email = new_email
        get_user = User.objects.get(username=user.username)
        get_user.username = new_name
        get_user.save()
        get_prof.save()


    def __str__(self) :
        return f"{self.user}"



class Message (models.Model) :
    text = models.CharField(max_length=200,blank=True)
    voice = models.FileField(upload_to='static/msg-voices-to-users/',blank=True)
    to_user = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)

    def create_one (user,msg) :
        msg = Message.objects.create(
            text=msg,
            to_user=Profile.objects.get(user=user)
        )
        msg.save()

    
    def __str__(self) :
        return f"{self.to_user}"