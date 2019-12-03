from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.board_list),
    path('writer/', views.board_writer),
    path('detail/<int:pk>/', views.board_detail),
]
