from django.urls import path
from . import views

urlpatterns = [

    path('', views.notifications_list,
         name='notifications'),

    # path('read/<int:noti_id>/',
    #      views.mark_as_read,
    #      name='mark_as_read'),
]
