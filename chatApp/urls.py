
from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreateRoom, name='create_room'),
    path('api/', views.CreateRoomView.as_view(), name='create_room'),
    path('api/chats/<str:room_name>/', views.CheckRoomExists.as_view(), name='room'),
    path('api/chatsAll/<str:room_name>/', views.CheckRoomGet.as_view(), name='room'),
    path('<str:room_name>/<str:username>/', views.MessageView, name='room'),
]