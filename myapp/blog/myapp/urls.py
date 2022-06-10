from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('yazilarim/', views.yazilarim, name='yazilarim'),
    path('yazi-ekle/', views.yazi_ekle, name='yazi-ekle'),
    path('yazar-<int:id>', views.yazar_panel, name='yazar'),
    path('yorum-duzenle-<int:id>', views.yorum_duzenle, name='yorum-duzenle'),
    path('yorum-sil-<int:id>', views.yorum_sil, name='yorum-sil'),
    path('kategor-<slug:slug>', views.Kategori, name='kategori'),
    path('details/<slug:slug>', views.details, name='details'),
]
