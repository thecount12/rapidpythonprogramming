#admin.py

from signup.models import Profile 
from django.contrib.auth.admin import UserAdmin 
from django.contrib.auth.models import User
class ProfInline(admin.StackedInline): 
	model=Profile 
class ProfAdmin(admin.ModelAdmin): 
	inlines = (ProfInline,)

admin.site.unregister(User) 
admin.site.register(User,ProfAdmin) 
