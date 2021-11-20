from django.contrib import admin
from users.models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')
    list_filter = ('username',)

admin.site.register(User, UserAdmin)
