from django.contrib import admin
from account.models import CastomUserModel
from django.contrib.auth.admin import UserAdmin
# Register your models here.



class CastomUserAdmin(UserAdmin):

    list_display = ('username', 'email',)

    fieldsets = UserAdmin.fieldsets + (
        ('Avatar Değiştirme Alanı',
        {'fields': ['image']}
        ),
        ('Görev Durumu',
        {'fields': ['admin']}
        ),
    )


admin.site.register(CastomUserModel, CastomUserAdmin)