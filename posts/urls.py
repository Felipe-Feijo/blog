from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts_lists, name="list"),
    path('new-post/', views.post_new, name="new-post"),
    path('<slug:slug>', views.post_page, name="page"),
    path('update/<slug:slug>', views.post_update, name="update"),
    path('delete/<slug:slug>/', views.post_delete, name="delete"),
]
