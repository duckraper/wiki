from django.urls import path

from . import views, util

urlpatterns = [
    path("", views.index, name="index"),
    path('random', views.random_entry, name='random'),
    path('create', views.create_page, name='create'),
    path('notfound/<str:entry>', views.notfound, name='notfound'),
    path('matches', views.matches, name='matches'),
    path('<str:entry>', views.show_entry, name='entry'),
    path('<str:entry>/edit', views.edit_page, name='edit'),
]