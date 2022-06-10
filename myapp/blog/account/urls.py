from django.urls import path
from account import views

urlpatterns = [
    path('', views.login_user, name='login'),
    path('logout-user', views.logout_user, name='logout'),
    path('user-create',views.register_user, name='register'),
    path('user-update', views.update_user, name='update'),
    path('password-change', views.password_change, name='password'),
]
