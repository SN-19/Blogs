from django.urls import include,path

from .views import *


urlpatterns=[
    path('createpost/',create_post),
    path('api-auth',include('rest_framework.urls')),
    path('index/',index),
    path('blogcreate/',create_post),
    path('listblogs/',list_blog),
    path('articles/<int:id>/', view_article,name='view_article'),
    path('add_likes/',add_likes)
]