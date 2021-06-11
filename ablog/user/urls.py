from django.urls import path,include
from .views import user
from django.contrib.auth.forms import User
from user import views
app_name='user'

urlpatterns = [
    path('register/',user.as_view(),name='register'),
    path('login/', views.login, name='login'),

]
