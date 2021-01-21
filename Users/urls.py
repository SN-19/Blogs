from django.urls import include,path

from .views import *


urlpatterns=[
    path('', signup, name='signup'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout_user, name='logout')
]