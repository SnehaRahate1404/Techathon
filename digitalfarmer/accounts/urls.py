from django.urls import path
from . import views 
from .views import user_registration ,user_login , user_logout 

app_name ='accounts'

urlpatterns = [
    # path('user_registration/', views.user_registration, name='register'),
    path('login/', user_login, name="user_login"),
    path('registration/',user_registration, name='user_registration'),
    path('logout/',user_logout,name='user_logout'),
    
]
