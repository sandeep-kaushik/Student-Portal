from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	description = models.CharField(max_length=100,default='')
	city = models.CharField(max_length=100,default='')
	website = models.URLField(default='')
	phone = models.IntegerField(default=0)

	def __str__(self):
		return self.user.username



def create_profile(sender, **Kwargs):
	if Kwargs['created']:
		user_profile = UserProfile.objects.create(user=Kwargs['instance'])


post_save.connect(create_profile,sender=User)



