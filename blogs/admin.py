from django.contrib import admin
from .models import Post, SignUp
# Register your models here.

class SignUpAdmin(admin.ModelAdmin):
	list_display = ['__str__','timestamp','updated']
	class Meta:
		model = SignUp



admin.site.register(SignUp, SignUpAdmin)
admin.site.register(Post)