from django.contrib import admin
from .models import Inbox, Setting, Dislike, Like, UserPhoto, Match, Profile

admin.site.register(UserPhoto)
admin.site.register(Profile)
admin.site.register(Setting)
admin.site.register(Like)
admin.site.register(Dislike)
admin.site.register(Inbox)
admin.site.register(Match)

# Register your models here.
