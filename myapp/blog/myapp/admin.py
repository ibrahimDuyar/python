from django.contrib import admin
from myapp.models import UrunModel, ResimGaleriModel, YorumModel, KategororiModel
# Register your models here.


class UrunModelImages(admin.TabularInline):
    model = ResimGaleriModel

    extra = 5




class UrunAdmin(admin.ModelAdmin):

    inlines = [UrunModelImages]





admin.site.register(UrunModel, UrunAdmin)
admin.site.register(YorumModel)
admin.site.register(KategororiModel)
admin.site.register(ResimGaleriModel)